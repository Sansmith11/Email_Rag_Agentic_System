from app.agents.clarification import check_clarification

entity_register = {
    "people": [],
    "dates": [],
    "amounts": [],
    "filenames": [],
    "message_refs": []
}

clarify_needed, clarify_text = check_clarification(
    "What does that PDF say?",
    entity_register
)

print("Clarify Needed:", clarify_needed)
print("Question:", clarify_text)