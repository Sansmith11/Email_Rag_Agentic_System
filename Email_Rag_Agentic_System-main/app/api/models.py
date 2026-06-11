from pydantic import BaseModel


class StartSessionRequest(BaseModel):

    thread_id: str


class AskRequest(BaseModel):

    session_id: str

    text: str


class SwitchThreadRequest(BaseModel):

    session_id: str

    thread_id: str