from ingestion import vectorstore


def retrieve_vector(query: str, user_id: str, k: int = 5):
    """Return the top vector matches restricted to one user."""
    if k <= 0:
        return []

    return vectorstore.similarity_search(
        query=query,
        k=k,
        filter={"user_id": user_id}
    )
