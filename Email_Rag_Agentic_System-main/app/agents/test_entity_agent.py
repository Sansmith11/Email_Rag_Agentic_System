from app.agents.entity_resolution_agent import entity_resolution_agent


state = {

    "raw_query":
    "What does that PDF say about that amount?",

    "entity_register": {

        "people": [],

        "dates": [],

        "amounts": ["$50,000"],

        "filenames": ["contract_v2.pdf"],

        "message_refs": []
    }
}

result = entity_resolution_agent(
    state
)

print(result["resolved_query"])

print(result["clarify_needed"])