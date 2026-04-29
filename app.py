import streamlit as st
import pdfplumber
import requests
import json

# =========================
# TEXT EXTRACTION
# =========================
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text

# =========================
# REMOVE DUPLICATES
# =========================
def remove_duplicates(questions):
    seen = set()
    unique = []

    for q in questions:
        q_text = q.get("question", "").strip()
        if q_text and q_text not in seen:
            seen.add(q_text)
            unique.append(q)

    return unique

# =========================
# AI EXTRACTION (CHUNKED)
# =========================
def ai_extract_mcqs(text):
    chunk_size = 8000
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    all_questions = []

    for i, chunk in enumerate(chunks):
        st.info(f"Processing chunk {i+1}/{len(chunks)}...")

        prompt = f"""
You are given messy exam text.

Extract ONLY valid MCQs.

Return STRICT JSON:
[
  {{
    "number": "1",
    "question": "full question",
    "options": ["A...", "B...", "C...", "D..."]
  }}
]

Rules:
- Ignore instructions
- Ignore garbage text
- Fix broken sentences
- Combine split words
- Minimum 2 options required
- Clean output

TEXT:
{chunk}
"""

        try:
            res = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                }
            )

            output = res.json()["response"]

            start = output.find("[")
            end = output.rfind("]") + 1

            data = json.loads(output[start:end])

            all_questions.extend(data)

        except Exception as e:
            print("Chunk failed:", e)
            continue

    return remove_duplicates(all_questions)

# =========================
# UI
# =========================
st.title("🔥 AI MCQ Extractor (Final Version)")

file = st.file_uploader("Upload PDF")

if file:
    text = extract_text(file)

    st.warning("⏳ Extracting MCQs using AI...")

    questions = ai_extract_mcqs(text)

    if not questions:
        st.error("❌ Could not extract MCQs")
        st.stop()

    st.success(f"✅ Extracted {len(questions)} questions")

    answers = {}

    for i, q in enumerate(questions):
        key = f"q_{i}"

        st.write(f"**{q['number']} {q['question']}**")

        answers[key] = st.radio(
            "Select",
            q["options"],
            key=key
        )