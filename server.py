"""This module starts the Flask server for the Emotion Detector app."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion detection')


@app.route('/emotionDetector')
def em_dtct():
    """Processes text input and returns the detected emotions."""

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    answer = (
    f"For this statement, the system responds with:\n"
    f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
    f"'joy': {joy}, and 'sadness': {sadness}.\n"
    f"The dominant emotion is {dominant_emotion}"
)

    return answer

@app.route("/")
def render_index_page():
    """Start with template"""

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
