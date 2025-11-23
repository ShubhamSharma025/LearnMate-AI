from agent import ResearchAgent
from rag import DocumentProcessor
import sys
import os

def main():
    print("Initializing Research Agent...")
    agent = ResearchAgent()
    processor = DocumentProcessor()
    
    print("Agent ready!")
    print("Commands:")
    print(" - 'exit': Quit")
    print(" - 'history': View past interactions")
    print(" - 'clear': Clear memory")
    print(" - 'ingest <path>': Load a document (PDF/TXT) into knowledge base")
    print(" - 'quiz <topic>': Generate a quiz on a topic")

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            if user_input.lower().startswith('ingest '):
                file_path = user_input[7:].strip()
                print(f"Processing {file_path}...")
                result = processor.process_and_store(file_path)
                print(result)
                continue

            if user_input.lower().startswith('quiz '):
                topic = user_input[5:].strip()
                result = agent.generate_quiz(topic)
                print(f"\n--- Quiz: {topic} ---\n{result}\n---------------------")
                continue
            
            if user_input.lower() == 'history':
                # ... (existing history logic) ...
                history = agent.memory.get_history()
                if not history:
                    print("No history yet.")
                else:
                    for i, interaction in enumerate(history):
                        print(f"\n--- Interaction {i+1} ---")
                        print(f"User: {interaction['query']}")
                        print(f"Agent: {interaction['response'][:100]}...") 
                continue

            if user_input.lower() == 'clear':
                agent.memory.clear()
                print("Memory cleared.")
                continue

            response = agent.process_query(user_input)
            print(f"\nAgent: {response}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
