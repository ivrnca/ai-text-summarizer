import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Page config
st.set_page_config(page_title="AI Text Summarizer", page_icon="📝", layout="centered")
st.title("📝 AI Text Summarizer")
st.caption("Month 1 – Project 1 (Groq)")

# Input box for text
input_text = st.text_area("Paste your text here to summarize:", height=220, placeholder="Drop your article, notes, or transcript here...")

# Live counters
word_count = len(input_text.split()) if input_text else 0
char_count = len(input_text) if input_text else 0
st.caption(f"{word_count} words • {char_count} characters")

# Select model
model_choice = st.selectbox(
    "Choose summarization model:",
    ["llama3-8b-8192", "llama3-70b-8192"], # Groq-supported models
    index=0
)

# Action row
summarize_btn = st.button("Summarize", type="primary", disabled=not input_text.strip())


# Result placeholder
summary_container = st.container()

if summarize_btn:
    try:
        with st.spinner("Summarizing..."):
            response = client.chat.completions.create(
                model=model_choice,
                messages=[
                    {"role": "system", "content": "You summarize text clearly and concisely. Keep it faithful, avoid fluff."},
                    {"role": "user", "content": f"Summarize this text in 5-7 sentences:\n\n{input_text}"}
                ],
                temperature=0.5,
                max_tokens=300
            )
            summary = response.choices[0].message.content.strip()

        with summary_container:
            st.subheader("Summary")
            st.write(summary)

            # Download button
            st.download_button(
                label="Download summary (.txt)",
                data=summary.encode("utf-8"),
                file_name="summary.txt",
                mime="text/plain"
            )

    except Exception as e:
        st.error(f"Error: {str(e)}")