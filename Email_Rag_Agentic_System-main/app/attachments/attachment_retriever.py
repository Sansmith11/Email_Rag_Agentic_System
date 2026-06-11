from app.attachments.attachment_loader import (
    load_attachments
)


class AttachmentRetriever:

    def __init__(self):

        self.attachments = (
            load_attachments()
        )

    def search(
        self,
        query
    ):

        query_words = (
            query.lower().split()
        )

        results = []

        for attachment in self.attachments:

            text = (
                attachment["text"]
                .lower()
            )

            if any(
                word in text
                for word in query_words
            ):

                results.append(
                    attachment
                )

        return results