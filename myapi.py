import google.generativeai as genai
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("AIzaSyBkfBTvcp2uyh8xcmhdRwKJupwycTJKwGs")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def get_sentiment(text):
    prompt = f"""
    You are an NLP model. Analyze the sentiment of the following text.
    Return ONLY JSON. No explanations.

    Text: "{text}"

    Format:
    {{
        "sentiment": "positive" or "negative" or "neutral"
    }}
    """

    response = model.generate_content(prompt)
    clean = response.text.strip()


    try:
        data = json.loads(clean)
        return data
    except:

        clean = clean.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)


def get_ner(text):
    prompt = f"""
    You are an NLP NER model. Extract ONLY named entities from the text.
    Return ONLY JSON. No extra text.

    Text: "{text}"

    JSON Format:
    {{
        "entities": [
            {{"text": "...", "type": "PERSON/ORG/LOCATION/etc"}}
        ]
    }}
    """

    response = model.generate_content(prompt)
    clean = response.text.strip()

    try:
        data = json.loads(clean)
        return data

    except:
        clean = clean.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)

def get_emotion(text):
    prompt = f"""
    You are an NLP model. Detect the primary emotion expressed in the text.
    Return ONLY JSON. No explanations.

    Text: "{text}"

    Allowed emotions:
    ["happy", "sad", "angry", "fear", "surprise", "disgust", "neutral"]

    Format:
    {{
        "emotion": "happy/sad/angry/fear/surprise/disgust/neutral"
    }}
    """

    response = model.generate_content(prompt)
    clean = response.text.strip()

    try:
        data = json.loads(clean)
        return data
    except:
        clean = clean.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)