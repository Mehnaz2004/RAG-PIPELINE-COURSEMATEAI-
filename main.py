from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()


# -----------------------------
# 1. Load embedding model
# -----------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# 2. Load existing vector DB
# -----------------------------

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)


# -----------------------------
# 3. Create retriever
# -----------------------------

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)


# -----------------------------
# 4. Load LLM
# -----------------------------

llm = ChatMistralAI(
    model="mistral-small-2506"
)


# -----------------------------
# 5. Create prompt
# -----------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)


print("RAG system created!")
print("Press 0 to exit.")


# -----------------------------
# 6. Chat loop
# -----------------------------

while True:

    query = input("\nYou: ")

    if query == "0":
        break

    # Retrieve relevant chunks
    docs = retriever.invoke(query)

    # Convert documents into context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # Fill prompt
    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": query
        }
    )

    # Ask LLM
    response = llm.invoke(final_prompt)

    print(f"\nAI: {response.content}")