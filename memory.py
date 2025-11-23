class SimpleMemory:
    def __init__(self):
        self.history = []

    def add_interaction(self, query, response, results=None):
        """
        Adds a user-agent interaction to the memory.
        """
        interaction = {
            "query": query,
            "response": response,
            "results": results
        }
        self.history.append(interaction)

    def get_history(self):
        """
        Returns the full conversation history.
        """
        return self.history

    def search_history(self, query):
        """
        Simple keyword search in history.
        """
        matches = []
        for interaction in self.history:
            if query.lower() in interaction["query"].lower() or query.lower() in interaction["response"].lower():
                matches.append(interaction)
        return matches

    def clear(self):
        """
        Clears the memory.
        """
        self.history = []
