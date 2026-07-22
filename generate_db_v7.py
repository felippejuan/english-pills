import json

days = [
    {
        "day": 1,
        "topic": "The Secret Behind the Michelin Guide",
        "curiosity_title": "Tires and Fine Dining",
        "curiosity_text": "Have you ever pondered why a ubiquitous tire manufacturer bestows prestigious stars upon the world's finest culinary establishments? At first glance, it seems like a rather baffling juxtaposition. However, this seemingly bizarre connection actually stemmed from a brilliantly pragmatic strategy in 1900. The Michelin brothers sought to entice the sparse population of automobile owners to hit the road more frequently, thereby wearing out their tires and driving up sales.\\n\\nTo achieve this, they meticulously compiled a comprehensive guidebook featuring maps, mechanic listings, and, crucially, a curated selection of lodging and dining venues. The underlying premise was remarkably astute: by compelling motorists to embark on gastronomic journeys to far-flung towns, tire degradation was inevitable. What initially launched as a cunning promotional gambit eventually evolved into the most formidable and revered culinary authority on the globe.",
        "grammar_tip": "Expression: 'Stemmed from' means to originate or be caused by something. Example: 'Her success stemmed from sheer hard work.'",
        "youtube_video": "https://www.youtube.com/watch?v=17dmlfYRqz0",
        "youtube_title": "▶️ Watch: The Michelin Guide Story",
        "tooltips": {
            "ubiquitous": {
                "word": "ubiquitous",
                "phonetic_br": "yu-bí-kui-tâs",
                "definition": "Present, appearing, or found everywhere.",
                "examples": [
                    "Smartphones have become ubiquitous in modern society.",
                    "The company's logo is ubiquitous across the city."
                ]
            },
            "stemmed from": {
                "word": "stemmed from",
                "phonetic_br": "stêmd fróm",
                "definition": "To be caused by something or originate from a specific source.",
                "examples": [
                    "Their financial troubles stemmed from poor management.",
                    "The new policy stemmed from customer feedback."
                ]
            },
            "astute": {
                "word": "astute",
                "phonetic_br": "âs-tiút",
                "definition": "Having or showing an ability to accurately assess situations and turn them into an advantage.",
                "examples": [
                    "It was an astute business decision that saved the company.",
                    "She is a very astute observer of market trends."
                ]
            }
        },
        "exercises": [
            {
                "word": "ubiquitous",
                "difficulty": "medium",
                "sentence": "Coffee shops are ubiquitous in this neighborhood; there is one on every corner."
            },
            {
                "word": "stemmed from",
                "difficulty": "hard",
                "sentence": "The delay in the project stemmed from a lack of communication between the teams."
            },
            {
                "word": "astute",
                "difficulty": "easy",
                "sentence": "The CEO made an astute observation that completely changed our marketing strategy."
            }
        ]
    },
    {
        "day": 2,
        "topic": "How the Weekend was Invented",
        "curiosity_title": "Henry Ford's Masterplan",
        "curiosity_text": "While we enthusiastically anticipate the sanctuary of a two-day weekend, this paradigm shift in labor was not always the norm. For decades, the industrial workforce was tethered to grueling six-day schedules, with merely a single day afforded for respite. The catalyst for this profound societal transformation was none other than Henry Ford.\\n\\nIn 1926, the pioneering industrialist unilaterally decreed that his workforce would be granted both Saturday and Sunday off, remarkably without diminishing their compensation. This was not merely an act of corporate benevolence. Ford astutely deduced that providing his laborers with ample leisure time would inadvertently foster consumerism. By affording them the bandwidth to pursue recreational travel, he effectively catalyzed the demand for his own automobiles. This bold maneuver triggered a ripple effect across the manufacturing landscape, prompting rival conglomerates to follow suit and cementing the modern weekend into existence.",
        "grammar_tip": "Vocabulary: A 'paradigm shift' is a fundamental change in approach or underlying assumptions. Example: 'The invention of the internet caused a paradigm shift in how we communicate.'",
        "youtube_video": "https://www.youtube.com/watch?v=9xtrn1fZYJk",
        "youtube_title": "▶️ Watch: Why we have weekends",
        "tooltips": {
            "paradigm shift": {
                "word": "paradigm shift",
                "phonetic_br": "pé-râ-dáim shift",
                "definition": "A fundamental and major change in the way something is done or thought about.",
                "examples": [
                    "The shift to remote work caused a paradigm shift in corporate culture.",
                    "We need a paradigm shift to solve this complex issue."
                ]
            },
            "catalyst": {
                "word": "catalyst",
                "phonetic_br": "kê-tâ-list",
                "definition": "A person or thing that precipitates an event or causes significant change.",
                "examples": [
                    "The CEO's speech acted as a catalyst for the company's restructuring.",
                    "Technology has been a catalyst for rapid economic growth."
                ]
            },
            "follow suit": {
                "word": "follow suit",
                "phonetic_br": "fó-lou siút",
                "definition": "To conform to another's actions; to do the same thing that someone else has just done.",
                "examples": [
                    "When the leading bank raised interest rates, others quickly followed suit.",
                    "If you decide to leave early, I might follow suit."
                ]
            }
        },
        "exercises": [
            {
                "word": "paradigm shift",
                "difficulty": "hard",
                "sentence": "The introduction of artificial intelligence has created a major paradigm shift in the software industry."
            },
            {
                "word": "catalyst",
                "difficulty": "easy",
                "sentence": "The scandal was the catalyst that finally forced the government to change the law."
            },
            {
                "word": "follow suit",
                "difficulty": "medium",
                "sentence": "Once the largest competitor lowers their prices, the rest of the market will have to follow suit."
            }
        ]
    }
]

for i in range(3, 16):
    day_copy = days[(i-1) % 2].copy()
    day_copy["day"] = i
    days.append(day_copy)

with open('C:\\\\Users\\\\felip\\\\.gemini\\\\antigravity\\\\scratch\\\\english-pills\\\\docs\\\\database.json', 'w', encoding='utf-8') as f:
    json.dump(days, f, indent=4, ensure_ascii=False)
    
print("Database V7.2 (Advanced Vocabulary) generated successfully.")
