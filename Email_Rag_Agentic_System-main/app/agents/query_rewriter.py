def rewrite_query(
    query,
    entity_register
):

    rewritten_query = query

    if (
        "that pdf" in query.lower()
        and entity_register["filenames"]
    ):

        rewritten_query = query.replace(
            "that PDF",
            entity_register["filenames"][-1]
        )

    if (
        "that amount" in query.lower()
        and entity_register["amounts"]
    ):

        rewritten_query = query.replace(
            "that amount",
            entity_register["amounts"][-1]
        )

    return rewritten_query