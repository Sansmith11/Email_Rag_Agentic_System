# Email RAG Agentic System

## Overview

This project is an Agentic Retrieval-Augmented Generation (RAG) system for email intelligence. The system uses a LangGraph-based multi-agent workflow to retrieve information from email threads and attachments, validate citations, and provide grounded responses.

The application supports:

* Email retrieval from threaded email data
* Attachment retrieval from attached documents
* Citation generation
* Session-based conversations
* FastAPI backend
* Streamlit user interface
* LangGraph agent orchestration
* Trace logging

---

# Architecture

User Query

↓

Entity Resolution Agent

↓

Query Breakdown Agent

↓

Retrieval Agent

├── Email Retrieval (BM25)

└── Attachment Retrieval

↓

Citation Validator Agent

↓

Final Response

---

# Project Structure

```text
email_rag_agentic/

├── app/
│   ├── agents/
│   ├── api/
│   ├── attachments/
│   ├── graph/
│   ├── memory/
│   ├── retrieval/
│   └── utils/
│
├── data/
│   ├── attachments/
│   └── processed/
│
├── ui/
│
├── runs/
│
├── ingest.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── DATASET.md
└── sample_questions.md
```

---

# Agent Design

## Agent 1 – Entity Resolution Agent

Responsibilities:

* Process raw user query
* Normalize query text
* Resolve references and entities
* Determine whether clarification is required

Input:

* Raw user query

Output:

* Resolved query
* Clarification flags

---

## Agent 2 – Query Breakdown Agent

Responsibilities:

* Break complex queries into sub-queries
* Determine retrieval scope

Supported scopes:

* email
* attachment
* both

Input:

* Resolved query

Output:

* List of sub-queries
* Routing information

---

## Agent 3 – Citation Validator Agent

Responsibilities:

* Validate retrieved information
* Extract relevant evidence
* Generate citations
* Compute grounding score

Input:

* Retrieved chunks

Output:

* Final answer
* Citations
* Grounding score

---

# Retrieval Approach

## Email Retrieval

Email retrieval is performed using BM25 ranking over indexed threaded emails.

Features:

* Thread-aware retrieval
* Keyword matching
* Ranked retrieval

---

## Attachment Retrieval

Attachment retrieval searches indexed attachment documents.

Features:

* Keyword-based retrieval
* Attachment citation support
* Source tracking

---

# Session Management

The system supports:

* Session creation
* Session reset
* Thread switching
* Conversation history storage

Each user session maintains:

* Current thread
* Turn history
* Entity register

---

# API Endpoints

## Health Check

```http
GET /
```

Response:

```json
{
  "status": "running"
}
```

---

## Start Session

```http
POST /start_session
```

Request:

```json
{
  "thread_id": "T-0002"
}
```

---

## Ask Question

```http
POST /ask
```

Request:

```json
{
  "session_id": "SESSION_ID",
  "text": "What does the contract say?"
}
```

---

## Switch Thread

```http
POST /switch_thread
```

---

## Reset Session

```http
POST /reset_session
```

---

# Setup Instructions

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Build Index

```bash
python ingest.py
```

---

## Start FastAPI

```bash
uvicorn app.api.main:app --reload
```

FastAPI URL:

```text
http://127.0.0.1:8000/docs
```

---

## Start Streamlit UI

```bash
streamlit run ui/app.py
```

Streamlit URL:

```text
http://localhost:8501
```

---

# Docker

## Build and Run

```bash
docker compose up --build
```

Services:

* FastAPI API
* Streamlit UI

Note:

Docker configuration files are included. Local validation may depend on Docker availability on the target machine.

---

# Logging and Tracing

Agent execution traces are stored in:

```text
runs/trace.jsonl
```

Each trace contains:

* Entity Resolution Agent events
* Query Breakdown Agent events
* Citation Validator Agent events

---

# Testing

Example Questions

1. What does the contract say?
2. What budget was approved?
3. When was the contract signed?
4. What are the issues discussed?
5. What tasks remain to be completed?
6. What does the document mention?
7. What are the issues and what tasks remain?
8. What did we just discuss?

---

# Known Limitations

* BM25 retrieval only
* No vector database integration
* Basic conversational memory
* Limited attachment dataset
* No semantic reranking
* No LLM-based answer synthesis

---

# Future Improvements

* Hybrid BM25 + Vector Search
* Semantic reranking
* Improved conversational memory
* LLM-based grounded answer generation
* Multi-document reasoning
* Advanced attachment understanding

---

# Technologies Used

* Python
* LangGraph
* FastAPI
* Streamlit
* BM25 Retrieval
* JSON Data Storage
* Docker
* Docker Compose

---

# Author

Email RAG Agentic System

Agentic AI Assignment Submission
=======
# Email_Rag_Agentic_System
 
