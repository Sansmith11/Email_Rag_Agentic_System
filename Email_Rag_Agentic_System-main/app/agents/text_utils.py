import re


def extract_relevant_sentences(
    text,
    query,
    max_sentences=5
):

    query_words = set(
        query.lower().split()
    )

    sentences = re.split(
        r'(?<=[.!?])\s+',
        text.replace("\n", " ")
    )

    scored = []

    for sentence in sentences:

        sentence_words = set(
            sentence.lower().split()
        )

        overlap = len(
            query_words.intersection(
                sentence_words
            )
        )

        scored.append(
            (
                overlap,
                sentence.strip()
            )
        )

    scored.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    selected = []

    for score, sentence in scored:

        if score <= 0:
            continue

        if len(sentence.strip()) < 20:
            continue

        if "Forwarded by" in sentence:
            continue

        if "To:" in sentence:
            continue

        if "Subject:" in sentence:
            continue

        selected.append(
            sentence.strip()
        )

        if len(selected) >= max_sentences:
            break

    return selected

def extract_todo_section(text):

    start = text.find(
        "Things left to do:"
    )

    if start == -1:
        return None

    end = text.find(
        "Things requested thus far"
    )

    if end == -1:
        end = len(text)

    return text[start:end]
def calculate_grounding_score(
    answer,
    source_text
):

    answer_words = set(
        answer.lower().split()
    )

    source_words = set(
        source_text.lower().split()
    )

    if not answer_words:
        return 0.0

    overlap = len(
        answer_words.intersection(
            source_words
        )
    )

    score = overlap / len(
        answer_words
    )

    return round(score, 2)