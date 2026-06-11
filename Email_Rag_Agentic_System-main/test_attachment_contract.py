from app.attachments.attachment_retriever import (
    AttachmentRetriever
)

retriever = AttachmentRetriever()

results = retriever.search(
    "contract"
)

print(results)