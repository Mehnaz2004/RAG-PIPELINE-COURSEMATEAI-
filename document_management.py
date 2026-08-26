from ingestion import vectorstore


def get_user_documents(user_id: str):
    records = vectorstore.get(
        where={"user_id": user_id},
        include=["metadatas"]
    )

    documents = []
    seen_document_ids = set()

    for metadata in records.get("metadatas", []):
        if not metadata:
            continue

        document_id = metadata.get("document_id")
        if not document_id or document_id in seen_document_ids:
            continue

        seen_document_ids.add(document_id)
        documents.append({
            "document_id": document_id,
            "filename": metadata.get("filename")
        })

    return documents


def delete_user_document(user_id: str, document_id: str):
    records = vectorstore.get(
        where={
            "$and": [
                {"user_id": user_id},
                {"document_id": document_id}
            ]
        },
        include=[]
    )

    chunk_ids = records.get("ids", [])
    if not chunk_ids:
        return False

    vectorstore.delete(ids=chunk_ids)
    return True