import hashlib
import re

from rank_bm25 import BM25Okapi
from langchain_core.documents import Document

from ingestion import vectorstore
from vector_retriever import retrieve_vector


DEFAULT_CANDIDATE_K = 10
DEFAULT_RRF_CONSTANT = 60


def _tokens(text: str):
    return re.findall(r"\b\w+\b", text.lower())


def _chunk_identity(document):
    """Identify a chunk without relying on a filename, which may be repeated."""
    metadata = document.metadata
    document_id = metadata.get("document_id", "")
    page = metadata.get("page", "")
    content_hash = hashlib.sha256(document.page_content.encode("utf-8")).hexdigest()
    return f"{document_id}:{page}:{content_hash}"


def _get_user_chunks(user_id: str):
    """Fetch only this user's chunks before building the in-memory BM25 index."""
    records = vectorstore.get(
        where={"user_id": user_id},
        include=["documents", "metadatas"]
    )

    documents = []
    for content, metadata in zip(
        records.get("documents", []),
        records.get("metadatas", [])
    ):
        if content is not None and metadata is not None:
            documents.append(Document(page_content=content, metadata=metadata))

    return documents


def retrieve_hybrid(
    query: str,
    user_id: str,
    k: int = 5,
    candidate_k: int = DEFAULT_CANDIDATE_K,
    rrf_constant: int = DEFAULT_RRF_CONSTANT
):
    """Fuse user-scoped vector and BM25 rankings with reciprocal rank fusion."""
    if k <= 0 or candidate_k <= 0:
        return []

    vector_results = retrieve_vector(query, user_id, candidate_k)
    user_chunks = _get_user_chunks(user_id)
    if not user_chunks:
        return []

    bm25 = BM25Okapi([_tokens(document.page_content) for document in user_chunks])
    bm25_scores = bm25.get_scores(_tokens(query))
    bm25_order = sorted(
        range(len(user_chunks)),
        key=lambda index: bm25_scores[index],
        reverse=True
    )[:candidate_k]
    bm25_results = [user_chunks[index] for index in bm25_order]

    # RRF adds 1 / (constant + rank) for each ranked list, so shared chunks
    # receive a higher score than chunks appearing in only one list.
    fused = {}
    for rank, document in enumerate(vector_results, start=1):
        identity = _chunk_identity(document)
        fused.setdefault(identity, {"score": 0.0, "document": document})
        fused[identity]["score"] += 1 / (rrf_constant + rank)

    for rank, document in enumerate(bm25_results, start=1):
        identity = _chunk_identity(document)
        fused.setdefault(identity, {"score": 0.0, "document": document})
        fused[identity]["score"] += 1 / (rrf_constant + rank)

    ranked = sorted(
        fused.values(),
        key=lambda item: item["score"],
        reverse=True
    )
    return [item["document"] for item in ranked[:k]]
