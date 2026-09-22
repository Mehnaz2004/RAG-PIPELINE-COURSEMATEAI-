import hashlib
import re

from langchain_core.documents import Document
from rank_bm25 import BM25Okapi

from ingestion import vectorstore
from vector_retriever import retrieve_vector


DEFAULT_CANDIDATE_K = 10
DEFAULT_RRF_CONSTANT = 60


def _tokenize(text: str) -> list[str]:
    """Convert text into lowercase tokens for BM25."""
    return re.findall(r"\b\w+\b", text.lower())


def _chunk_identity(document: Document) -> str:
    """
    Create a stable identity for a chunk.

    The same filename can exist in multiple documents, so identity is based
    on document metadata and the chunk content.
    """
    metadata = document.metadata

    document_id = metadata.get("document_id", "")
    page = metadata.get("page", "")

    content_hash = hashlib.sha256(
        document.page_content.encode("utf-8")
    ).hexdigest()

    return f"{document_id}:{page}:{content_hash}"


def _get_user_chunks(user_id: str) -> list[Document]:
    """
    Fetch all chunks belonging to a specific user.

    These chunks are used to build the user-scoped BM25 index.
    """
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
            documents.append(
                Document(
                    page_content=content,
                    metadata=metadata
                )
            )

    return documents


def _retrieve_bm25(
    query: str,
    documents: list[Document],
    k: int
) -> list[Document]:
    """Retrieve the top-k documents using BM25."""
    if not documents:
        return []

    tokenized_documents = [
        _tokenize(document.page_content)
        for document in documents
    ]

    bm25 = BM25Okapi(tokenized_documents)

    query_tokens = _tokenize(query)

    if not query_tokens:
        return []

    scores = bm25.get_scores(query_tokens)

    ranked_indices = sorted(
        range(len(documents)),
        key=lambda index: scores[index],
        reverse=True
    )

    return [
        documents[index]
        for index in ranked_indices[:k]
    ]


def _fuse_with_rrf(
    result_lists: list[list[Document]],
    rrf_constant: int
) -> list[Document]:
    """
    Combine multiple ranked result lists using Reciprocal Rank Fusion.
    """
    fused = {}

    for results in result_lists:

        for rank, document in enumerate(results, start=1):

            identity = _chunk_identity(document)

            if identity not in fused:
                fused[identity] = {
                    "score": 0.0,
                    "document": document
                }

            fused[identity]["score"] += (
                1 / (rrf_constant + rank)
            )

    ranked = sorted(
        fused.values(),
        key=lambda item: item["score"],
        reverse=True
    )

    return [
        item["document"]
        for item in ranked
    ]


def retrieve_hybrid(
    query: str,
    user_id: str,
    k: int = 3,
    candidate_k: int = DEFAULT_CANDIDATE_K,
    rrf_constant: int = DEFAULT_RRF_CONSTANT
) -> list[Document]:
    """
    Retrieve relevant chunks for a user using:

    1. Vector similarity search
    2. BM25 keyword search
    3. Reciprocal Rank Fusion
    """

    if not query.strip():
        return []

    if k <= 0 or candidate_k <= 0:
        return []

    # Ensure enough candidates are retrieved to satisfy the final result count.
    candidate_k = max(candidate_k, k)

    # -----------------------------
    # Vector retrieval
    # -----------------------------

    vector_results = retrieve_vector(
        query=query,
        user_id=user_id,
        k=candidate_k
    )

    # -----------------------------
    # Fetch only this user's chunks
    # for BM25 retrieval
    # -----------------------------

    user_chunks = _get_user_chunks(user_id)

    if not user_chunks:
        return []

    # -----------------------------
    # BM25 retrieval
    # -----------------------------

    bm25_results = _retrieve_bm25(
        query=query,
        documents=user_chunks,
        k=candidate_k
    )

    # -----------------------------
    # Reciprocal Rank Fusion
    # -----------------------------

    fused_results = _fuse_with_rrf(
        result_lists=[
            vector_results,
            bm25_results
        ],
        rrf_constant=rrf_constant
    )

    return fused_results[:k]