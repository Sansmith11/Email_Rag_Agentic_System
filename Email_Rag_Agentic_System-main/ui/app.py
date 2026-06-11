import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Email RAG Agentic AI")

thread_id = st.text_input(
    "Thread ID",
    "T-0002"
)

if "session_id" not in st.session_state:
    st.session_state.session_id = None

if st.button("Start Session"):

    response = requests.post(
        f"{API_URL}/start_session",
        json={
            "thread_id": thread_id
        }
    )

    data = response.json()

    st.session_state.session_id = data[
        "session_id"
    ]

    st.success(
        f"Session: {st.session_state.session_id}"
    )

question = st.text_input(
    "Question"
)

if st.button("Ask"):

    if not st.session_state.session_id:

        st.error(
            "Start session first"
        )

    else:

        response = requests.post(
            f"{API_URL}/ask",
            json={
                "session_id":
                st.session_state.session_id,

                "text":
                question
            }
        )

        result = response.json()

        st.subheader("Answer")

        st.write(
            result["answer"]
        )

        st.subheader("Rewrite")

        st.write(
            result["rewrite"]
        )

        st.subheader("Citations")

        st.json(
            result["citations"]
        )
        st.subheader("Entity Register")

        st.json(
            result["entity_register"]
        )

        st.subheader("Grounding Score")

        st.write(
            result["grounding_score"]
        )

        st.subheader("Retrieved Chunks")

        st.json(
            result["retrieved"]
        )