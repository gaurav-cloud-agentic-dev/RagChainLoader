# LangChain-Based RAG Document Loader using Qdrant (Docker)

This project implements a complete **Retrieval-Augmented Generation (RAG)** pipeline using:

- **LangChain**
- **Qdrant Vector Database** (via Docker)
- **OpenAI Embeddings**
- **PDF document loading and chunking**
- **A query/chat script to ask questions from your documents**

It provides an end-to-end workflow:  
**PDF → Text Chunks → Embeddings → Qdrant → Retrieval → AI Answer**

---

## 🚀 Features

- Load PDF documents using LangChain’s PDF loader  
- Split text into structured, overlapping chunks  
- Generate vector embeddings using OpenAI’s embedding model  
- Store embedded chunks in a Qdrant collection  
- Retrieve relevant document chunks using semantic search  
- Use an LLM to answer questions grounded in retrieved context  

---

## 📦 Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/gaurav-cloud-agentic-dev/RagChainLoader.git
cd RagChainLoader
```

---

### 2. Install Python Dependencies

Install all required packages using:

```
pip install -qU langchain-qdrant
pip install -qU langchain-openai
pip install -qU langchain-text-splitters
pip install -qU langchain-community
pip install pypdf
pip install python-dotenv
pip install openai
```

You may also install everything together:

```
pip install -qU langchain-qdrant langchain-openai langchain-text-splitters langchain-community pypdf python-dotenv openai
```

---

### 3. Start Qdrant Using Docker

Download and run Qdrant locally:

```
docker compose up -d
```

Qdrant will be available at:

```
http://localhost:6333
```

---

### 4. Add Your OpenAI API Key

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 📁 Project Structure

```
.
├── index.py         # Indexing script (loads PDF, splits, embeds, pushes to Qdrant)
├── chat.py          # Query interface for Qdrant + LLM
├── node-dev.pdf     # PDF document used for RAG
├── .env             # Stores API keys
└── README.md
```

Here’s what each file does:

---

### **index.py — Document Indexing Script**

This script:

1. Loads the PDF using LangChain’s `PyPDFLoader`
2. Splits it into smaller text chunks using a recursive text splitter
3. Generates embeddings using OpenAI’s `text-embedding-3-large`
4. Creates a Qdrant collection (if not already created)
5. Inserts all the document chunks into the Qdrant vector database  
6. Prints confirmation after indexing is completed  

This file is responsible for **building** the vector index.

Run it **once**, or whenever you update the PDF.

---

### **chat.py — Query + Retrieval + Answering**

This script:

1. Connects to the existing Qdrant collection created by `index.py`
2. Converts your question into an embedding  
3. Retrieves the most similar chunks from Qdrant  
4. Builds a context block containing:
   - Page content  
   - Page number  
   - Source PDF path  
5. Sends the context + user question to `gpt-4o-mini`
6. Returns a grounded answer pointing to the correct page  

Use this file every time you want to **query your documents**.

---

### **.env — Environment Variables**

Stores:

- Your OpenAI API key  
- Any additional configuration needed  

---

### **node-dev.pdf — Document for RAG**

The PDF used for indexing and question answering.  
You can replace it with your own document.

---

## 🧠 How the Workflow Looks

1. **Run `index.py` once**  
   Builds the vector database from the PDF.

2. **Run `chat.py` whenever you need answers**  
   Retrieves the most relevant document chunks →  
   Passes context to the LLM →  
   Returns accurate, source-grounded answers.

---

## 🪄 Example Flow (Conceptual)

- You ask: *"How does the Node.js event loop work?"*  
- Qdrant returns the best matching PDF chunks  
- The LLM reads only that context  
- It responds and tells you the related **page number**  

---

## 🙌 Contributions

Feel free to open issues or submit pull requests.

---

## 📄 License

MIT License
