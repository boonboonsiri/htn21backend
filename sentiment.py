# Sentiment Analyzer   
from afinn import Afinn
af = Afinn()


def score_sentiment(data):

    lst = data.split(' ')
    total = 0
    n = 0

    for x in lst:
        total += af.score(x)
        n += 1

    print(total / n)
    sentiment_scores = [af.score(x) for x in lst]
    return sentiment_scores


