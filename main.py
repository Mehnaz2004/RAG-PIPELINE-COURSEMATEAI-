from rag_service import chat


print("\nStudyLensAI CLI")
print("Press 0 to exit.")

session_id = input(
    "\nSession ID: "
).strip() or "default_session"

user_id = input(
    "User ID: "
).strip() or "user_A"


print("\n[SESSION]")
print(f"  Session ID : {session_id}")
print(f"  User ID    : {user_id}")


while True:
    question = input("\nYou: ")

    if question == "0":
        break

    if not question.strip():
        continue

    try:
        answer = chat(
            user_id=user_id,
            session_id=session_id,
            question=question
        )

        print("\nStudyLensAI:", answer)

    except Exception as e:
        print(f"\nError: {e}")