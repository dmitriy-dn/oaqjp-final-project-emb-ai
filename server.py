from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion detection')


@app.route('/emotionDetector')
def em_dtct():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion == None:
        return "Invalid text! Please try again!"

    answer = (
        "For this statement, the system responds with:\n"
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, and 'sadness': {}.\n "
        "The dominant emotion is {}"
    ).format(anger,
             disgust,
             fear,
             joy,
             sadness,
             dominant_emotion)

    return answer
