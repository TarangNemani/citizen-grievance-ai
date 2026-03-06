from fastapi import FastAPI
from ai_engine import analyze_complaint
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["citizen_ai"]
collection = db["complaints"]

@app.get("/")
def read_root():
    return {"message": "Citizen Grievance AI System Running 🚀"}

@app.post("/complaint")
def create_complaint(text: str):

    analysis = analyze_complaint(text)

    complaint = {
        "text": text,
        "analysis": analysis,
        "status": "received"
    }

    collection.insert_one(complaint)

    return {
        "message": "Complaint analyzed and stored",
        "analysis": analysis
    }