import os
import shutil
import uuid

from fastapi import UploadFile, HTTPException
from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# -----------------------------
# Configuration
# -----------------------------

CHROMA_PATH = "chroma_db"
TEMP_UPLOAD_PATH = "temp_uploads"

os.makedirs(TEMP_UPLOAD_PATH, exist_ok=True)


# -----------------------------
# Load embedding model once
# -----------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# Load persistent Chroma DB
# -----------------------------

vectorstore = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_model
)


# -----------------------------
# Text splitter
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


# -----------------------------
# Ingest one PDF
# -----------------------------

async def ingest_pdf(
    file: UploadFile,
    user_id: str
):

    # Validate file type
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail=f"{file.filename} is not a valid PDF"
        )

    # Generate unique ID for this uploaded document
    document_id = str(uuid.uuid4())

    # Collision-safe temporary filename
    temp_filename = f"{document_id}_{file.filename}"

    temp_path = os.path.join(
        TEMP_UPLOAD_PATH,
        temp_filename
    )

    try:

        # -----------------------------
        # Save uploaded PDF temporarily
        # -----------------------------

        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )


        # -----------------------------
        # Read PDF using pypdf
        # -----------------------------

        reader = PdfReader(temp_path)

        documents = []


        # -----------------------------
        # Convert each page into a
        # LangChain Document
        # -----------------------------

        for page_number, page in enumerate(reader.pages):

            page_text = page.extract_text()

            # Skip pages with no extractable text
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


        # Ensure usable text was extracted
        if not documents:
            raise HTTPException(
                status_code=400,
                detail=f"No readable text found in {file.filename}"
            )


        # -----------------------------
        # Split pages into chunks
        # -----------------------------

        chunks = text_splitter.split_documents(
            documents
        )


        # -----------------------------
        # Debug: print one chunk
        # -----------------------------

        if chunks:
            print("\n" + "=" * 50)
            print("DEBUG: SAMPLE CHUNK")
            print("=" * 50)
            print("\nCONTENT:\n")
            print(chunks[0].page_content[:500])

            print("\nMETADATA:\n")
            print(chunks[0].metadata)
            print("=" * 50 + "\n")


        # -----------------------------
        # Store chunks in persistent
        # local Chroma database
        # -----------------------------

        vectorstore.add_documents(
            documents=chunks
        )


        # -----------------------------
        # Return successful ingestion
        # -----------------------------

        return {
            "document_id": document_id,
            "filename": file.filename
        }


    except HTTPException:
        raise


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to process {file.filename}: {str(e)}"
        )


    finally:

        # -----------------------------
        # Delete temporary file
        # -----------------------------

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