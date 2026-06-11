from app.retrieval.retrieval_node import retrieval_node


state = {

    "thread_id": "T-0002",

    "sub_queries": [
        {
            "id": "q1",
            "text": "issues",
            "scope": "both",
            "priority": 1
        }
    ]
}

result = retrieval_node(
    state
)

print(
    "Retrieved:",
    len(result["retrieved_chunks"])
)

print(
    result["retrieved_chunks"][0]
)