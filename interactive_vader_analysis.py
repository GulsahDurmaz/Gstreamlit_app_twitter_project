# interactive_vader_analysis.py
from imports import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment using VADER
def analyze_sentiment(tweet):
    sentiment_score = analyzer.polarity_scores(tweet)
    # Extracting the 'compound' score which tells overall sentiment
    score = sentiment_score['compound']
    if score >= 0.05:
        return "Positive", score
    elif score <= -0.05:
        return "Negative", score
    else:
        return "Neutral", score

