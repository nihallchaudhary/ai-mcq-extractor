# 🔥 AI MCQ Extractor

An AI-powered application that extracts multiple-choice questions (MCQs) from unstructured PDF documents and converts them into clean, structured JSON format.

---

## 🚀 Overview

This project is designed to automate the process of extracting MCQs from messy exam PDFs. It leverages a locally hosted AI model to intelligently parse text, identify valid questions, and structure them for easy use.

The system handles noisy input data, broken text, and formatting issues, making it useful for students, educators, and content creators.

---

## ✨ Features

* 📄 Extracts text from PDFs using **pdfplumber**
* 🤖 Uses a locally hosted AI model (**LLaMA3**) for intelligent MCQ extraction
* ⚡ Processes large documents efficiently using chunking
* 🧹 Cleans and structures output into JSON format
* 🔁 Removes duplicate questions automatically
* 🖥️ Interactive UI built with **Streamlit**

---

## 🛠️ Tech Stack

* Python
* Streamlit
* pdfplumber
* Requests
* JSON
* Local AI Model (LLaMA3 via API)

---

## ⚙️ How It Works

1. Upload a PDF file through the Streamlit interface
2. Extract raw text from each page
3. Split text into chunks for efficient AI processing
4. Send chunks to the AI model for MCQ extraction
5. Parse and clean JSON output
6. Remove duplicate questions
7. Display MCQs interactively in the UI

---

## 📌 Use Cases

* Exam paper analysis
* Question bank creation
* Educational content digitization
* Practice test generation

---

## 🧠 Key Highlights

* Handles unstructured and noisy data effectively
* Demonstrates integration of AI with real-world applications
* End-to-end pipeline from raw PDF → structured MCQs

---

## 🚧 Future Improvements

* Export to CSV / Excel
* Add answer key detection
* Improve extraction accuracy
* Deploy as a web application

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📷 Demo

![Upload Screen](assets/upload.png)

![Extraction Output](assets/output.png)

---

## 📄 License

This project is for educational purposes.
