from ingestion import test_user_retrieval


print("\n" + "#" * 60)
print("TEST 1: USER A SEARCHING FOR FLASK")
print("#" * 60)

test_user_retrieval(
    query="What is Flask?",
    user_id="user_A"
)


print("\n" + "#" * 60)
print("TEST 2: USER B SEARCHING FOR FLASK")
print("#" * 60)

test_user_retrieval(
    query="What is Flask?",
    user_id="user_b"
)


print("\n" + "#" * 60)
print("TEST 3: USER A SEARCHING FOR PYTHON")
print("#" * 60)

test_user_retrieval(
    query="What is Python?",
    user_id="user_A"
)


print("\n" + "#" * 60)
print("TEST 4: NONEXISTENT USER")
print("#" * 60)

test_user_retrieval(
    query="What is Django?",
    user_id="user_C"
)