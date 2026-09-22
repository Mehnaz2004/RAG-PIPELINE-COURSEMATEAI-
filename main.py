from dotenv import load_dotenv

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from hybrid_retriever import retrieve_hybrid

load_dotenv()


# -----------------------------
# 1. Load embedding model
# -----------------------------

print("\n[INIT] Loading embedding model...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("[INIT] Embedding model loaded.")


# -----------------------------
# 2. Load LLM
# -----------------------------

print("\n[INIT] Loading LLM...")

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

print("[INIT] LLM loaded: openai/gpt-oss-20b")


# -----------------------------
# 3. Create prompt with history
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
        MessagesPlaceholder(variable_name="chat_history"),
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


SESSION_STORE = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    """Return the in-memory history for a session; create one if needed."""
    if session_id not in SESSION_STORE:
        SESSION_STORE[session_id] = InMemoryChatMessageHistory()
    return SESSION_STORE[session_id]


print("\nRAG system created!")
print("Press 0 to exit.")
print("Enter a session id to keep the conversation. Press Enter for a default session.")

session_id = input("\nSession ID: ").strip() or "default_session"
user_id = input("User ID: ").strip() or "user_A"

history = get_session_history(session_id)

print("\n[SESSION]")
print(f"  Session ID : {session_id}")
print(f"  User ID    : {user_id}")
print(f"  History    : {len(history.messages)} messages")


# -----------------------------
# 4. Chat loop
# -----------------------------

while True:

    query = input("\nYou: ")

    if query == "0":
        break

    if not query.strip():
        continue


    # =========================================================
    # DEBUG 1 — USER QUERY
    # =========================================================

    print("\n" + "=" * 70)
    print("[DEBUG] USER QUERY")
    print("=" * 70)

    print(query)


    # =========================================================
    # DEBUG 2 — RETRIEVAL INPUT
    # =========================================================

    print("\n" + "=" * 70)
    print("[DEBUG] RETRIEVAL")
    print("=" * 70)

    print(f"User ID : {user_id}")
    print(f"Query   : {query}")
    print("Calling retrieve_hybrid()...")


    # Retrieve relevant chunks using the current question only.
    docs = retrieve_hybrid(
        query=query,
        user_id=user_id,
        k=5,
    )


    # =========================================================
    # DEBUG 3 — RETRIEVAL RESULTS
    # =========================================================

    print("\n" + "-" * 70)
    print(f"[DEBUG] RETRIEVAL RESULTS — {len(docs)} documents")
    print("-" * 70)

    if not docs:

        print("No documents retrieved.")

    else:

        for i, doc in enumerate(docs, start=1):

            print(f"\n--- Retrieved Document {i} ---")

            print("Metadata:")
            print(doc.metadata)

            print("\nContent:")
            print(doc.page_content)


    # =========================================================
    # DEBUG 4 — BUILD CONTEXT
    # =========================================================

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    ) if docs else "No relevant document context found."

    print("\n" + "=" * 70)
    print("[DEBUG] CONTEXT SENT TO LLM")
    print("=" * 70)

    print(context)


    # =========================================================
    # DEBUG 5 — CHAT HISTORY
    # =========================================================

    print("\n" + "=" * 70)
    print("[DEBUG] CHAT HISTORY")
    print("=" * 70)

    print(f"Messages in history: {len(history.messages)}")

    if history.messages:

        for i, message in enumerate(history.messages, start=1):

            print(f"\nMessage {i}")
            print(f"Type: {type(message).__name__}")
            print(f"Content: {message.content}")

    else:

        print("No previous conversation.")


    # =========================================================
    # DEBUG 6 — FILLED PROMPT
    # =========================================================

    final_prompt = prompt.invoke(
        {
            "chat_history": history.messages,
            "context": context,
            "question": query
        }
    )

    print("\n" + "=" * 70)
    print("[DEBUG] FINAL PROMPT SENT TO LLM")
    print("=" * 70)

    print(final_prompt)


    # =========================================================
    # DEBUG 7 — INDIVIDUAL PROMPT MESSAGES
    # =========================================================

    print("\n" + "-" * 70)
    print("[DEBUG] PROMPT MESSAGES")
    print("-" * 70)

    for i, message in enumerate(final_prompt.messages, start=1):

        print(f"\n--- Message {i} ---")
        print(f"Type: {type(message).__name__}")
        print(message.content)


    # =========================================================
    # DEBUG 8 — LLM CALL
    # =========================================================

    print("\n" + "=" * 70)
    print("[DEBUG] CALLING LLM")
    print("=" * 70)

    print("Model: openai/gpt-oss-20b")

    response = llm.invoke(final_prompt)

    answer = response.content


    # =========================================================
    # DEBUG 9 — LLM RESPONSE
    # =========================================================

    print("\n" + "=" * 70)
    print("[DEBUG] LLM RESPONSE")
    print("=" * 70)

    print(answer)


    # =========================================================
    # DEBUG 10 — UPDATE HISTORY
    # =========================================================

    history.add_messages([
        HumanMessage(content=query),
        AIMessage(content=answer)
    ])

    print("\n" + "=" * 70)
    print("[DEBUG] HISTORY UPDATED")
    print("=" * 70)

    print(f"Total messages now: {len(history.messages)}")