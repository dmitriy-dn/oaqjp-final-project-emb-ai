import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_emotion = emotion_detector("I'm pleased that this happened")
        self.assertEqual(test_emotion, 'joy')

        test_emotion = emotion_detector("I'm really angry about this")
        self.assertEqual(test_emotion['dominant_emotion'], 'anger')

        test_emotion = emotion_detector("I'm disgusted just hearing about it")
        self.assertEqual(test_emotion['dominant_emotion'], 'disgust')

        test_emotion = emotion_detector("I'm very sad about this")
        self.assertEqual(test_emotion['dominant_emotion'], 'sadness')

        test_emotion = emotion_detector("I'm really afraid that this will happen")
        self.assertEqual(test_emotion['dominant_emotion'], 'fear')

unittest.main()
