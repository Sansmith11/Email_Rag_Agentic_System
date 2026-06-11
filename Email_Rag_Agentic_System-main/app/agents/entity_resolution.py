import re


def extract_entities(text):

    entities = {
        "people": [],
        "dates": [],
        "amounts": [],
        "filenames": [],
        "message_refs": []
    }

    amounts = re.findall(
        r"\$[\d,]+",
        text
    )

    filenames = re.findall(
        r"\b[\w\-]+\.(?:pdf|doc|docx|txt|xls|xlsx)\b",
        text,
        flags=re.IGNORECASE
    )

    dates = re.findall(
        r"\d{1,2}/\d{1,2}/\d{2,4}",
        text
    )

    entities["amounts"] = amounts
    entities["dates"] = dates
    entities["filenames"] = filenames

    return entities