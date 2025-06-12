def get_book_recommendation(topic_or_genre=None):
    # TODO: Integrate with an AI API or a curated book list
    if topic_or_genre:
        return f"Book on {topic_or_genre}: 'AI 2041' by Kai-Fu Lee"
    return "General AI Book: 'Life 3.0' by Max Tegmark"