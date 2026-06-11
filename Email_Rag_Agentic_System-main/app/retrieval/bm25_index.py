import json
from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, json_path):

        with open(
            json_path,
            "r",
            encoding="utf-8"
        ) as f:

            self.documents = json.load(f)

        self.corpus = [
            doc["body"].lower().split()
            for doc in self.documents
        ]

        self.bm25 = BM25Okapi(self.corpus)

    def search(
        self,
        query,
        top_k=5
    ):

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        ranked = sorted(
            zip(
                self.documents,
                scores
            ),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]

    def search_by_thread(
        self,
        query,
        thread_id,
        top_k=5
    ):

        filtered_docs = [
            doc
            for doc in self.documents
            if doc["thread_id"] == thread_id
        ]

        if not filtered_docs:
            return []

        corpus = [
            doc["body"].lower().split()
            for doc in filtered_docs
        ]

        bm25 = BM25Okapi(corpus)

        scores = bm25.get_scores(
            query.lower().split()
        )

        ranked = sorted(
            zip(filtered_docs, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]