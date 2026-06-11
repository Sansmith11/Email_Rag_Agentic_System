import json
import os
import uuid
from datetime import datetime


LOG_DIR = "runs"

os.makedirs(
    LOG_DIR,
    exist_ok=True
)


def create_trace_id():

    return str(
        uuid.uuid4()
    )


def log_agent_event(data):

    log_file = os.path.join(
        LOG_DIR,
        "trace.jsonl"
    )

    data["timestamp"] = (
        datetime.now().isoformat()
    )

    with open(
        log_file,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            json.dumps(data)
            + "\n"
        )

def read_trace_events():

    log_file = os.path.join(
        LOG_DIR,
        "trace.jsonl"
    )

    if not os.path.exists(
        log_file
    ):
        return []

    with open(
        log_file,
        "r",
        encoding="utf-8"
    ) as f:

        lines = f.readlines()

    events = []

    for line in lines[-20:]:

        try:

            events.append(
                json.loads(line)
            )

        except:

            pass

    return events