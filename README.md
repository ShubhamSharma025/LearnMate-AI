# 🤖 AI Study Buddy

An intelligent study companion that helps you learn by answering questions, generating quizzes, and remembering your conversations. Powered by Google Gemini and RAG (Retrieval-Augmented Generation).

---

## ✨ Features

- 📚 **Document Ingestion**: Load PDF or TXT files into the knowledge base
- 💬 **Smart Q&A**: Ask questions and get answers from your documents + web search
- 📝 **Quiz Generation**: Auto-generate multiple-choice quizzes on any topic
- 🧠 **Conversation Memory**: Remembers your chat history
- 🔍 **RAG Pipeline**: Uses FAISS vector search for accurate document retrieval

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.8+
- Google Gemini API Key ([Get one here](https://ai.google.dev/))

### 2. Installation

```bash
# Clone or download this project
cd ai

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
GOOGLE_CSE_ID=your_google_search_id  # Optional, for web search
```

### 4. Run

```bash
python main.py
```

---

## 📖 How to Use

### Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `ingest <file>` | Load a document | `ingest notes.pdf` |
| `<question>` | Ask anything | `What is photosynthesis?` |
| `quiz <topic>` | Generate a quiz | `quiz quantum physics` |
| `history` | View past chats | `history` |
| `clear` | Clear memory | `clear` |
| `exit` | Quit | `exit` |

### Example Session

```
You: ingest sample.txt
Agent: Successfully processed 1 chunks from sample.txt.

You: Who is Dr. Barista?
Agent: Dr. Barista is the project lead of the secret "Apollo" 
       initiative to build a quantum-powered coffee machine...

You: quiz Dr. Barista
Agent: [Generates 5-question quiz]

You: exit
Agent: Goodbye!
```

---

## 🏗️ How It Works

### RAG Pipeline

```
┌─────────────────────────────────────────────────────────┐
│  1. YOU: "Who is Dr. Barista?"                         │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  2. EMBEDDING: Question → Vector [0.23, -0.45, ...]    │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  3. FAISS SEARCH: Find similar chunks                  │
│     → "Dr. Barista... quantum coffee..."               │
│     → "...Swiss Alps bunker..."                        │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  4. GEMINI: Generate answer from context              │
└─────────────────────────────────────────────────────────┘
```

### Architecture

- **LLM**: Google Gemini 2.5 Flash
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2 (384D)
- **Vector DB**: FAISS (Facebook AI Similarity Search)
- **Search**: Google Custom Search API (optional)

---

## 📁 Project Structure

```
ai/
├── main.py              # CLI interface
├── agent.py             # Core agent logic
├── rag.py               # RAG engine (FAISS + embeddings)
├── tools.py             # Web search tool
├── memory.py            # Conversation memory
├── requirements.txt     # Python dependencies
├── .env                 # API keys (create this)
├── sample.txt           # Example document
└── db/                  # Vector database storage
    └── chunks.txt       # Stored document chunks
```

---

## 🔧 Technical Details

### Dependencies

```
langchain                    # LLM framework
langchain-community          # Community integrations
langchain-google-genai       # Gemini integration
google-api-python-client     # Google Search API
sentence-transformers        # Embeddings model
faiss-cpu                    # Vector search
pypdf                        # PDF support
requests                     # HTTP requests
```

### How Documents Are Processed

1. **Load**: Read PDF/TXT file
2. **Split**: Break into 1000-character chunks (200 overlap)
3. **Embed**: Convert each chunk to 384D vector using `all-MiniLM-L6-v2`
4. **Store**: Save vectors in FAISS index + text in `db/chunks.txt`
5. **Query**: Convert question to vector → Find top 3 similar chunks → Send to Gemini

---

## 💡 Usage Tips

### For Best Results

1. **Ingest focused documents**: Separate files for different topics
2. **Ask specific questions**: "What is X?" > "Tell me about stuff"
3. **Use quizzes for review**: Generate quizzes after reading material
4. **Check history**: Use `history` to review what you've learned

### Creating Study Material

Create a text file with your notes:

**biology_notes.txt**
```
Photosynthesis:
Plants convert light energy into chemical energy using chloroplasts.
Equation: 6CO2 + 6H2O + light → C6H12O6 + 6O2

Cellular Respiration:
Cells break down glucose to release ATP energy.
```

Then:
```
You: ingest biology_notes.txt
You: What is photosynthesis?
You: quiz cellular respiration
```

---

## 🚨 Troubleshooting

### Common Issues

**Error: `ModuleNotFoundError`**
```bash
pip install -r requirements.txt
```

**Error: `GOOGLE_API_KEY not found`**
- Create `.env` file with your API key
- Get key from: https://ai.google.dev/

**Error: `429 Quota exceeded`**
- You've hit the API rate limit
- Wait 1 minute and try again
- Free tier: 15 requests/minute for gemini-2.5-flash

**Slow first run**
- Downloads embedding model (~90MB) on first use
- Subsequent runs are much faster

**Wrong answers**
- Make sure you ingested the correct document
- Try more specific questions
- Check if document was processed: look for `db/chunks.txt`

---

## 📊 API Costs

### Gemini API (Free Tier)

- **Rate Limit**: 15 requests/minute
- **Monthly Quota**: Check [Google AI Studio](https://ai.google.dev/)
- **Cost**: Free tier available, then pay-as-you-go

### Offline Capabilities

- ✅ Document ingestion (after first model download)
- ✅ Vector search
- ❌ Answer generation (requires Gemini API)
- ❌ Web search (requires internet)

---

## 🎓 Example Use Cases

### 1. Exam Preparation
```bash
You: ingest chemistry_chapter5.pdf
You: quiz chemical bonding
You: What is the difference between ionic and covalent bonds?
```

### 2. Research Notes
```bash
You: ingest research_paper.pdf
You: Summarize the main findings
You: What methodology did they use?
```

### 3. Language Learning
```bash
You: ingest spanish_vocabulary.txt
You: quiz spanish verbs
You: How do you conjugate "hablar"?
```

---

## 🔐 Privacy & Security

- ✅ Documents stored locally in `db/` folder
- ✅ No data sent to third parties (except Gemini API for answers)
- ✅ API key stored in `.env` (add to `.gitignore`)
- ⚠️ Questions and answers sent to Google Gemini API

---

## 🤝 Contributing

Want to improve this project? Here are some ideas:

- [ ] Add support for more document formats (DOCX, EPUB)
- [ ] Implement conversation context in prompts
- [ ] Add flashcard generation
- [ ] Create web UI with Streamlit
- [ ] Support multiple languages
- [ ] Add export functionality (PDF reports)

---

## 📄 License

This project is open source. Feel free to use and modify as needed.

---

## 🙏 Acknowledgments

- **Google Gemini** - LLM API
- **Sentence Transformers** - Embedding models
- **FAISS** - Vector search
- **LangChain** - LLM framework

---

## 📞 Support

Having issues? Check:
1. This README's troubleshooting section
2. [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)
3. [LangChain Documentation](https://python.langchain.com/)

---

**Happy studying! 🎉**
