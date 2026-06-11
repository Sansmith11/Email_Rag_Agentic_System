import json
from collections import defaultdict

INPUT_FILE = "data/processed/emails.json"

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

valid_threads = {
    subject: msgs
    for subject, msgs in subject_groups.items()
    if len(msgs) >= 2
}

print("Valid Threads:", len(valid_threads))

for subject, msgs in list(valid_threads.items())[:20]:
    print(f"{subject} --> {len(msgs)} messages")