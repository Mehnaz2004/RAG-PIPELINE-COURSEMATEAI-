from typing import List

from fastapi import FastAPI, UploadFile, File, Form

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