from textblob import TextBlob

with open("preprocessed_articles.txt", "r") as file:
    preprocessed_articles = file.readlines()


article_sentiments = []

for article in preprocessed_articles:
    blob = TextBlob(article)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.05:
        sentiment = "positive"
    elif polarity < -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    article_sentiments.append((sentiment, polarity, subjectivity))


for i in range(10):
    sentiment, polarity, subjectivity = article_sentiments[i]
    print(f"Article {i+1} Sentiment: {sentiment} (Polarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f})")
