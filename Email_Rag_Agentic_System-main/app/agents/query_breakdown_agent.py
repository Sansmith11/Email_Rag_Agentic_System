from app.utils.logger import log_agent_event


def detect_scope(query):

    return "attachment"


def query_breakdown_agent(state):

    query = state["resolved_query"]

    sub_queries = []

    query_lower = query.lower()

    if " and " in query_lower:

        parts = query.split(" and ")

        for idx, part in enumerate(parts):

            sub_queries.append(
                {
                    "id": f"q{idx+1}",
                    "text": part.strip(),
                    "scope": detect_scope(
                        part
                    ),
                    "priority": idx + 1
                }
            )

    else:

        sub_queries.append(
            {
                "id": "q1",
                "text": query,
                "scope": detect_scope(
                    query
                ),
                "priority": 1
            }
        )

    state["sub_queries"] = sub_queries

    log_agent_event(
        {
            "agent": "query_breakdown",
            "input": {
                "resolved_query": query
            },
            "output": {
                "sub_queries": sub_queries
            }
        }
    )

    return state