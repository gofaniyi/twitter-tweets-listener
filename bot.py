import tweepy
import re
from credentials import TwitterCredentials


twitter_cred = TwitterCredentials()
authentication = tweepy.OAuthHandler(
                    twitter_cred.consumer_key,
                    twitter_cred.consumer_secret)
authentication.set_access_token(
                    twitter_cred.access_token,
                    twitter_cred.access_token_secret)
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
