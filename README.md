# 🤖 AI-Powered RAG-Based Enterprise Document Q&A Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG)** chatbot that enables users to interact with enterprise documents using natural language. Built with **LangChain**, **Google Gemini**, **semantic chunking**, **embedding-based retrieval**, and an **In-Memory Vector Store** to deliver accurate, context-aware responses from uploaded PDF documents.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- 🔍 Retrieval-Augmented Generation (RAG) pipeline
- 🧠 Semantic chunking and embedding-based retrieval
- ⚡ In-Memory Vector Store for fast semantic search
- 💬 Context-aware conversational question answering
- 🤖 Google Gemini LLM integration
- 📚 Enterprise knowledge retrieval from proprietary documents
- 🖥️ Interactive Streamlit web interface
- 🔒 Secure API key management using `.env`

---

## 🏗️ System Architecture

```text
                          ┌────────────────────┐
                          │   PDF Document     │
                          └─────────┬──────────┘
                                    │
                                    ▼
                      ┌─────────────────────────┐
                      │  Document Loader        │
                      │ (LangChain PDF Loader)  │
                      └─────────┬───────────────┘
                                │
                                ▼
                     ┌──────────────────────────┐
                     │ Semantic Text Chunking   │
                     └─────────┬────────────────┘
                               │
                               ▼
                  ┌─────────────────────────────┐
                  │ Gemini Embedding Model      │
                  └─────────┬───────────────────┘
                            │
                            ▼
                ┌──────────────────────────────┐
                │ In-Memory Vector Store        │
                └─────────┬────────────────────┘
                          │
                          ▼
                ┌──────────────────────────────┐
                │ Similarity Search Retriever   │
                └─────────┬────────────────────┘
                          │
                          ▼
                ┌──────────────────────────────┐
                │ Google Gemini LLM            │
                └─────────┬────────────────────┘
                          │
                          ▼
                ┌──────────────────────────────┐
                │ Context-Aware Response       │
                └──────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Framework | Streamlit |
| LLM Framework | LangChain |
| LLM | Google Gemini |
| Embeddings | Gemini Embeddings |
| Vector Store | InMemoryVectorStore |
| Document Loader | PyPDFLoader |
| Text Processing | Recursive Character Text Splitter |
| Environment Management | python-dotenv |

---

## 📂 Project Structure

```text
RAG-BASED-ENTERPRISE-CHAT-BOT/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
├── uploaded_document.pdf
└── images/
    ├── home.png
    └── chat.png
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Sayeed-Ansari/RAG-BASED-ENTERPRISE-CHAT-BOT.git
cd RAG-BASED-ENTERPRISE-CHAT-BOT
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Upload a PDF document.
2. The document is loaded using LangChain.
3. Text is split into semantic chunks.
4. Chunks are converted into vector embeddings.
5. Embeddings are stored in an In-Memory Vector Store.
6. User questions are converted into embeddings.
7. Relevant document chunks are retrieved using similarity search.
8. Retrieved context is passed to Google Gemini.
9. Gemini generates a context-aware response grounded in the uploaded document.

---


## 🎯 Future Enhancements

- ✅ Support for multiple document uploads
- ✅ Persistent vector databases (FAISS / ChromaDB)
- ✅ Role-based authentication
- ✅ Citation and source highlighting
- ✅ Multi-format document support (DOCX, PPTX, TXT)
- ✅ Deployment on Streamlit Cloud or AWS

---

## 👨‍💻 Author

**Sayeed Ansari**

- GitHub: https://github.com/Sayeed-Ansari
- LinkedIn: *https://www.linkedin.com/in/sayeedansari/*

---

## ⭐ If you found this project useful, consider giving it a Star!
