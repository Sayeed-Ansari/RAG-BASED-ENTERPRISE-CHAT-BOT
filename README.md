# AI Document Q&A Bot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot that enables intelligent question answering over enterprise documents. Built using LangChain, semantic chunking, embeddings, vector search, and LLMs to provide accurate, context-aware responses from uploaded PDFs.

## Features

- 📄 PDF document ingestion
- ✂️ Semantic text chunking
- 🧠 Embedding-based retrieval
- 🔍 In-memory vector search
- 🤖 LLM-powered question answering
- ⚡ Built with Streamlit for an interactive UI

## Tech Stack

- Python
- LangChain
- Streamlit
- Google Gemini / Groq
- InMemoryVectorStore
- Python-dotenv

## Installation

```bash
git clone https://github.com/<your-username>/Documentation-QnA-Bot.git
cd Documentation-QnA-Bot

pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

Run the app:

```bash
streamlit run app.py
```
