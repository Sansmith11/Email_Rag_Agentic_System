from typing import TypedDict, Any


class PipelineState(TypedDict):

    session_id: str

    thread_id: str

    turn_history: list

    entity_register: dict[str, Any]

    raw_query: str

    resolved_query: str

    clarify_needed: bool

    clarify_text: str | None

    sub_queries: list

    retrieved_chunks: list

    retrieval_attempt: int

    draft_answer: str

    citations: list

    grounding_score: float

    retrieval_insufficient: bool

    final_answer: str