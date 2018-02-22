import requests
import json

uri = 'https://westeurope.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'
accessKey = 'ab1d0fb6173c434eaab22e9acbc38450'

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    body = json.dumps (documents)
    response = requests.post(uri+path, data=body, headers=headers)
    return json.loads(response.text)

def get_emotion(msg):
    documents = {'documents': [
        {'id': '1', 'language': 'en',
         'text': msg}
    ]}
    result = GetSentiment(documents)
    if result['documents'][0]['score'] > 0.55:
        return 'pleased'
    elif result['documents'][0]['score'] < 0.45:
        return 'unpleased'
    else:
        return 'neutral'