from langchain_community.utilities import GoogleSearchAPIWrapper
import os
from dotenv import load_dotenv

load_dotenv()

class SearchTool:
    def __init__(self):
        # Check for Google Search keys
        if os.getenv("GOOGLE_API_KEY") and os.getenv("GOOGLE_CSE_ID"):
            self.search_engine = GoogleSearchAPIWrapper()
            self.active = True
        else:
            print("Warning: Google Search keys not found. Search will be disabled.")
            self.search_engine = None
            self.active = False

    def search(self, query):
        """
        Executes a search if active.
        """
        if not self.active:
            return "Search is disabled (no API keys configured)."
            
        try:
            results = self.search_engine.run(query)
            return results
        except Exception as e:
            return f"Error performing search: {str(e)}"

    def parse_results(self, results):
        """
        Parses and formats the search results (if needed).
        For now, just returns the raw string as LangChain tools usually return strings.
        """
        return results
