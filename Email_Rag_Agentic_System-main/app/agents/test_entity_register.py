from app.agents.entity_resolution import extract_entities
from app.agents.entity_register import update_entity_register


entity_register = {
    "people": [],
    "dates": [],
    "amounts": [],
    "filenames": [],
    "message_refs": []
}

text = """
The approved amount is $50,000.

Please review contract_v2.pdf.

Meeting date is 12/05/2001.
"""

entities = extract_entities(text)

updated = update_entity_register(
    entity_register,
    entities
)

print(updated)