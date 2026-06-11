from app.utils.logger import log_agent_event

from app.agents.text_utils import (
    extract_relevant_sentences,
    extract_todo_section
)

from app.agents.text_utils import (
    calculate_grounding_score
)


def citation_validator_agent(state):

    retrieved_chunks = state["retrieved_chunks"]

    if not retrieved_chunks:

        state["draft_answer"] = (
            "No relevant information found."
        )

        state["citations"] = []

        state["grounding_score"] = 0.0

        state["retrieval_insufficient"] = False

        state["final_answer"] = (
            "No relevant information found."
        )

        return state

    top_chunk = retrieved_chunks[0]

    query_text = ""

    if state["sub_queries"]:

        query_text = (
            state["sub_queries"][0]["text"]
        )

    if (
        "task" in query_text.lower()
        or "to do" in query_text.lower()
    ):

        todo_text = extract_todo_section(
            top_chunk["body"]
        )

        if todo_text:

            relevant_sentences = (
                extract_relevant_sentences(
                    todo_text,
                    query_text
                )
            )

        else:

            relevant_sentences = (
                extract_relevant_sentences(
                    top_chunk["body"],
                    query_text
                )
            )

    else:

        relevant_sentences = (
            extract_relevant_sentences(
                top_chunk["body"],
                query_text
            )
        )

    if relevant_sentences:

        draft_answer = (
            "Key findings:\n\n- "
            + "\n- ".join(
                relevant_sentences
            )
        )

    else:

        draft_answer = (
            top_chunk["body"][:300]
        )

    source_id = (
        top_chunk.get("message_id")
        or top_chunk.get("filename")
        or "unknown"
    )

    citations = [
        {
            "claim_text": draft_answer,
            "source_id": source_id,
            "page_no": None,
            "confidence": 1.0
        }
    ]

    state["draft_answer"] = draft_answer

    state["citations"] = citations

    state["grounding_score"] = (
        calculate_grounding_score(
            draft_answer,
            top_chunk["body"]
        )
    )

    # TEMPORARILY DISABLE RETRY LOOP
    state["retrieval_insufficient"] = False

    state["final_answer"] = (
        f"{draft_answer}\n\n"
        f"[source: {source_id}]"
    )

    log_agent_event(
        {
            "agent": "citation_validator",
            "input": {
                "retrieved_chunks":
                len(retrieved_chunks)
            },
            "output": {
                "grounding_score":
                state["grounding_score"],
                "citations":
                len(state["citations"])
            }
        }
    )

    print(
        "DEBUG:",
        "attempt=", state["retrieval_attempt"],
        "insufficient=", state["retrieval_insufficient"]
    )

    return state