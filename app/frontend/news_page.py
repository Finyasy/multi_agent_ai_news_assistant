import reflex as rx

def news_page(state):
    """
    Defines the user interface for the news assistant

    Args:
        state (State): The state object managing the workflow.

    Returns:
        reflex.container: The reflex UI container.
    """

    return rx.container(
        [
            rx.input(
                placeholder="Enter a topic to search for...",
                on_change=lambda text: state.process_news(text),
            ),

            rx.button(
                "Process News",
                on_click=lambda: state.process_news(state.current_topic),
                loading_indicator=True,
            ),

            rx.text(
                f"summary: {state.results.get('summary', 'Enter a topic to search for...')}"
            ),
        ]
    )