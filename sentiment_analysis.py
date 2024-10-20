import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()



def analyze_sentiment(message_content):
    """
    Analyze the sentiment of a message using VADER and return the compound score.
    :param message_content: The text content of the message
    :return: The compound sentiment score between -1 (negative) and +1 (positive)
    """
    sentiment_dict = analyzer.polarity_scores(message_content)
    return sentiment_dict['compound']  # Return only the compound score