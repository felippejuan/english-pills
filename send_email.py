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

# Generate Audio for Target Phrase
audio_path = "audio.mp3"
tts = gTTS(text=today_data["target_phrase"], lang='en', tld='co.uk', slow=False) # British Accent
tts.save(audio_path)

# Build Pronunciation Tips HTML
pronunciation_html = ""
if "pronunciation_tips" in today_data:
    for word, tip in today_data["pronunciation_tips"].items():
        pronunciation_html += f"<li><strong>{word}</strong> <span style='color: #86868b; font-size: 13px;'>— pronounce it like <em>{tip}</em></span></li>"

# Build HTML (Apple-style minimalist)
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f5f5f7; color: #1d1d1f; margin: 0; padding: 40px 20px; line-height: 1.5; }}
    .container {{ background: #ffffff; border-radius: 18px; padding: 40px; max-width: 640px; margin: 0 auto; box-shadow: 0 4px 24px rgba(0,0,0,0.04); }}
    .pill-badge {{ display: inline-block; background: #0071e3; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 20px; }}
    h1 {{ color: #1d1d1f; font-size: 28px; font-weight: 700; margin: 0 0 10px 0; letter-spacing: -0.5px; }}
    h2 {{ color: #1d1d1f; font-size: 20px; font-weight: 600; margin-top: 35px; margin-bottom: 15px; letter-spacing: -0.3px; }}
    p {{ font-size: 16px; color: #515154; margin-bottom: 16px; line-height: 1.6; }}
    .curiosity-box {{ padding: 0; margin-bottom: 30px; }}
    .grammar-box {{ background: #fbfbfd; border: 1px solid #d2d2d7; border-radius: 12px; padding: 20px; margin-top: 20px; }}
    .grammar-box p {{ margin: 0; color: #1d1d1f; font-size: 15px; }}
    .pronunciation-list {{ list-style: none; padding: 0; margin: 0; }}
    .pronunciation-list li {{ padding: 8px 0; border-bottom: 1px solid #e5e5ea; font-size: 15px; }}
    .pronunciation-list li:last-child {{ border-bottom: none; }}
    
    .video-card {{ display: block; text-decoration: none; background: #fbfbfd; border-radius: 12px; padding: 20px; text-align: center; margin-top: 30px; border: 1px solid #d2d2d7; transition: all 0.3s ease; }}
    .video-card:hover {{ background: #f5f5f7; }}
    .video-icon {{ font-size: 24px; margin-bottom: 10px; }}
    .video-title {{ color: #1d1d1f; font-weight: 600; font-size: 16px; margin: 0; }}
    .video-subtitle {{ color: #86868b; font-size: 13px; margin: 5px 0 0 0; }}

    .cta-container {{ text-align: center; margin-top: 45px; padding-top: 35px; border-top: 1px solid #e5e5ea; }}
    .btn {{ display: inline-block; background: #0071e3; color: white; text-decoration: none; padding: 14px 28px; border-radius: 25px; font-weight: 600; font-size: 16px; transition: background 0.3s ease; }}
    .btn:hover {{ background: #0077ed; }}
    .cta-hint {{ font-size: 13px; color: #86868b; margin-top: 15px; }}
    
    .footer {{ margin-top: 40px; font-size: 12px; color: #86868b; text-align: center; }}
</style>
</head>
<body>
    <div class="container">
        <div class="pill-badge">Day {current_day}</div>
        <h1>{today_data['topic']}</h1>
        
        <h2>{today_data['curiosity_title']}</h2>
        <div class="curiosity-box">
            <p>{today_data['curiosity_text'].replace(chr(10), '<br>')}</p>
        </div>

        <h2>🗣️ Pronunciation Tips</h2>
        <p style="font-size: 14px; color: #86868b; margin-top: -10px;">Listen to the attached audio, and check out these tips for the hard words:</p>
        <ul class="pronunciation-list">
            {pronunciation_html}
        </ul>

        <h2>💡 Grammar Focus</h2>
        <div class="grammar-box">
            <p>{today_data['grammar_tip']}</p>
        </div>
"""

if 'youtube_video' in today_data:
    html_content += f"""
        <a href="{today_data['youtube_video']}" class="video-card" target="_blank">
            <div class="video-icon">▶️</div>
            <p class="video-title">Watch the Complementary Video</p>
            <p class="video-subtitle">Boost your listening skills (under 10 mins)</p>
        </a>
    """

html_content += f"""
        <div class="cta-container">
            <h2 style="margin-top: 0; margin-bottom: 20px;">Ready for your Interactive Workout?</h2>
            <a href="https://felippejuan.github.io/english-pills/?day={current_day}" class="btn">Open Web App</a>
            <p class="cta-hint">The Web App will sync with your cloud progress, generate AI exercises,<br>and evaluate your pronunciation.</p>
        </div>

        <div class="footer">
            <p>Designed for you. Powered by Gemini AI & GitHub Actions.</p>
        </div>
    </div>
</body>
</html>
"""

# Send Email
msg = EmailMessage()
msg['Subject'] = f"💊 Your English Pill - Day {current_day}"
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
