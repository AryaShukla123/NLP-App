import google.generativeai as genai
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

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

def detect_language(text):
    prompt = f"""
    You are an NLP model. Detect the language of the following text.
    Return ONLY JSON. No explanations.

    Text: "{text}"

    Format:
    {{
        "language": "English/French/Spanish/etc"
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

def get_paraphrase(text):
    prompt = f"""
    You are an NLP model. Paraphrase the following text.
    Return ONLY JSON. No extra text.

    Text: "{text}"

    Format:
    {{
        "paraphrased_text": "Your paraphrased version of the text here"
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

def semantic_search(query):
    prompt = f"""
    You are an NLP model performing semantic search.

    Task:
    Given a user query, return the top 5 semantically similar topics or ideas.

    Return ONLY JSON. No explanation.

    Query: "{query}"

    Format:
    {{
        "results": [
            "result 1",
            "result 2",
            "result 3",
            "result 4",
            "result 5"
        ]
    }}
    """

    response = model.generate_content(prompt)
    clean = response.text.strip()

    try:
        return json.loads(clean)
    except:
        clean = clean.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)

def semantic_similarity(text1, text2):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    Calculate the semantic similarity between these two texts.
    Text 1: {text1}
    Text 2: {text2}

    Give the answer only in this JSON format:
    {{
        "similarity_score": number_between_0_and_1,
        "explanation": "short explanation here"
    }}
    """

    response = model.generate_content(prompt)

    try:
        # Gemini response contains JSON inside text
        import json
        data = json.loads(response.text)
        return data

    except:
        return {
            "similarity_score": 0,
            "explanation": "Could not calculate similarity."
        }

def summarize_text(text):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    Summarize the following text in a concise and clear way.

    Text: {text}

    Give the answer ONLY in this JSON format:
    {{
        "summary": "summarized text here",
        "length": "short/medium/long"
    }}
    """

    response = model.generate_content(prompt)

    try:
        import json
        data = json.loads(response.text)
        return data

    except:
        return {
            "summary": "",
            "length": "unknown"
        }
def summarize_text(text):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    You are an NLP summarization model.
    Summarize the following text in a short and clear way.
    Do NOT add anything extra.

    Text: "{text}"

    Return only JSON in this format:
    {{
        "summary": "your summary here"
    }}
    """

    response = model.generate_content(prompt)
    clean = response.text.strip()

    import json
    try:
        data = json.loads(clean)
        return data

    except:
        clean = clean.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)

def translate_text(text, target_lang):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    You are a translation model.
    Translate the following text into the target language.

    Text: "{text}"
    Target Language: "{target_lang}"

    Return ONLY JSON:
    {{
        "translated_text": "..."
    }}
    """

    response = model.generate_content(prompt)
    clean = response.text.strip()

    import json
    try:
        return json.loads(clean)
    except:
        clean = clean.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)

def answer_question(question, context):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    You are a QA model.
    Answer the question using the given context.
    Return ONLY JSON.

    Context: "{context}"

    Question: "{question}"

    JSON Format:
    {{
        "answer": "..."
    }}
    """

    response = model.generate_content(prompt)
    clean = response.text.strip()

    import json
    try:
        return json.loads(clean)
    except:
        clean = clean.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)


