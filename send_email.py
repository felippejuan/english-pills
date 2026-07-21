import json
import os
import smtplib
import datetime
from email.message import EmailMessage

# Get environment variables
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', SMTP_USER)

if not SMTP_USER or not SMTP_PASSWORD:
    print("Error: Email credentials not found.")
    exit(1)

start_date = datetime.date(2026, 7, 21)
today = datetime.date.today()
delta_days = (today - start_date).days
current_day = ((delta_days) % 15) + 1

print(f"Executing Fluency Coach for Day {current_day}")

with open('docs/database.json', 'r', encoding='utf-8') as f:
    database = json.load(f)

today_data = next((item for item in database if item["day"] == current_day), None)
if not today_data:
    print("Error: Day data not found!")
    exit(1)

curiosity_html = today_data['curiosity_text'].replace('\\n', '<br><br>')

# Build HTML (Apple-style Elegant Off-White, safe for Gmail)
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
        margin: 0; 
        padding: 0; 
    }}
    .container {{ 
        background: #ffffff; 
        border-radius: 24px; 
        padding: 45px; 
        max-width: 600px; 
        margin: 0 auto; 
        box-shadow: 0 10px 40px rgba(0,0,0,0.08); 
    }}
    .pill-badge {{ 
        display: inline-block; 
        background: #000000; 
        color: white; 
        padding: 6px 16px; 
        border-radius: 20px; 
        font-size: 13px; 
        font-weight: 600; 
        text-transform: uppercase; 
        letter-spacing: 1px; 
        margin-bottom: 25px; 
    }}
    h1 {{ color: #1d1d1f; font-size: 32px; font-weight: 700; margin: 0 0 10px 0; letter-spacing: -0.5px; }}
    h2 {{ color: #1d1d1f; font-size: 22px; font-weight: 600; margin-top: 40px; margin-bottom: 15px; letter-spacing: -0.3px; }}
    p {{ font-size: 17px; color: #515154; margin-bottom: 16px; line-height: 1.6; }}
    
    .grammar-box {{ 
        background: #fbfbfd; 
        border: 1px solid #d2d2d7; 
        border-radius: 16px; 
        padding: 24px; 
        margin-top: 20px; 
    }}
    .grammar-box p {{ margin: 0; color: #1d1d1f; font-size: 16px; }}
    
    .yt-card {{ 
        display: block; 
        text-decoration: none; 
        border-radius: 16px; 
        overflow: hidden; 
        margin-top: 30px; 
        border: 1px solid #d2d2d7; 
    }}
    .yt-img {{ width: 100%; display: block; border-bottom: 1px solid #d2d2d7; }}
    .yt-info {{ padding: 15px; background: #ffffff; text-align: left; }}
    .yt-title {{ color: #1d1d1f; font-weight: 600; font-size: 16px; margin: 0; }}
    .yt-subtitle {{ color: #86868b; font-size: 14px; margin: 5px 0 0 0; }}

    .cta-container {{ text-align: center; margin-top: 50px; padding-top: 40px; border-top: 1px solid #e5e5ea; }}
    .btn {{ 
        display: inline-block; 
        background: #0071e3; 
        color: white; 
        text-decoration: none; 
        padding: 16px 32px; 
        border-radius: 30px; 
        font-weight: 600; 
        font-size: 18px; 
    }}
    .cta-hint {{ font-size: 14px; color: #86868b; margin-top: 15px; }}
    .footer {{ margin-top: 40px; font-size: 13px; color: #86868b; text-align: center; }}
</style>
</head>
<body style="background-color: #f5f5f7;">
    <!-- Wrapper div with inline background to force Gmail to show the off-white color -->
    <div style="background-color: #f5f5f7; width: 100%; padding: 40px 0;">
        <div class="container">
            <div class="pill-badge">Day {current_day}</div>
            <h1>{today_data['topic']}</h1>
            
            <h2>{today_data['curiosity_title']}</h2>
            <div class="curiosity-box">
                <p>{curiosity_html}</p>
            </div>

            <h2>💡 Grammar Focus</h2>
            <div class="grammar-box">
                <p>{today_data['grammar_tip']}</p>
            </div>
"""

if 'youtube_video' in today_data and 'youtube_thumbnail' in today_data:
    # Use the actual video title if provided in the DB
    yt_title = today_data.get('youtube_title', '▶️ Watch Video')
    html_content += f"""
            <a href="{today_data['youtube_video']}" class="yt-card" target="_blank">
                <img src="{today_data['youtube_thumbnail']}" alt="YouTube Video" class="yt-img">
                <div class="yt-info">
                    <p class="yt-title">{yt_title}</p>
                    <p class="yt-subtitle">Immerse yourself in today's topic (Under 10 mins)</p>
                </div>
            </a>
    """

html_content += f"""
            <div class="cta-container">
                <h2 style="margin-top: 0; margin-bottom: 20px;">Unlock Your Fluency</h2>
                <a href="https://felippejuan.github.io/english-pills/?day={current_day}" class="btn">Open Fluency Coach</a>
                <p class="cta-hint">Calibrate your vocabulary and train your pronunciation.</p>
            </div>

            <div class="footer">
                <p>Designed for you. Powered by Gemini AI.</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Send Email
msg = EmailMessage()
msg['Subject'] = f"🎓 Your Fluency Coach - Day {current_day}"
msg['From'] = SMTP_USER
msg['To'] = RECIPIENT_EMAIL
msg.set_content("Please enable HTML to view this email.")
msg.add_alternative(html_content, subtype='html')

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
    exit(1)
