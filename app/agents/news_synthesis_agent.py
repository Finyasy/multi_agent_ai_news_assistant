class NewsSynthesisAgent:
    def __init__(self, model):
        self.name = "News Synthesis Agent"
        self.model = model

    def synthesize_news(self, articles):
        """
        Synthesizes a concise summary from multiple news articles.

        Args:
            articles (list): A list of summaries.

        Returns:
            str: A single synthesized summary.
        """
        if not articles:
            raise ValueError("No articles to synthesize")
        
        combined_text = "\n".join([article["summary"] for article in articles])
        prompt = f"Summarize the following news articles:\n\n{combined_text}"
        
        try:
            return self.model.generate(prompt, max_length=100)[0]["generated_text"]
        except Exception as e:
            raise RuntimeError(f"Error in News Synthesis Agent: {str(e)}")