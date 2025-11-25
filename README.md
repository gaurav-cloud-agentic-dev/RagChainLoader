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

### 1. Install Python dependencies

Install all required LangChain, Qdrant, OpenAI, and PDF-processing libraries.

### 2. Start Qdrant via Docker

Run Qdrant locally using Docker Compose.  
It should be available at:

```
http://localhost:6333
```

### 3. Add your OpenAI API key

Create a `.env` file and add your `OPENAI_API_KEY`.

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

You run it **once** (or whenever you change the PDF).

---

### **chat.py — Query + Retrieval + Answering**

This script:

1. Connects to the existing Qdrant collection created by `index.py`
2. Converts your question into an embedding  
3. Retrieves the most similar chunks from Qdrant  
4. Builds a context block that includes:
   - page content  
   - page number  
   - source PDF path  
5. Sends both your question and the retrieved context to `gpt-4o-mini`
6. Returns a grounded answer referring to the correct page number  

This file is used every time you want to **query your documents**.

---

### **.env — Environment Variables**

Stores:

- Your OpenAI API key  
- Any other optional configs  

---

### **node-dev.pdf — Document for RAG**

This is the PDF file being indexed and queried.

You can replace it with any PDF you want.

---

## 🧠 How the Workflow Looks

1. **Run indexing once**  
   Builds the vector store from the PDF.

2. **Run the chat script anytime**  
   Retrieves relevant vector chunks → Sends them to the LLM →  
   Returns an accurate answer based only on your document.

---

## 🪄 Example Flow (Conceptual)

- You ask: *"How does the Node.js event loop work?"*  
- Qdrant returns the best matching chunks from the PDF  
- The LLM reads only that context  
- It answers and tells you the exact **page number** to refer to  

---

## 🙌 Contributions

Feel free to open issues or submit pull requests.

---

## 📄 License

MIT License
