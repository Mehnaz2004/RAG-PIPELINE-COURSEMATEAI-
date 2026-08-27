#INGESTION TEST CODES
#curl.exe -X POST "http://127.0.0.1:8000/documents/upload" -F "user_id=user_A" -F "files=@C:\Users\mehna\OneDrive\Desktop\Small_project\2026\CourseMateAI\documents\Python.pdf"

#list documents for user_A
#curl.exe "http://127.0.0.1:8000/documents/user_A"

#delete documents from user_A
#curl.exe -X DELETE "http://127.0.0.1:8000/documents/user_A/YOUR_DOCUMENT_ID"

import os
import shutil
import uuid
import traceback
import chromadb

from dotenv import load_dotenv
from fastapi import UploadFile, HTTPException
from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# -----------------------------
# Configuration
# -----------------------------

load_dotenv()

TEMP_UPLOAD_PATH = "temp_uploads"

CHROMA_API_KEY = os.getenv("CHROMA_API_KEY")
CHROMA_TENANT = os.getenv("CHROMA_TENANT")
CHROMA_DATABASE = os.getenv("CHROMA_DATABASE")

os.makedirs(TEMP_UPLOAD_PATH, exist_ok=True)


# -----------------------------
# Load embedding model once
# -----------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# Connect to Chroma Cloud
# -----------------------------

chroma_client = chromadb.CloudClient(
    api_key=CHROMA_API_KEY,
    tenant=CHROMA_TENANT,
    database=CHROMA_DATABASE
)


# -----------------------------
# Connect LangChain to Chroma
# -----------------------------

vectorstore = Chroma(
    client=chroma_client,
    collection_name="studylens_documents",
    embedding_function=embedding_model
)


# -----------------------------
# Text splitter
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2700,
    chunk_overlap=300
)


# -----------------------------
# Ingest one PDF
# -----------------------------

async def ingest_pdf(
    file: UploadFile,
    user_id: str
):

    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail=f"{file.filename} is not a valid PDF"
        )

    document_id = str(uuid.uuid4())

    temp_filename = f"{document_id}_{file.filename}"

    temp_path = os.path.join(
        TEMP_UPLOAD_PATH,
        temp_filename
    )

    try:

        # Save uploaded PDF temporarily
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )


        # Read PDF
        reader = PdfReader(temp_path)

        documents = []


        # Convert pages into LangChain Documents
        for page_number, page in enumerate(reader.pages):

            page_text = page.extract_text()

            if not page_text or not page_text.strip():
                continue

            document = Document(
                page_content=page_text,
                metadata={
                    "user_id": user_id,
                    "document_id": document_id,
                    "filename": file.filename,
                    "page": page_number + 1
                }
            )

            documents.append(document)


        if not documents:
            raise HTTPException(
                status_code=400,
                detail=f"No readable text found in {file.filename}"
            )


        # Split pages into chunks
        chunks = text_splitter.split_documents(
            documents
        )


        # Debug: print one chunk
        if chunks:
            print("\n" + "=" * 50)
            print("DEBUG: SAMPLE CHUNK")
            print("=" * 50)

            print("\nCONTENT:\n")
            print(chunks[0].page_content[:500])

            print("\nMETADATA:\n")
            print(chunks[0].metadata)

            print("=" * 50 + "\n")


        # Store chunks in Chroma Cloud
        # LangChain uses YOUR embedding model
        vectorstore.add_documents(
            documents=chunks
        )


        return {
            "document_id": document_id,
            "filename": file.filename
        }


    except HTTPException:
        raise


    except Exception as e:
        print("\n" + "=" * 50)
        print("INGESTION ERROR:")
        print("=" * 50)

        traceback.print_exc()

        print("=" * 50 + "\n")

        raise HTTPException(
            status_code=500,
            detail=f"Failed to process {file.filename}: {str(e)}"
        )


    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)


# -----------------------------
# Debug: test user-based retrieval
# -----------------------------

def test_user_retrieval(
    query: str,
    user_id: str
):

    results = vectorstore.similarity_search(
        query=query,
        k=5,
        filter={
            "user_id": user_id
        }
    )

    print("\n" + "=" * 50)
    print(f"DEBUG: RETRIEVAL FOR {user_id}")
    print("=" * 50)

    if not results:
        print("\nNO DOCUMENTS FOUND FOR THIS USER.\n")

    for index, document in enumerate(results, start=1):

        print(f"\nRESULT {index}")

        print("\nCONTENT:\n")
        print(document.page_content[:500])

        print("\nMETADATA:\n")
        print(document.metadata)

        print("-" * 50)

    return results