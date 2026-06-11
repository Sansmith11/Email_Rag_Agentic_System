def update_entity_register(
    entity_register,
    entities
):

    for key, values in entities.items():

        if key not in entity_register:
            continue

        for value in values:

            if value not in entity_register[key]:
                entity_register[key].append(
                    value
                )

    return entity_register