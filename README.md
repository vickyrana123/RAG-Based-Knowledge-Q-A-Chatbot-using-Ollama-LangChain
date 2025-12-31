This project implements a Retrieval-Augmented Generation (RAG) based Knowledge Q&A Chatbot that answers user questions using information extracted from PDF documents. The system combines semantic search with a local Large Language Model (LLM) running via Ollama, ensuring accurate, context-aware, and hallucination-free responses.

The chatbot ingests domain-specific documents (Machine Learning PDFs), stores them in a vector database (ChromaDB), retrieves the most relevant content using embeddings, and generates answers grounded strictly in the retrieved context.


🚀 Key Features :

📄 PDF-based knowledge ingestion
🔎 Semantic search using vector embeddings
🧠 Retrieval-Augmented Generation (RAG) architecture
🤖 Local LLM inference using Ollama (LLaMA 3.2 – 1B)
🗂️ Vector database with ChromaDB
⚡ FastAPI-based backend (optional API mode)
🧠 In-memory conversational caching
🧪 Unit testing with pytest
🔐 Offline, cost-free, and privacy-friendly

🛠️ Tech Stack :

Language: Python
LLM: Ollama (LLaMA 3.2 – 1B)
Framework: LangChain
Vector DB: ChromaDB
Embeddings: HuggingFace Sentence Transformers
API: FastAPI + Uvicorn
Testing: pytest

🏗️ Architecture :

1.) The system follows a RAG pipeline:
2.) Document ingestion and chunking
3.) Embedding generation
4.) Vector storage
5.) Query-time retrieval
6.) Context-aware response generation using LLM
