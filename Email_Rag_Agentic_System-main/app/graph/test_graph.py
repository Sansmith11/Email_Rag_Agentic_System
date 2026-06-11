from app.graph.email_rag_graph import (
    email_rag_graph
)

state = {

    "session_id": "s1",

    "thread_id": "T-0002",

    "turn_history": [],

    "entity_register": {
        "people": [],
        "dates": [],
        "amounts": [],
        "filenames": [],
        "message_refs": []
    },

    "raw_query": "issues",

    "resolved_query": "",

    "clarify_needed": False,

    "clarify_text": None,

    "sub_queries": [],

    "retrieved_chunks": [],

    "retrieval_attempt": 0,

    "draft_answer": "",

    "citations": [],

    "grounding_score": 0.0,

    "retrieval_insufficient": False,

    "final_answer": ""
}

result = email_rag_graph.invoke(
    state
)

print(
    result["final_answer"]
)

print(
    result["citations"]
)