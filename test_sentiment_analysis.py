# run unit tests on some test cases to check the validity of its outputs

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

# create the unit test class
class TestSentimentAnalyzer(unittest.TestCase):
    # function to run the unit tests
    def test_sentiment_analyzer(self):
        # Test case for positive sentiment
        result_1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result_1["label"], "SENT_POSITIVE")
        # test case for negative sentiment
        result_2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result_2["label"], "SENT_NEGATIVE")
        # test case for neutral sentiment
        result_3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result_3["label"], "SENT_NEUTRAL")

# call the unit test
unittest.main()