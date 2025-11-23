import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

class DocumentProcessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def load_document(self, file_path):
        """Loads a PDF or TXT file."""
        if not os.path.exists(file_path):
            return f"Error: File {file_path} not found."

        try:
            if file_path.lower().endswith('.pdf'):
                loader = PyPDFLoader(file_path)
            else:
                loader = TextLoader(file_path)
            
            documents = loader.load()
            return documents
        except Exception as e:
            return f"Error loading file: {str(e)}"

    def process_and_store(self, file_path, persist_directory="./db"):
        """Loads, splits, and stores document in vector DB."""
        documents = self.load_document(file_path)
        if isinstance(documents, str): # Error message
            return documents

        chunks = self.text_splitter.split_documents(documents)
        
        if not chunks:
            return "No text found in document."

        # Store chunks for RAGEngine to use
        chunk_texts = [doc.page_content for doc in chunks]
        
        # Save to file
        os.makedirs(persist_directory, exist_ok=True)
        chunks_file = os.path.join(persist_directory, "chunks.txt")
        with open(chunks_file, "w", encoding="utf-8") as f:
            for chunk in chunk_texts:
                f.write(chunk + "\n---CHUNK---\n")
        
        return f"Successfully processed {len(chunks)} chunks from {os.path.basename(file_path)}."

class RAGEngine:
    def __init__(self, persist_directory="./db"):
        self.persist_directory = persist_directory
        self.embed_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.chunks = []
        self.index = None
        
        # Load existing chunks if available
        chunks_file = os.path.join(persist_directory, "chunks.txt")
        if os.path.exists(chunks_file):
            with open(chunks_file, "r", encoding="utf-8") as f:
                content = f.read()
                self.chunks = [c.strip() for c in content.split("---CHUNK---") if c.strip()]
            
            if self.chunks:
                # Build FAISS index
                chunk_embeddings = self.embed_model.encode(self.chunks, convert_to_numpy=True, show_progress_bar=False)
                chunk_embeddings = self._normalize(chunk_embeddings).astype("float32")
                
                d = chunk_embeddings.shape[1]
                self.index = faiss.IndexFlatIP(d)
                self.index.add(chunk_embeddings)

    def _normalize(self, vecs: np.ndarray):
        norms = np.linalg.norm(vecs, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return vecs / norms

    def query(self, query_text, k=3):
        """Retrieves relevant chunks for a query."""
        if not self.index or not self.chunks:
            return []
        
        try:
            q_emb = self.embed_model.encode([query_text], convert_to_numpy=True, show_progress_bar=False)
            q_emb = self._normalize(q_emb).astype("float32")
            D, I = self.index.search(q_emb, min(k, len(self.chunks)))
            top_chunks = [self.chunks[i] for i in I[0] if i < len(self.chunks)]
            return top_chunks
        except Exception as e:
            print(f"RAG Query Error: {e}")
            return []
