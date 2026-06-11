# Dataset Information

## Dataset Name

Enron Email Dataset

---

## Description

The Enron Email Dataset is a large collection of real-world corporate email communications. It is commonly used for research in information retrieval, email analytics, natural language processing, and question answering systems.

This project uses processed threaded email conversations derived from the Enron Email Dataset.

---

## Processed Data

Processed email data is stored in:

```text
data/processed/threaded_emails.json
```

The processed file contains:

* Thread IDs
* Message IDs
* Email subjects
* Email body content
* Thread relationships

---

## Attachments

The project includes sample attachment documents for attachment retrieval testing.

Example attachment:

```text
sample_contract.txt
```

Sample contents include:

* Approved budget information
* Contract approval details
* Contract signing dates

---

## Example Thread

```text
T-0002
```

This thread is used for demonstrating:

* Email retrieval
* Attachment retrieval
* Citation generation
* Agent routing

---

## Retrieval Sources

### Email Source

Processed threaded emails stored in:

```text
data/processed/threaded_emails.json
```

### Attachment Source

Attachment documents stored in:

```text
data/attachments/
```

---

## Purpose

The dataset is used to demonstrate:

* Agentic Retrieval-Augmented Generation (RAG)
* Email search and retrieval
* Attachment search and retrieval
* Citation validation
* Session-based conversational querying
* LangGraph multi-agent orchestration

---

## Limitations

* Uses a subset of available email threads
* Limited attachment collection
* Retrieval is based primarily on BM25 and keyword matching
* No vector database is currently used

---

## Example Queries

* What are the issues discussed?
* What tasks remain to be completed?
* What does the contract say?
* What budget was approved?
* When was the contract signed?
