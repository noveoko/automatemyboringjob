import sqlite3
import mailbox

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS emails (
                        id INTEGER PRIMARY KEY,
                        sender TEXT,
                        receiver TEXT,
                        subject TEXT,
                        body TEXT)''')
    conn.commit()

def insert_email(conn, sender, receiver, subject, body):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO emails (sender, receiver, subject, body)
                      VALUES (?, ?, ?, ?)''', (sender, receiver, subject, body))
    conn.commit()

def mbox_to_sqlite(mbox_file, db_file):
    conn = sqlite3.connect(db_file)
    create_table(conn)
    mbox = mailbox.mbox(mbox_file)
    for message in mbox:
        sender = message['From']
        receiver = message['To']
        subject = message['Subject']
        body = ""
        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload()
        else:
            body = message.get_payload()
        insert_email(conn, sender, receiver, subject, body)
    conn.close()

# Usage example
mbox_file = "example.mbox"  # Replace with your MBOX file name
db_file = "emails.db"       # Name of the SQLite database file
mbox_to_sqlite(mbox_file, db_file)
