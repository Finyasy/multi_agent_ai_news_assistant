class State:
    def __init__(self,search_agent, synthesis_agent):
        self.search_agent = search_agent
        self.synthesis_agent = synthesis_agent
        self.topic = ""
        self.results = []

    def reset_state(self):
        """Resets the state for a new topic"""
        self.topic = ""
        self.results = []

    def process_news(self,topic):
        """
        Processes news for the given topic using the search and synthesis agents.

        Args:
            topic (str): The topic to search for.

        Returns:
            dict: A dictionary containing the topic, articles, and synthesized news.
        """
        self.reset_state()
        self.topic = topic
        try:
            articles = self.search_agent.search_news(topic)
            summary = self.synthesis_agent.synthesize_news(articles)
            self.results = {"topic": topic, "articles": articles, "summary": summary}
        except Exception as e:
            raise RuntimeError(f"Error in State: {str(e)}")
        return self.results