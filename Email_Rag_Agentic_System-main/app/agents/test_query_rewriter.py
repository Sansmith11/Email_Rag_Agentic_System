from app.agents.query_rewriter import rewrite_query

entity_register = {
    "people": [],
    "dates": [],
    "amounts": ["$50,000"],
    "filenames": ["contract_v2.pdf"],
    "message_refs": []
}

query = "What does that PDF say about that amount?"

result = rewrite_query(
    query,
    entity_register
)

print(result)