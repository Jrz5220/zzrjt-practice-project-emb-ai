# NLP sentiment analysis is the practice of using computers to recognize sentiment or emotion expressed in text.
# Through NLP, sentiment analysis categorizes words as positive, negative, or neutral.
# Sentiment analysis helps businesses monitor brand and product sentiment in customer feedback.
# We'll be using Watson Embedded AI libraries to create a sentiment analysis application.
# We do not need to import these libraries into our code since they are already deployed on the Cloud IDE server, which is the IDE we are using for this project.

import requests  # handles HTTP requests
import json # formatting JSON data

# function for running sentiment analysis using the Watson NLP Bert Sentiment Analysis function
def sentiment_analyzer(text_to_analyse):
    # url of the sentiment analysis service
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    # dictionary with text to be analyzed
    myobj = { "raw_document": {"text": text_to_analyse} }
    # set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers = header)
    # the response from the API is an object with an attribute of 'text' containing the response details.
    # 'text' returns a nested dictionary (dictionary of dictionaries) formatted as a string.
    # format the response from the API as JSON
    formatted_response = json.loads(response.text)
    # extract the label and score values from the response
    label = formatted_response["documentSentiment"]["label"]
    score = formatted_response["documentSentiment"]["score"]
    # return the response text from the API
    return { "label": label, "score": score }

