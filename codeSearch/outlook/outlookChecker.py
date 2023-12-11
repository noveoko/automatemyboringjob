```bash
pip install imaplib ftplib
```

Now, here's a basic script outline:

```python
import imaplib
import email
import os
import ftplib

# Email account credentials
username = 'your_email@example.com'
password = 'your_password'

# IMAP server settings (for Outlook)
imap_host = 'outlook.office365.com'
imap_port = 993

# FTP server details
ftp_host = 'ftp.yourserver.com'
ftp_username = 'ftp_user'
ftp_password = 'ftp_password'

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(imap_host, imap_port)
mail.login(username, password)
mail.select('inbox')

# Search for emails with attachments
type, data = mail.search(None, '(UNSEEN ATTACHMENT)')

# Process emails
for num in data[0].split():
    typ, msg_data = mail.fetch(num, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = part.get_filename()
                if filename:
                    filepath = os.path.join('/path/to/save/attachments', filename)
                    with open(filepath, 'wb') as file:
                        file.write(part.get_payload(decode=True))

                    # Upload to FTP
                    with ftplib.FTP(ftp_host, ftp_username, ftp_password) as ftp:
                        with open(filepath, 'rb') as file:
                            ftp.storbinary(f'STOR {filename}', file)

# Close the connection
mail.logout()
```

**Important Notes:**
1. Replace placeholders with your actual email and FTP credentials.
2. Modify the IMAP search criteria as per your requirements.
3. The script checks for unread emails with attachments. You may want to adjust this.
4. Make sure to handle exceptions and add error checking for a robust solution.
5. Use this script responsibly and ensure compliance with all relevant data protection laws.