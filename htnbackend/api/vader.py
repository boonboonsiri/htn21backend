from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def score_text(text):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)


def score_words(text):
    words = dict()
    sid =  SentimentIntensityAnalyzer()
    lst = text.split(' ')
    
    for x in lst:
        if x in words:
            continue
        else:
            words[x] = sid.polarity_scores(x)
    
    return words



