from app.retrieval.bm25_index import BM25Retriever


retriever = BM25Retriever(
    "data/processed/threaded_emails.json"
)

results = retriever.search(
    "issues",
    top_k=3
)

for idx, (doc, score) in enumerate(results, start=1):

    print("\n====================")
    print("Rank:", idx)
    print("Score:", round(score, 2))
    print("Thread:", doc["thread_id"])
    print("Subject:", doc["subject"])
    print("Message ID:", doc["message_id"])
    print("Body:", doc["body"][:300])