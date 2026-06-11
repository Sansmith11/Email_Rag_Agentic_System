from app.memory.session_store import SessionStore


store = SessionStore()

session_id = store.start_session(
    "T-0002"
)

print(
    "Session ID:",
    session_id
)

print(
    store.get_session(
        session_id
    )
)