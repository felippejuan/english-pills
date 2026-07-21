import json

days = [
    {
        "day": 1,
        "topic": "The Secret Behind the Michelin Guide",
        "curiosity_title": "Tires and Fine Dining",
        "curiosity_text": "Have you ever wondered why a tire company gives out stars to the best restaurants in the world? It <span class='highlightable' data-id='sounds_random'>sounds pretty random</span>, right? Back in 1900, the Michelin brothers wanted people to drive their cars more often so they would buy more tires. But there was a problem: people didn't really have many places to drive to.\\n\\nSo, they <span class='highlightable' data-id='came_up_with'>came up with</span> a clever idea. They created a free guide book filled with maps, tire repair tips, and most importantly, a list of great hotels and restaurants. The idea was simple: if people want to try out a nice restaurant in another city, they will drive there, wear out their tires, and eventually need to buy new ones from Michelin. What started as a sneaky marketing trick <span class='highlightable' data-id='turned_into'>turned into</span> the most respected food guide on the planet.",
        "grammar_tip": "Expression: 'Come up with' means to think of an idea or a plan. Example: 'They came up with a clever idea to sell more tires.'",
        "youtube_video": "https://www.youtube.com/watch?v=17dmlfYRqz0",
        "youtube_title": "▶️ Watch: The Michelin Guide Story",
        "tooltips": {
            "sounds_random": {
                "word": "sounds pretty random",
                "phonetic_br": "sáunds prí-ti rân-dom",
                "definition": "Seems unusual, unexpected, or lacking a clear logical connection.",
                "examples": [
                    "I know it sounds pretty random, but hear me out.",
                    "The decision sounds pretty random to me.",
                    "It sounds pretty random that a tire company rates food."
                ]
            },
            "came_up_with": {
                "word": "came up with",
                "phonetic_br": "kêim ãp uíf",
                "definition": "To think of an idea, plan, or solution.",
                "examples": [
                    "She came up with a great marketing strategy.",
                    "We need to come up with a backup plan.",
                    "They came up with a clever idea."
                ]
            },
            "turned_into": {
                "word": "turned into",
                "phonetic_br": "tãrnd in-tu",
                "definition": "To become something different; transform.",
                "examples": [
                    "A small project turned into a global success.",
                    "The meeting turned into a heated argument.",
                    "The trick turned into the most respected guide."
                ]
            }
        },
        "exercises": [
            {
                "word": "sounds pretty random",
                "difficulty": "easy",
                "sentence": "I know it sounds pretty random, but it actually works."
            },
            {
                "word": "came up with",
                "difficulty": "medium",
                "sentence": "The marketing team came up with a brilliant idea for the new campaign."
            },
            {
                "word": "turned into",
                "difficulty": "hard",
                "sentence": "What started as a small hobby turned into a million-dollar business."
            }
        ]
    },
    {
        "day": 2,
        "topic": "How the Weekend was Invented",
        "curiosity_title": "Henry Ford's Masterplan",
        "curiosity_text": "Most of us <span class='highlightable' data-id='look_forward_to'>look forward to</span> Saturday and Sunday, but the 'two-day weekend' wasn't always a normal thing. For a long time, people worked six days a week and only had Sunday off for rest. So, who changed this?\\n\\nIn 1926, Henry Ford, the famous car maker, decided to give his factory workers both Saturday and Sunday off, without cutting their pay. He didn't just do this because he was a nice boss. He <span class='highlightable' data-id='figured_out'>figured out</span> that if people had more free time on the weekends, they would have a reason to buy a car and go on trips with their families. By giving them extra time off, he actually created more customers for his own business. Soon after, other companies <span class='highlightable' data-id='followed_his_lead'>followed his lead</span>, and the modern weekend was born.",
        "grammar_tip": "Phrasal Verb: 'Look forward to' means to feel happy and excited about something that is going to happen. Example: 'I always look forward to the weekend.'",
        "youtube_video": "https://www.youtube.com/watch?v=9xtrn1fZYJk",
        "youtube_title": "▶️ Watch: Why we have weekends",
        "tooltips": {
            "look_forward_to": {
                "word": "look forward to",
                "phonetic_br": "luk fór-uard tu",
                "definition": "To feel pleased and excited about something that is going to happen.",
                "examples": [
                    "I look forward to our meeting tomorrow.",
                    "We look forward to hearing from you soon.",
                    "Most of us look forward to the weekend."
                ]
            },
            "figured_out": {
                "word": "figured out",
                "phonetic_br": "fí-guerd áut",
                "definition": "To understand or solve something after thinking about it.",
                "examples": [
                    "She finally figured out the math problem.",
                    "We figured out a way to reduce costs.",
                    "He figured out that free time creates customers."
                ]
            },
            "followed_his_lead": {
                "word": "followed his lead",
                "phonetic_br": "fó-loud ris líd",
                "definition": "To do the same thing that someone else has just done.",
                "examples": [
                    "The manager left early, and the team followed his lead.",
                    "When Apple removed the headphone jack, others followed their lead.",
                    "Other companies followed his lead to create the weekend."
                ]
            }
        },
        "exercises": [
            {
                "word": "look forward to",
                "difficulty": "medium",
                "sentence": "I really look forward to our summer vacation every year."
            },
            {
                "word": "figured out",
                "difficulty": "easy",
                "sentence": "It took me a while, but I finally figured out how to use the software."
            },
            {
                "word": "followed his lead",
                "difficulty": "hard",
                "sentence": "After the CEO decided to allow remote work, many other companies followed his lead."
            }
        ]
    }
]

# Expand to 15 days by repeating for the mock DB
for i in range(3, 16):
    day_copy = days[(i-1) % 2].copy()
    day_copy["day"] = i
    days.append(day_copy)

with open('C:\\\\Users\\\\felip\\\\.gemini\\\\antigravity\\\\scratch\\\\english-pills\\\\docs\\\\database.json', 'w', encoding='utf-8') as f:
    json.dump(days, f, indent=4, ensure_ascii=False)
    
print("Database V7 (Pre-Generated AI Content) generated successfully.")
