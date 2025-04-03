# VOX AI Voice Assistant

## 📌 Overview

VOX AI Voice Assistant is a real-time voice-enabled AI assistant that allows users to interact with documents through natural conversations. Built using **Streamlit**, **LangChain**, **FAISS**, **Groq's Llama 3.3**, and **speech recognition**, this application enables users to upload a PDF and ask voice-based queries about its content.

## ✨ Features

- **Real-time voice interaction**: Converts speech to text and generates spoken responses.
- **Retrieval-Augmented Generation (RAG)**: Extracts relevant information from uploaded documents.
- **Integration with Llama 3.3 (Groq)**: Enhances question-answering capabilities.
- **Efficient vector search (FAISS)**: Enables quick and accurate retrieval of document information.
- **Streamlit UI**: Provides a simple interface for uploading PDFs and starting voice interactions.

## 🏗️ Tech Stack

- **Python**
- **Streamlit** (Frontend UI)
- **LangChain** (Conversational AI framework)
- **FAISS** (Vector database for similarity search)
- **Llama 3.3 via Groq** (Large Language Model)
- **pyttsx3** (Text-to-Speech)
- **speech_recognition** (Speech-to-Text)
- **Hugging Face Embeddings** (Text vectorization)
- **PyPDFLoader** (PDF document processing)

## 🚀 Installation & Setup

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/your-username/VOX-AI-Voice-Assistant.git
cd VOX-AI-Voice-Assistant
```

2️⃣ **Create a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
venv\Scripts\activate
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Set Up API Keys**

Create a .env file in the root directory and add the following environment variables:

```bash
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

5️⃣ **Run the Application**

```bash
streamlit run app.py
```

## 🛠️ Usage
1️⃣ Upload a PDF document.

2️⃣ Click on the "Start Voice Chat" button.

3️⃣ Speak your queries, and VOX AI will respond with relevant answers based on the document.

🏗️ Future Enhancements
- Support for multiple document uploads.
- Enhanced voice synthesis with ElevenLabs API.
- Improved UI/UX for a better user experience.
- Deployment on cloud platforms.
