import tweepy
import os
import re

twitter_consumer_key = os.getenv("TWITTER_CONSUMER_KEY", "")
twitter_consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET", "")
twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN", "")
twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "")

authentication = tweepy.OAuthHandler(
                    twitter_consumer_key,
                    twitter_consumer_secret)
authentication.set_access_token(
                    twitter_access_token,
                    twitter_access_token_secret)
api = tweepy.API(authentication)

class Bot(object):

    def public_tweets(self):
        return api.home_timeline()



class BotStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        followers_count = status.followers_count


if __name__ == "__main__":
    myStreamListener = BotStreamListener()
    stream = tweepy.Stream(authentication, myStreamListener)
    stream.filter(track=['#jesusislord'])
