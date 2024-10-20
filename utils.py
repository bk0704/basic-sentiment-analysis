# utils.py
def aggregate_sentiment(sentiment_scores):
    """
    Aggregate the sentiment scores to calculate the overall sentiment for the server.
    :param sentiment_scores: A list of sentiment scores (floats)
    :return: The average sentiment score
    """
    if not sentiment_scores:
        return 0
    return sum(sentiment_scores) / len(sentiment_scores)