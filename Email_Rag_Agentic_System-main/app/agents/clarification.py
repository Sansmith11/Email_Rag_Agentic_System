def check_clarification(
    query,
    entity_register
):

    query_lower = query.lower()

    if (
        "that pdf" in query_lower
        and not entity_register["filenames"]
    ):

        return (
            True,
            "Which PDF are you referring to?"
        )

    if (
        "that amount" in query_lower
        and not entity_register["amounts"]
    ):

        return (
            True,
            "Which amount are you referring to?"
        )

    return (
        False,
        None
    )