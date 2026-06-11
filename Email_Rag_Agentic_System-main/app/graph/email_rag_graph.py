from langgraph.graph import StateGraph, END

from app.graph.state import PipelineState

from app.agents.entity_resolution_agent import (
    entity_resolution_agent
)

from app.agents.query_breakdown_agent import (
    query_breakdown_agent
)

from app.retrieval.retrieval_node import (
    retrieval_node
)

from app.agents.citation_validator_agent import (
    citation_validator_agent
)


def clarify_node(state):

    state["final_answer"] = (
        state["clarify_text"]
    )

    return state


def respond_node(state):

    return state


graph = StateGraph(PipelineState)

graph.add_node(
    "entity_resolution",
    entity_resolution_agent
)

graph.add_node(
    "query_breakdown",
    query_breakdown_agent
)

graph.add_node(
    "retrieval",
    retrieval_node
)

graph.add_node(
    "citation_validator",
    citation_validator_agent
)

graph.add_node(
    "clarify",
    clarify_node
)

graph.add_node(
    "respond",
    respond_node
)

graph.set_entry_point(
    "entity_resolution"
)

graph.add_conditional_edges(
    "entity_resolution",
    lambda s:
    "clarify"
    if s["clarify_needed"]
    else "query_breakdown"
)

graph.add_edge(
    "query_breakdown",
    "retrieval"
)

graph.add_edge(
    "retrieval",
    "citation_validator"
)

graph.add_edge(
    "clarify",
    END
)

graph.add_edge(
    "respond",
    END
)

graph.add_conditional_edges(
    "citation_validator",
    lambda s:
    "retrieval"
    if s.get(
        "retrieval_insufficient",
        False
    )
    else "respond"
)

email_rag_graph = graph.compile()