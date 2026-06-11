from app.agents.entity_resolution import extract_entities
from app.agents.entity_register import update_entity_register
from app.agents.query_rewriter import rewrite_query
from app.agents.clarification import check_clarification
from app.utils.logger import log_agent_event

def entity_resolution_agent(state):

    raw_query = state["raw_query"]

    entities = extract_entities(
        raw_query
    )

    state["entity_register"] = update_entity_register(
        state["entity_register"],
        entities
    )

    clarify_needed, clarify_text = check_clarification(
        raw_query,
        state["entity_register"]
    )

    resolved_query = rewrite_query(
        raw_query,
        state["entity_register"]
    )

    state["resolved_query"] = resolved_query

    state["clarify_needed"] = clarify_needed

    state["clarify_text"] = clarify_text
    
    log_agent_event(
    {
        "agent": "entity_resolution",
        "input": {
            "raw_query": raw_query
        },
        "output": {
            "resolved_query": resolved_query,
            "clarify_needed": clarify_needed,
            "clarify_text": clarify_text
        }
    }
)
    return state