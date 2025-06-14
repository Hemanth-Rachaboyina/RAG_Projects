# LlamaIndex Document QA Pipeline
This project is a full-fledged pipeline that brings the power of LLMs (Large Language Models) and vector databases into one seamless workflow. It’s built to demonstrate how you can turn raw documents — PDFs, text files, and more — into a smart, searchable knowledge system.

At its core, the project uses LlamaIndex to handle document ingestion, transformation, and indexing. With the help of Groq’s high-performance LLMs, the system can intelligently extract useful insights like titles and question-answer pairs directly from your documents. These insights are then embedded using a HuggingFace model and stored in a vector index — allowing for fast and intelligent semantic search.

You can ask natural language questions like "What is this document about?" or "What are the key points covered?" and the system will respond using the combined power of the vector index and a large language model.

Whether you're building a Retrieval-Augmented Generation (RAG) system, a document assistant, or just want to organize unstructured content into something queryable, this project serves as a modular and practical starting point.

There’s also support for ChromaDB, so you can scale your storage needs beyond local environments and plug into a more production-ready backend.

In short, it’s a great demonstration of how to combine modern AI tools to turn static documents into interactive knowledge bases.

---

## 📌 Features

- 📄 Load documents from a directory (`./data`)
- 🔄 Transform text with advanced metadata handling
- 🧠 Extract titles and Q&As using Groq's LLMs
- 💡 Generate embeddings via HuggingFace's `bge-small-en-v1.5`
- 🔍 Create a `VectorStoreIndex` for intelligent querying
- 💾 Persist vectors locally or use ChromaDB
- 🗣️ Ask questions about the data using LLM-based query engine

---

## 🏗️ Pipeline Overview


📂 ./data → 🧹 Transformation → 🧠 LLM-based Extraction → 📌 Embeddings → 🧾 Indexing → 🔍 Query Engine → 💬 Answers



## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -U llama-index
pip install -U llama-index-llms-groq
pip install -U llama-index-embeddings-huggingface
pip install -U chromadb
pip install -U llama-index-vector-stores-chroma
```

### 2. Prepare Environment
Store your Groq API key securely:

```bash
import os
import getpass
os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
```

 ### 3. Add Your Documents 
   Place your input documents (e.g., PDFs or TXT files) inside the `./data/` directory.


 ### 4. Set Up Groq API Key  
   When running the script, you'll be prompted to enter your Groq API key for LLM-powered extraction and querying.

 ### 5. Run the Pipeline Script  
   Execute the script (`main.py` or notebook):
   - It will load and transform the documents
   - Extract Q&As and titles using Groq LLM
   - Generate embeddings using HuggingFace
   - Build and persist the vector index

 ### 6. (Optional) Use ChromaDB for Vector Storage  
   You can opt to use ChromaDB instead of local vector storage for better scalability.

 ### 7. Start Querying  
   Use the built-in query engine to ask questions and get intelligent responses from your documents.

