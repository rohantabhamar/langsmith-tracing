from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
import os


def get_model():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.1,
        api_key=os.getenv("GROQ_API_KEY")
    )

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )