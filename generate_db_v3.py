import json
import os
import urllib.request

# Init JSON Blob
blob_id = "019f8682-7a50-78b6-9391-f6a94c05601b"
url = f"https://jsonblob.com/api/jsonBlob/{blob_id}"
req = urllib.request.Request(url, data=b'{"progress": {}, "schedule": {}}', headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, method='PUT')
try:
    urllib.request.urlopen(req)
    print("JSONBlob initialized.")
except Exception as e:
    print("Error initializing JSONBlob:", e)


# Generate Database
days = [
    {
        "day": 1,
        "topic": "Present Perfect & British Corporate Culture",
        "curiosity_title": "The Evolution of the BBC",
        "curiosity_text": "The British Broadcasting Corporation (BBC), affectionately known as 'The Auntie', was founded in 1922 and operates under a Royal Charter. Unlike many global broadcasters, the BBC is primarily funded by an annual television licence fee paid by British households. This unique funding model allows it to remain largely free of commercial advertising and political influence, striving to provide impartial news and high-quality programming to the public.\\n\\nOver the decades, the BBC has pioneered numerous technological advancements in broadcasting, from the world's first regular high-definition television service in 1936 to the launch of the iPlayer in 2007. It remains a cornerstone of British culture, showcasing everything from hard-hitting documentaries to beloved dramas like Doctor Who.",
        "grammar_tip": "In British English, the Present Perfect is frequently used to give recent news. For example, 'I have just finished the report' instead of the American 'I just finished the report'.",
        "pronunciation_tips": {
            "Broadcasting": "bród-cás-tin",
            "Impartial": "im-pár-shoul",
            "Showcasing": "shou-cêi-sin"
        },
        "youtube_video": "https://www.youtube.com/watch?v=F0Z715w0V0c",
        "target_phrase": "The BBC has always strived to provide impartial news to the public."
    },
    {
        "day": 2,
        "topic": "Conditionals & British History",
        "curiosity_title": "The Mystery of Stonehenge",
        "curiosity_text": "Stonehenge, located on Salisbury Plain in Wiltshire, is one of the most famous prehistoric monuments in the world. Constructed in several stages between 3000 BC and 2000 BC, the iconic stone circle continues to baffle historians and archaeologists. If you were to transport the massive sarsen stones today, you would need heavy machinery, yet our ancestors managed to move them from quarries up to 20 miles away using only ropes, wooden sledges, and sheer human strength.\\n\\nThe true purpose of Stonehenge remains a subject of intense debate. While some believe it was an ancient burial ground, others argue it was a sophisticated astronomical observatory aligned with the solstices. If they hadn't aligned the stones so perfectly with the sunrise on the summer solstice, we wouldn't have such strong evidence of their astronomical knowledge.",
        "grammar_tip": "Second Conditional: Use 'If + Past Simple, would + Verb' to talk about hypothetical situations in the present or future (e.g., 'If I lived in London, I would visit the British Museum').",
        "pronunciation_tips": {
            "Prehistoric": "pri-his-tó-rik",
            "Baffle": "bé-foul",
            "Sledges": "slé-djis"
        },
        "youtube_video": "https://www.youtube.com/watch?v=-6exTXhqQLE",
        "target_phrase": "If I were to visit England, I would definitely go to Stonehenge."
    }
]

# Expand to 15 days for the loop
for i in range(3, 16):
    day_copy = days[(i-1) % 2].copy()
    day_copy["day"] = i
    days.append(day_copy)

with open('C:\\\\Users\\\\felip\\\\.gemini\\\\antigravity\\\\scratch\\\\english-pills\\\\docs\\\\database.json', 'w', encoding='utf-8') as f:
    json.dump(days, f, indent=4, ensure_ascii=False)
    
print("Database V3 generated successfully.")
