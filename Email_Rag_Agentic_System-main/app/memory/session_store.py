import uuid


class SessionStore:

    def __init__(self):

        self.sessions = {}

    def start_session(
        self,
        thread_id
    ):

        session_id = str(
            uuid.uuid4()
        )

        self.sessions[
            session_id
        ] = {

            "thread_id": thread_id,

            "turn_history": [],

            "entity_register": {
                "people": [],
                "dates": [],
                "amounts": [],
                "filenames": [],
                "message_refs": []
            }
        }

        return session_id

    def get_session(
        self,
        session_id
    ):

        return self.sessions.get(
            session_id
        )

    def add_turn(
        self,
        session_id,
        user_text,
        assistant_text
    ):

        if session_id not in self.sessions:
            return

        self.sessions[
            session_id
        ]["turn_history"].append(
            {
                "user": user_text,
                "assistant": assistant_text
            }
        )

    def switch_thread(
        self,
        session_id,
        thread_id
    ):

        if session_id not in self.sessions:
            return False

        self.sessions[
            session_id
        ]["thread_id"] = thread_id

        return True

    def reset_session(
        self,
        session_id
    ):

        if session_id not in self.sessions:
            return False

        self.sessions[
            session_id
        ]["turn_history"] = []

        self.sessions[
            session_id
        ]["entity_register"] = {
            "people": [],
            "dates": [],
            "amounts": [],
            "filenames": [],
            "message_refs": []
        }

        return True

