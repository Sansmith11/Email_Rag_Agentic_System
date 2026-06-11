import os


def load_attachments():

    attachments = []

    folder = "data/attachments"

    if not os.path.exists(folder):
        return attachments

    for filename in os.listdir(folder):

        path = os.path.join(
            folder,
            filename
        )

        if not os.path.isfile(path):
            continue

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        attachments.append(
            {
                "filename": filename,
                "text": text
            }
        )

    return attachments