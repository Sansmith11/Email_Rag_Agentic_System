from app.agents.citation_validator_agent import (
    citation_validator_agent
)

state = {

    "retrieved_chunks": [

        {
            "message_id":
            "msg_123",

            "body":
            "Finance approved the proposal."
        }
    ]
}

result = citation_validator_agent(
    state
)

print(
    result["final_answer"]
)

print(
    result["citations"]
)

print(
    result["grounding_score"]
)