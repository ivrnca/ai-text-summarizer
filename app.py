import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

st.set_page_config(page_title="AI Text Summarizer", page_icon="📝", layout="centered")
st.title("📝 AI Text Summarizer")
st.caption("Month 1 – Project 1 (Groq)")

if not os.getenv("GROQ_API_KEY"):
    st.error("GROQ_API_KEY not found in .env file.")
else:
    st.success("Groq environment is ready.")

st.write("If you see this message and a green box, Groq + Streamlit setup is working.")
