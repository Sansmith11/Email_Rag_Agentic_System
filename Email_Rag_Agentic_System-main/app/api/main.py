from fastapi import FastAPI

from app.api.models import (
    StartSessionRequest,
    AskRequest,
    SwitchThreadRequest
)

from app.utils.logger import (
    create_trace_id,
    read_trace_events
)

from app.graph.email_rag_graph import (
    email_rag_graph
)

from app.memory.session_store import (
    SessionStore
)

app = FastAPI(
    title="Email RAG Agentic System"
)

session_store = SessionStore()


@app.get("/")
def home():

    return {
        "status": "running"
    }


@app.post("/start_session")
def start_session(
    request: StartSessionRequest
):

    session_id = (
        session_store.start_session(
            request.thread_id
        )
    )

    return {
        "session_id": session_id,
        "thread_id": request.thread_id
    }


@app.post("/ask")
def ask_question(
    request: AskRequest
):

    trace_id = create_trace_id()

    session = session_store.get_session(
        request.session_id
    )

    if not session:

        return {
            "error":
            "Invalid session_id"
        }

    state = {

        "trace_id":
        trace_id,

        "session_id":
        request.session_id,

        "thread_id":
        session["thread_id"],

        "turn_history":
        session["turn_history"],

        "entity_register":
        session["entity_register"],

        "raw_query":
        request.text,

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

    events = read_trace_events()

    agent_trace = []

    for event in events[-10:]:

        if "agent" in event:

            agent_trace.append(
                {
                    "agent":
                    event.get(
                        "agent"
                    )
                }
            )

    return {

        "trace_id":
        trace_id,

        "answer":
        result["final_answer"],

        "citations":
        result["citations"],

        "rewrite":
        result["resolved_query"],

        "grounding_score":
        result["grounding_score"],

        "retrieved":
        result["retrieved_chunks"],

        "entity_register":
        result["entity_register"],

        "agent_trace":
        agent_trace
    }


@app.post("/switch_thread")
def switch_thread(
    request: SwitchThreadRequest
):

    success = (
        session_store.switch_thread(
            request.session_id,
            request.thread_id
        )
    )

    return {
        "success": success,
        "thread_id":
        request.thread_id
    }


@app.post("/reset_session")
def reset_session(
    session_id: str
):

    success = (
        session_store.reset_session(
            session_id
        )
    )

    return {
        "success": success
    }