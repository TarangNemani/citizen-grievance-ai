# ai_engine.py — Gemini version
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_complaint(text):
    prompt = f"""
    Analyze the following citizen complaint.

    Complaint: {text}

    Return:
    1. Category
    2. Urgency (Low/Medium/High)
    3. Short Summary
    """
    response = model.generate_content(prompt)
    return response.text
