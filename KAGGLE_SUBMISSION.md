# 🎓 Kaggle GenAI Intensive Course - Capstone Project

## Project Title: AI Study Buddy - Intelligent Learning Assistant

### 📋 Project Overview

This capstone project demonstrates the practical application of concepts learned in the **Google & Kaggle GenAI Intensive Course**. The AI Study Buddy is an intelligent learning assistant that leverages:

- **RAG (Retrieval-Augmented Generation)** for accurate, context-aware responses
- **Google Gemini 2.5 Flash** for natural language understanding and generation
- **FAISS Vector Search** for efficient document retrieval
- **Sentence Transformers** for semantic embeddings

### 🎯 Course Concepts Applied

#### 1. **Prompt Engineering (Day 1)**
- Structured prompts for quiz generation
- System prompts for "Study Buddy" persona
- Context-aware question answering

#### 2. **Embeddings & Vector Search (Day 2)**
- Document chunking strategy (1000 chars, 200 overlap)
- Semantic search using sentence-transformers
- FAISS index for similarity search

#### 3. **Generative AI Models (Day 3)**
- Integration with Google Gemini API
- Temperature and parameter tuning
- Structured output generation (quizzes)

#### 4. **RAG Implementation (Day 4)**
- Complete RAG pipeline from scratch
- Document ingestion and preprocessing
- Context retrieval and augmentation

#### 5. **Agent Design (Day 5)**
- Multi-tool agent architecture
- Memory management
- Tool orchestration (search + RAG + LLM)

### 🏗️ Technical Architecture

```
User Input
    ↓
┌─────────────────────────────────────┐
│  Agent (agent.py)                   │
│  - Orchestrates tools               │
│  - Manages conversation memory      │
└─────────────────────────────────────┘
    ↓           ↓           ↓
┌─────────┐ ┌─────────┐ ┌─────────┐
│   RAG   │ │ Search  │ │ Memory  │
│ Engine  │ │  Tool   │ │ System  │
└─────────┘ └─────────┘ └─────────┘
    ↓
┌─────────────────────────────────────┐
│  FAISS Vector DB                    │
│  - 384D embeddings                  │
│  - Cosine similarity search         │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Gemini 2.5 Flash                   │
│  - Answer generation                │
│  - Quiz creation                    │
└─────────────────────────────────────┘
```

### 📊 Key Features Implemented

| Feature | Course Day | Implementation |
|---------|-----------|----------------|
| Document Ingestion | Day 2 | `rag.py` - DocumentProcessor |
| Vector Search | Day 2 | FAISS IndexFlatIP |
| Prompt Templates | Day 1 | ChatPromptTemplate |
| RAG Pipeline | Day 4 | `rag.py` - RAGEngine |
| Agent Orchestration | Day 5 | `agent.py` - ResearchAgent |
| Quiz Generation | Day 1 | Structured prompt engineering |

### 🔬 Innovation & Unique Aspects

1. **Hybrid Context Retrieval**: Combines internal documents (RAG) with web search for comprehensive answers

2. **Educational Focus**: Specifically designed for learning with quiz generation and conversation memory

3. **Production-Ready**: 
   - Error handling and graceful degradation
   - Optional web search (works offline for ingested docs)
   - Clean CLI interface

4. **Efficient Architecture**: 
   - FAISS instead of ChromaDB (faster, no compilation needed)
   - Local embeddings (no API quota for embeddings)
   - Minimal dependencies

### 📈 Performance Metrics

- **Embedding Dimension**: 384D (all-MiniLM-L6-v2)
- **Chunk Size**: 1000 characters with 200 overlap
- **Retrieval**: Top-3 chunks per query
- **Response Time**: ~2-3 seconds (including LLM call)
- **Memory Footprint**: ~500MB (with loaded model)

### 🎓 Learning Outcomes Demonstrated

✅ Understanding of RAG architecture and implementation  
✅ Practical experience with vector databases (FAISS)  
✅ Integration of multiple AI components (embeddings, LLM, search)  
✅ Prompt engineering for specific use cases  
✅ Agent design patterns and tool orchestration  
✅ Production considerations (error handling, API management)  

### 🚀 Future Enhancements

Based on course learnings, potential improvements:

- **Fine-tuning**: Custom embeddings for domain-specific content
- **Multi-modal**: Support for images and diagrams in documents
- **Advanced RAG**: Implement re-ranking and query expansion
- **Evaluation**: Add RAGAS metrics for quality assessment
- **Deployment**: Containerize with Docker, deploy to Cloud Run

### 📚 References & Resources

- [Google Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)

### 👨‍💻 Author

**Anand Kumar & Aryan Jaiswal**  
Google & Kaggle GenAI Intensive Course - Capstone Project

### 📄 License

Open Source - Educational Use

---

## 🎯 Submission Checklist

- [x] Complete README with installation instructions
- [x] Working code with all dependencies listed
- [x] Example usage and sample data
- [x] Documentation of course concepts applied
- [x] Clean, well-structured codebase
- [x] GitHub repository with proper .gitignore
- [ ] Kaggle notebook version (optional)
- [ ] Demo video/screenshots (optional)

---

**This project represents the culmination of knowledge gained from the Google & Kaggle GenAI Intensive Course, demonstrating practical application of RAG, prompt engineering, and agent design patterns.**
