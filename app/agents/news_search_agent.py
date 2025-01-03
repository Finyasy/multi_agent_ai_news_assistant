import logging
from duckduckgo_search import DDGS
from datetime import datetime

class NewsSearchAgent:
    def __init__(self):
        self.name = "News Search Agent"

    def fetch_latest_news(self, topic):
        """
        Fetches up to 3 news articles from DuckDuckGo for the given topic.

        Args:
            topic (str): The topic to search for.

        Returns:
            str: Formatted string of news articles.
        """
        try:
            query = f"{topic} news {datetime.now().strftime('%Y-%m')}"
            logging.debug(f"Searching for topic: {query}")

            with DDGS() as search_engine:
                results = search_engine.text(query, max_results=3)
                logging.debug(f"Raw results from DuckDuckGo: {results}")

                if not results:
                    raise RuntimeError("No results returned from DuckDuckGo")

                formatted_results = "\n\n".join(
                    f"Title: {result['title']}\nURL: {result['href']}\nSummary: {result['body']}"
                    for result in results
                )
                return formatted_results

        except Exception as e:
            error_msg = f"Error in News Search Agent: {str(e)}"
            logging.error(error_msg)
            raise RuntimeError(error_msg)

# Test the fetch_latest_news function
if __name__ == "__main__":
    agent = NewsSearchAgent()
    print(agent.fetch_latest_news("test search"))