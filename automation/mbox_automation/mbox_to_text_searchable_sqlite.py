import sqlite3
import mailbox
import email.utils

# Function to create SQLite database with full-text search capabilities
def create_database():
    conn = sqlite3.connect('gmail_data.db')
    c = conn.cursor()

    # Create table for emails
    c.execute('''CREATE TABLE IF NOT EXISTS emails
                 (id INTEGER PRIMARY KEY, subject TEXT, sender TEXT, receiver TEXT, date TEXT, body TEXT)''')

    # Create full-text search index
    c.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS emails_fts
                 USING FTS5(subject, sender, receiver, body, content='emails')''')

    conn.commit()
    conn.close()

# Function to parse Mbox file and insert data into SQLite database
def parse_mbox(mbox_file):
    conn = sqlite3.connect('gmail_data.db')
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
    conn.close()

if __name__ == "__main__":
    mbox_file = "path_to_your_mbox_file.mbox"
    create_database()
    parse_mbox(mbox_file)
    print("Conversion completed successfully.")
