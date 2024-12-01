import requests #library to send POST requests to NLP library
import json #library to convert json stuff

#a function that takes input text, sends to NLP lib and returns the emotions
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #the url of the emotion detection service that the post request is sent to
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #headers necessary for the API request
    myobj = { "raw_document": { "text": text_to_analyze } }  
    # Create a dictionary with the text to be analyzed
    response = requests.post(url, json = myobj, headers = headers)  
    #Send a POST request to the API with the text and headers

    #convert response text into a dictionary
    formatted_response = json.loads(response.text)

    #extracting emotions from the dictionary named emotionPredictions
    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    
    #express emotions as a list & calculate dominant emotion
    emotions = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
    #max() finds highest emotion value, index() finds the position of this highest emotion
    #then, only the index number of the max emotion is stored in the variable
    dominant_emotion_index = emotions.index(max(emotions))
    #creates a new list of keys in the same order as the emotions[] list
    emotions_keys = ["anger", "disgust", "fear", "joy", "sadness"]
    #uses the index found earlier to access the right emotion from the list of keys
    dominant_emotion_key = emotions_keys[dominant_emotion_index]


    return{
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        #the key name corresponding to the dominant emotion found earlier
        'dominant_emotion': dominant_emotion_key
    }


