from app.attachments.attachment_retriever import (
    AttachmentRetriever
)

retriever = (
    AttachmentRetriever()
)

results = retriever.search(
    "finance approved"
)

print(results)