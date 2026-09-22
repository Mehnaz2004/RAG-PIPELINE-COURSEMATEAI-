from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage


MAX_TURNS = 10
MAX_MESSAGES = MAX_TURNS * 2

SESSION_STORE = {}


def get_session_history(
    user_id: str,
    session_id: str
) -> InMemoryChatMessageHistory:
    """
    Return the conversation history for a user's session.

    Sessions are scoped by both user_id and session_id so that
    two users cannot accidentally share the same session id.
    """
    session_key = (user_id, session_id)

    if session_key not in SESSION_STORE:
        SESSION_STORE[session_key] = InMemoryChatMessageHistory()

    return SESSION_STORE[session_key]


def add_turn(
    user_id: str,
    session_id: str,
    question: str,
    answer: str
):
    """
    Add one user/assistant turn to the session.

    A turn consists of:
        1 HumanMessage
        1 AIMessage

    Only the latest MAX_TURNS are kept.
    """
    history = get_session_history(
        user_id=user_id,
        session_id=session_id
    )

    history.add_messages([
        HumanMessage(content=question),
        AIMessage(content=answer)
    ])

    if len(history.messages) > MAX_MESSAGES:
        history.messages = history.messages[-MAX_MESSAGES:]


def clear_session(
    user_id: str,
    session_id: str
):
    """Delete a user's conversation session."""
    session_key = (user_id, session_id)
    SESSION_STORE.pop(session_key, None)