from app.retrieval.bm25_index import BM25Retriever

from app.attachments.attachment_retriever import (
    AttachmentRetriever
)


retriever = BM25Retriever(
    "data/processed/threaded_emails.json"
)

attachment_retriever = (
    AttachmentRetriever()
)


def retrieval_node(state):

    state["retrieval_attempt"] += 1

    thread_id = state["thread_id"]

    retrieved_chunks = []

    top_k = 3

    if state["retrieval_attempt"] > 1:
        top_k = 6

    for sub_query in state["sub_queries"]:

        # EMAIL SEARCH

        if sub_query["scope"] in [
            "email",
            "both"
        ]:

            results = retriever.search_by_thread(
                query=sub_query["text"],
                thread_id=thread_id,
                top_k=top_k
            )

            for doc, score in results:

                retrieved_chunks.append(
                    {
                        "source": "email",
                        "sub_query": sub_query["id"],
                        "score": float(score),
                        "message_id": doc["message_id"],
                        "thread_id": doc["thread_id"],
                        "subject": doc["subject"],
                        "body": doc["body"]
                    }
                )

        # ATTACHMENT SEARCH

        if sub_query["scope"] in [
            "attachment",
            "both"
        ]:

            attachment_results = (
                attachment_retriever.search(
                    sub_query["text"]
                )
            )

            for attachment in attachment_results:

                retrieved_chunks.append(
                    {
                        "source": "attachment",
                        "filename":
                        attachment["filename"],
                        "body":
                        attachment["text"]
                    }
                )

    state["retrieved_chunks"] = retrieved_chunks

    return state