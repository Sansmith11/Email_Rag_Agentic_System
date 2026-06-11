from app.agents.query_breakdown_agent import query_breakdown_agent

state = {

    "resolved_query":
    "What did finance approve and when was it sent?"
}

result = query_breakdown_agent(
    state
)

for q in result["sub_queries"]:
    print(q)