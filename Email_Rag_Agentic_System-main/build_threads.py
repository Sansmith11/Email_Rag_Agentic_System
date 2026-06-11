import json
from collections import defaultdict

INPUT_FILE = "data/processed/emails.json"
OUTPUT_FILE = "data/processed/threaded_emails.json"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    emails = json.load(f)

subject_groups = defaultdict(list)

for email in emails:

    subject = email.get("subject", "").strip()

    if not subject:
        continue

    if subject.lower() == "re:":
        continue

    subject_groups[subject].append(email)

threaded_emails = []

thread_counter = 1

for subject, messages in subject_groups.items():

    if len(messages) < 2:
        continue

    thread_id = f"T-{thread_counter:04d}"

    for msg in messages:

        msg["thread_id"] = thread_id

        threaded_emails.append(msg)

    thread_counter += 1

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        threaded_emails,
        f,
        indent=2,
        ensure_ascii=False
    )

print(
    f"Threads Created: {thread_counter-1}"
)

print(
    f"Messages Saved: {len(threaded_emails)}"
)