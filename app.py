#start server: uv run uvicorn app:app --reload


from typing import List

from fastapi import FastAPI, UploadFile, File, Form, HTTPException

from document_management import delete_user_document, get_user_documents
from ingestion import ingest_pdf


app = FastAPI()


@app.post("/documents/upload")
async def upload_documents(
    user_id: str = Form(...),
    files: List[UploadFile] = File(...)
):
    uploaded_documents = []

    for file in files:
        result = await ingest_pdf(
            file=file,
            user_id=user_id
        )

        uploaded_documents.append(result)

    return {
        "user_id": user_id,
        "documents": uploaded_documents
    }


@app.get("/documents/{user_id}")
async def list_user_documents(user_id: str):
    return {
        "user_id": user_id,
        "documents": get_user_documents(user_id)
    }


@app.delete("/documents/{user_id}/{document_id}")
async def delete_document(user_id: str, document_id: str):
    deleted = delete_user_document(user_id, document_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Document not found for this user"
        )

    return {
        "message": "Document deleted successfully",
        "document_id": document_id,
        "user_id": user_id
    }