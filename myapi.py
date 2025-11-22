import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyBeJrycNLRVb5C3D8q0UuobY3hLquXMdiE")

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