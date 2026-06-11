from app.agents.entity_resolution import extract_entities


sample_text = """
The approved amount is $50,000.

Please review contract_v2.pdf.

Meeting date is 12/05/2001.
"""

entities = extract_entities(
    sample_text
)

print(entities)