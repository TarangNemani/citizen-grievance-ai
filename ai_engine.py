from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_complaint(text):

    prompt = f"""
    Analyze the following citizen complaint.

    Complaint: {text}

    Return:
    1. Category
    2. Urgency (Low/Medium/High)
    3. Short Summary
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content