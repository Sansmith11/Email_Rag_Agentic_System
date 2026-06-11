import json
import pandas as pd
from email import message_from_string


CSV_PATH = r"C:\Users\hhr21\Downloads\emails.csv"
OUTPUT_PATH = "data/processed/emails.json"


def extract_body(msg):
    try:
        if msg.is_multipart():
            parts = []

            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)

                    if payload:
                        parts.append(
                            payload.decode(errors="ignore")
                        )

            return "\n".join(parts)

        payload = msg.get_payload(decode=True)

        if payload:
            return payload.decode(errors="ignore")

        return str(msg.get_payload())

    except Exception:
        return ""


def parse_email(raw_email, idx):

    msg = message_from_string(raw_email)

    return {
        "message_id": msg.get("Message-ID", f"msg_{idx}"),
        "date": msg.get("Date", ""),
        "from": msg.get("From", ""),
        "to": msg.get("To", ""),
        "subject": msg.get("Subject", ""),
        "body": extract_body(msg)
    }


df = pd.read_csv(CSV_PATH)

emails = []

for idx, row in df.head(500).iterrows():

    parsed = parse_email(
        row["message"],
        idx
    )

    emails.append(parsed)

with open(
    OUTPUT_PATH,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        emails,
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"Saved {len(emails)} emails")