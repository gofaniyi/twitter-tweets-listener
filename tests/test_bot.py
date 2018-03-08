import unittest
from bot import Bot

class BotTestCase(unittest.TestCase):

    def test_can_fetch_public_tweets(self):
        instance = Bot()
        public_tweets = instance.public_tweets()
        self.assertTrue(len(public_tweets) > 0)
