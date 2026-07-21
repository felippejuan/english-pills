import json
import os
import smtplib
import datetime
from email.message import EmailMessage
from gtts import gTTS

# Get environment variables
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', SMTP_USER)

if not SMTP_USER or not SMTP_PASSWORD:
    print("Error: Email credentials not found.")
    exit(1)

# Determine the "Current Day" based on start date
start_date = datetime.date(2026, 7, 21)
today = datetime.date.today()
delta_days = (today - start_date).days
current_day = ((delta_days) % 15) + 1

print(f"Executing English Pill for Day {current_day}")

# Read JSON
with open('docs/database.json', 'r', encoding='utf-8') as f:
    database = json.load(f)

today_data = next((item for item in database if item["day"] == current_day), None)
if not today_data:
    print("Error: Day data not found!")
    exit(1)

# Active Recall Data (7 days ago)
recall_day = current_day - 7
if recall_day < 1:
    recall_day = 15 + recall_day

recall_data = next((item for item in database if item["day"] == recall_day), None)

# Generate Audio
audio_path = "audio.mp3"
tts = gTTS(text=today_data["target_phrase"], lang='en', slow=False)
tts.save(audio_path)

# Build HTML
glossary_html = ""
if "vocabulary_glossary" in today_data:
    glossary_html = "<ul>"
    for word, meaning in today_data["vocabulary_glossary"].items():
        glossary_html += f"<li><strong>{word}:</strong> {meaning}</li>"
    glossary_html += "</ul>"

html_content = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; color: #333; margin: 0; padding: 20px; }}
    .container {{ background: #ffffff; border-radius: 12px; padding: 30px; max-width: 600px; margin: 0 auto; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #3b82f6; }}
    h1 {{ color: #1e293b; font-size: 24px; }}
    h2 {{ color: #3b82f6; font-size: 18px; margin-top: 25px; border-bottom: 2px solid #e2e8f0; padding-bottom: 5px; }}
    .highlight {{ background: #eff6ff; padding: 15px; border-left: 4px solid #3b82f6; border-radius: 4px; margin: 15px 0; line-height: 1.6; }}
    .cta-box {{ background: #fffbeb; padding: 15px; border-left: 4px solid #f59e0b; border-radius: 4px; margin: 15px 0; font-weight: bold; color: #b45309; }}
    .phrase-box {{ background: #1e293b; color: white; padding: 20px; text-align: center; border-radius: 8px; font-size: 20px; font-weight: bold; margin: 25px 0; }}
    .btn {{ display: inline-block; background: #3b82f6; color: white; text-decoration: none; padding: 12px 25px; border-radius: 50px; font-weight: bold; margin-top: 10px; }}
    .btn:hover {{ background: #2563eb; }}
    .footer {{ margin-top: 30px; font-size: 12px; color: #94a3b8; text-align: center; }}
</style>
</head>
<body>
    <div class="container">
        <h1>💊 English Pill - Day {current_day}</h1>
        <p><strong>Topic:</strong> {today_data['topic']}</p>
        
        <h2>🧠 Curiosity of the Day: {today_data['fact_title']}</h2>
        <div class="highlight">
            <p>{today_data['fact_text'].replace(chr(10), '<br>')}</p>
        </div>

        <h2>📖 Vocabulary Glossary</h2>
        <div class="highlight">
            {glossary_html}
        </div>

        <h2>💬 Phrasal Verb: {today_data['phrasal_verb']}</h2>
        <p><strong>Meaning:</strong> {today_data['phrasal_verb_meaning']}</p>
        <p><strong>Example:</strong> {today_data['phrasal_verb_example']}</p>

        <h2>💡 Grammar Tip</h2>
        <p>{today_data['grammar_tip']}</p>

        <div class="cta-box">
            <p>🎯 <strong>Action Required:</strong> {today_data.get('grammar_cta', 'Reply to this email using the grammar rule!')}</p>
            <p style="font-size: 12px; margin-top: 5px; color: #d97706;">(Just hit 'Reply', type your answer, and our AI Tutor will respond to you shortly!)</p>
        </div>

        <h2>🗣️ Target Phrase (Listen & Repeat)</h2>
        <p>Listen to the attached audio file and try to repeat the phrase below:</p>
        <div class="phrase-box">
            {today_data['target_phrase']}
        </div>

        <div style="text-align: center; margin-top: 30px;">
            <p>Ready to test your pronunciation?</p>
            <a href="https://felippejuan.github.io/english-pills/?day={current_day}" class="btn">Open Pronunciation App</a>
        </div>
"""

if recall_data:
    html_content += f"""
        <h2>⏳ Active Recall Challenge</h2>
        <p>Do you remember the Phrasal Verb we learned 7 days ago?</p>
        <div class="highlight">
            <p>What is the meaning of <strong>{recall_data['phrasal_verb']}</strong>?</p>
            <p style="font-size: 10px; color: transparent; text-shadow: 0 0 8px rgba(0,0,0,0.5);">Answer: {recall_data['phrasal_verb_meaning']} - Select this blurred text to reveal the answer.</p>
        </div>
    """

html_content += """
        <div class="footer">
            <p>Automated by your English Pills System.</p>
        </div>
    </div>
</body>
</html>
"""

# Send Email
msg = EmailMessage()
msg['Subject'] = f"Re: 💊 Your English Pill - Day {current_day}"
msg['From'] = SMTP_USER
msg['To'] = RECIPIENT_EMAIL
msg.set_content("Please enable HTML to view this email.")
msg.add_alternative(html_content, subtype='html')

with open(audio_path, 'rb') as f:
    audio_data = f.read()
msg.add_attachment(audio_data, maintype='audio', subtype='mpeg', filename=f'pronunciation_day_{current_day}.mp3')

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
    exit(1)
finally:
    if os.path.exists(audio_path):
        os.remove(audio_path)
