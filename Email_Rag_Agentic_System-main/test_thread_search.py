from app.retrieval.bm25_index import BM25Retriever

retriever = BM25Retriever(
    "data/processed/threaded_emails.json"
)

results = retriever.search_by_thread(
    query="issues",
    thread_id="T-0002",
    top_k=3
)

for doc, score in results:

    print("\n================")
    print("Score:", round(score, 2))
    print("Thread:", doc["thread_id"])
    print("Subject:", doc["subject"])