from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import SearchTool
from memory import SimpleMemory
import os
from dotenv import load_dotenv
from rag import RAGEngine

load_dotenv()

class ResearchAgent:
    def __init__(self):
        self.memory = SimpleMemory()
        self.search_tool = SearchTool()
        self.rag_engine = RAGEngine()
        
        # Initialize LLM - Gemini Only
        if os.getenv("GOOGLE_API_KEY"):
            self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        else:
            print("Error: GOOGLE_API_KEY not found in .env")
            self.llm = None


        self.prompt = ChatPromptTemplate.from_template("""
        You are the "AI Study Buddy", a helpful and encouraging tutor.
        Your goal is to help the user learn and understand the material.
        
        User Query: {query}
        
        Context Information:
        {context}
        
        Based on the context provided above (both internal documents and web search), please provide a comprehensive answer to the user's query.
        If the context is not relevant, say so.
        """)

    def generate_quiz(self, topic):
        """Generates a 5-question quiz based on the topic and available context."""
        print(f"Generating quiz on: {topic}...")
        
        # 1. Retrieve Context
        rag_docs = self.rag_engine.query(topic, k=5)
        context = "\n".join(rag_docs) if rag_docs else "No specific internal documents found. Use general knowledge."
        
        # 2. Prompt for Quiz
        quiz_prompt = ChatPromptTemplate.from_template("""
        You are an AI Study Buddy.
        Create a 5-question multiple-choice quiz about: {topic}
        
        Use the following context if available:
        {context}
        
        Format the output clearly:
        1. Question
        A) Option
        B) Option
        C) Option
        D) Option
        Answer: (Correct Option)
        
        (Repeat for 5 questions)
        """)
        
        if self.llm:
            chain = quiz_prompt | self.llm | StrOutputParser()
            try:
                response = chain.invoke({"topic": topic, "context": context})
                return response
            except Exception as e:
                return f"Error generating quiz: {str(e)}"
        else:
            return "LLM not configured. Cannot generate quiz."

    def process_query(self, query):
        # 1. RAG Retrieval
        print(f"Checking internal documents...")
        rag_docs = self.rag_engine.query(query)
        rag_context = "\n".join(rag_docs) if rag_docs else "No relevant internal documents found."

        # 2. Web Search
        if self.search_tool.active:
            print(f"Searching web for: {query}...")
            search_results = self.search_tool.search(query)
        else:
            print(f"Thinking (Web Search disabled)...")
            search_results = "Web search disabled."
        
        # 3. Combine Context
        full_context = f"--- Internal Documents ---\n{rag_context}\n\n--- Web Search Results ---\n{search_results}"
        
        if self.llm:
            chain = self.prompt | self.llm | StrOutputParser()
            try:
                response = chain.invoke({"query": query, "context": full_context})
            except Exception as e:
                response = f"Error generating response: {str(e)}"
        else:
            response = f"Context:\n{full_context}\n\n(LLM not configured to summarize)"
        
        self.memory.add_interaction(query, response, full_context)
        return response
