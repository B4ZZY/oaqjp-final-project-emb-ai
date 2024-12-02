"""
the starting file of the server. It serves API requests with the appropriate response
"""

from flask import Flask, render_template, request
#render_template function (from Flask library) deploys the HTML file
#requests funtion (also from Flask library) initialises GET requests from homepage
from EmotionDetection.emotion_detection import emotion_detector #import function to use

app = Flask("Emotion Detector") #Initializes the Flask app with the name "Emotion Detector"

@app.route("/emotionDetector")
def server_emotion_detector():
    """ a function that:
    #1. sends a GET request to the HTML interface to retrieve input text
    #2. stores incoming text to a variable
    """
    text_to_analyze = request.args.get('textToAnalyze') #retrieves text
    response = emotion_detector(text_to_analyze)
    #Pass the text to the emotion_detector function and store the response
    anger = response['anger'] #extract the score from the response
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"


    return (
        "For the given statement, the system response is "
        f"'anger':  {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}"
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    A function to run the render_template function on the HTML template, index.html
    upon file execution, run the application on host: 0.0.0.0 (or localhost) on port number 5000.
    """
    return render_template ('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
