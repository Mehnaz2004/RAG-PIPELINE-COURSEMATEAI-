from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_groq import ChatGroq

from hybrid_retriever import retrieve_hybrid
from memory import add_turn, get_session_history


load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


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


chain = prompt | llm | StrOutputParser()

def chat(
    user_id: str,
    session_id: str,
    question: str,
    k: int = 5
) -> str:

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    print("\n" + "=" * 80)
    print("RAG DEBUG")
    print("=" * 80)

    print("\n[1] REQUEST")
    print(f"User ID    : {user_id}")
    print(f"Session ID : {session_id}")
    print(f"Question   : {question}")

    # --------------------------------------------------
    # MEMORY
    # --------------------------------------------------

    history = get_session_history(
        user_id=user_id,
        session_id=session_id
    )

    print("\n[2] CHAT HISTORY SENT TO PROMPT")

    if not history.messages:
        print("  <empty>")
    else:
        for index, message in enumerate(history.messages, start=1):
            print(
                f"\n  Message {index}"
                f"\n  Type    : {type(message).__name__}"
                f"\n  Content : {message.content}"
            )

    # --------------------------------------------------
    # RETRIEVAL
    # --------------------------------------------------

    docs = retrieve_hybrid(
        query=question,
        user_id=user_id,
        k=k
    )

    print("\n[3] RETRIEVED DOCUMENTS")
    print(f"Number of chunks retrieved: {len(docs)}")

    if not docs:
        print("  <none>")

    for index, document in enumerate(docs, start=1):
        print("\n" + "-" * 60)
        print(f"CHUNK {index}")

        print("\nMetadata:")
        print(document.metadata)

        print("\nContent:")
        print(document.page_content[:1500])

    # --------------------------------------------------
    # CONTEXT
    # --------------------------------------------------

    context = "\n\n".join(
        document.page_content
        for document in docs
    )

    if not context:
        context = "No relevant document context found."

    print("\n[4] CONTEXT SENT TO LLM")
    print("-" * 60)
    print(context)
    print("-" * 60)

    # --------------------------------------------------
    # FINAL INPUT
    # --------------------------------------------------

    print("\n[5] INVOKING LLM...")

    answer = chain.invoke({
        "chat_history": history.messages,
        "context": context,
        "question": question
    })

    # --------------------------------------------------
    # MEMORY UPDATE
    # --------------------------------------------------

    add_turn(
        user_id=user_id,
        session_id=session_id,
        question=question,
        answer=answer
    )

    print("\n[6] ANSWER")
    print(answer)

    print("\n[7] MEMORY AFTER THIS TURN")
    updated_history = get_session_history(
        user_id=user_id,
        session_id=session_id
    )

    print(f"Messages stored: {len(updated_history.messages)}")

    for index, message in enumerate(
        updated_history.messages,
        start=1
    ):
        print(
            f"  {index}. "
            f"{type(message).__name__}: "
            f"{message.content}"
        )

    print("\n" + "=" * 80)
    print("END RAG DEBUG")
    print("=" * 80 + "\n")

    return answer