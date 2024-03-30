import sqlite3
import mailbox
import email.utils

# Function to parse Mbox file and insert data into SQLite database
def parse_mbox(mbox_file, conn):
    c = conn.cursor()

    mbox = mailbox.mbox(mbox_file)
    for message in mbox:
        subject = message['subject']
        sender = email.utils.parseaddr(message['from'])[1]
        receiver = email.utils.parseaddr(message['to'])[1]
        date = message['date']
        body = ""
        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" not in content_disposition:
                    body += part.get_payload(decode=True).decode("utf-8", errors="ignore") + "\n"
        else:
            body = message.get_payload(decode=True).decode("utf-8", errors="ignore")

        c.execute('''INSERT INTO emails (subject, sender, receiver, date, body) VALUES (?, ?, ?, ?, ?)''',
                  (subject, sender, receiver, date, body))

    conn.commit()

# Function to merge new Mbox file with existing SQLite database
def merge_mbox_with_database(mbox_file, db_file):
    conn = sqlite3.connect(db_file)
    parse_mbox(mbox_file, conn)
    conn.close()
    print("Merge completed successfully.")

if __name__ == "__main__":
    mbox_file = "path_to_new_mbox_file.mbox"
    db_file = "gmail_data.db"
    merge_mbox_with_database(mbox_file, db_file)
