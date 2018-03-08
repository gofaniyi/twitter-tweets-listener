import tweepy
import os
import re
from spreadsheets import GoogleSpreadSheets

twitter_consumer_key = os.getenv("TWITTER_CONSUMER_KEY", "")
twitter_consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET", "")
twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN", "")
twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "")


def initializeCredentials():

    if not all([twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret]):
        raise ValueError('You need to set the Twitter Credentials')

    authentication = tweepy.OAuthHandler(
                        twitter_consumer_key,
                        twitter_consumer_secret)
    authentication.set_access_token(
                        twitter_access_token,
                        twitter_access_token_secret)

    return authentication

class Bot(object):

    def __init__(self):
        authentication = initializeCredentials()
        self.api = tweepy.API(authentication)

    def public_tweets(self):
        return self.api.home_timeline()



class BotStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        followers_count = status.user.followers_count
        data={'Profile name' : username, 'Number of followers' : followers_count}

        GoogleSpreadSheets().write(filename='Twitter Bot', data=data)

        for key in ['Profile name', 'Number of followers']:
            value = data[key]
            print(f'[*] {key}: {value}')
        print('-' * 100)

if __name__ == "__main__":
    text = input("[+] Enter each hastag separated by comma or space: ")
    tags = re.findall(r"[\w']+", text)
    #Add hastag symbol to inputs without the symbol.
    hastags = ["#" + tag if '#' not in tag else tag for tag in tags]
    if hastags:
        authentication = initializeCredentials()
        myStreamListener = BotStreamListener()
        stream = tweepy.Stream(authentication, myStreamListener)
        print(f'[-] Filter stream based on the following hastags : {hastags}')
        print('-' * 100)
        stream.filter(track=hastags)
