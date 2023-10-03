import json
from textblob import TextBlob

def lambda_handler(event, context):
    article = event['body']
    blob = TextBlob(article)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.05:
        result = "positive"
    elif sentiment < -0.05:
        result = "negative"
    else:
        result = "neutral"

    response = {
        "sentiment": result,
        "polarity": sentiment
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
