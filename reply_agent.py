import imaplib
import email
import smtplib
import os
import time
from email.message import EmailMessage
from email.header import decode_header
import google.generativeai as genai

# Get environment variables
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not all([SMTP_USER, SMTP_PASSWORD, GEMINI_API_KEY]):
    print("Error: Missing environment variables for reply agent.")
    exit(1)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
# We can use gemini-1.5-flash for fast and cheap responses
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction="You are a friendly, encouraging English teacher. A student is replying to a daily English email challenge. Correct their grammar if needed, answer their question, and keep the conversation going in 1 or 2 short paragraphs. Always respond in English only.")

def clean_email_body(body):
    # Very basic cleanup to avoid processing the whole quoted history
    lines = body.split('\\n')
    cleaned = []
    for line in lines:
        # Stop if we hit a quoted reply block
        if line.startswith('>') or 'On ' in line and 'wrote:' in line:
            break
        cleaned.append(line)
    return '\\n'.join(cleaned).strip()

def process_inbox():
    # Connect to IMAP
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(SMTP_USER, SMTP_PASSWORD)
    mail.select('inbox')

    # Search for unread emails that are replies to the English Pill
    status, messages = mail.search(None, '(UNSEEN SUBJECT "Re: 💊 Your English Pill")')
    
    if status != 'OK' or not messages[0]:
        print("No new replies to process.")
        mail.close()
        mail.logout()
        return

    email_ids = messages[0].split()
    print(f"Found {len(email_ids)} unread replies.")

    for e_id in email_ids:
        res, msg_data = mail.fetch(e_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')
                
                sender = msg.get("From")
                print(f"Processing email from {sender} - Subject: {subject}")

                # Extract Body
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            try:
                                body = part.get_payload(decode=True).decode()
                                break
                            except:
                                pass
                else:
                    body = msg.get_payload(decode=True).decode()

                clean_body = clean_email_body(body)
                if not clean_body:
                    print("Could not extract body or body was empty.")
                    # Mark as read anyway
                    mail.store(e_id, '+FLAGS', '\\Seen')
                    continue
                
                print(f"Student wrote: {clean_body}")

                # Call Gemini API
                try:
                    response = model.generate_content(f"The student wrote: '{clean_body}'. Please reply to them.")
                    ai_reply = response.text
                except Exception as e:
                    print(f"Gemini API Error: {e}")
                    continue

                # Send Reply via SMTP
                reply_msg = EmailMessage()
                reply_msg['Subject'] = subject  # Keep the same Re: subject
                reply_msg['From'] = SMTP_USER
                reply_msg['To'] = sender
                reply_msg.set_content(ai_reply)

                try:
                    with smtplib.SMTP('smtp.gmail.com', 587) as server:
                        server.starttls()
                        server.login(SMTP_USER, SMTP_PASSWORD)
                        server.send_message(reply_msg)
                    print("AI Reply sent successfully.")
                    
                    # Mark as read only if reply was successful
                    mail.store(e_id, '+FLAGS', '\\Seen')
                except Exception as e:
                    print(f"Error sending reply: {e}")
                    
    mail.close()
    mail.logout()

if __name__ == '__main__':
    process_inbox()
