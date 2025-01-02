from duckduckpy import query as ddg_query

class NewsSearchAgent:
    def __init__(self):
        self.name = "News Search Agent"

    def search_news(self, topic):
        """
        Fetches up to 3 news articles from DuckDuckGo for the given topic.

        Args:
            topic (str): The topic to search for.

        Returns:
            list: A list of dictionaries containing the title,URL and summary.
        """
        try:
            response = ddg_query(topic,max_results=3)
            articles = response.get("results", [])
            return [
                {
                    "title": article.get("title", ""),
                    "url": article.get("url", ""),
                    "summary": article.get("description", "")
                }
                for article in articles
            ]
        except Exception as e:
            raise RuntimeError(f"Error in News Search Agent: {str(e)}")