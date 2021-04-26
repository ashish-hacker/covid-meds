"""
This program is for building a twitter bot . Which can retweet and fav the tweets about COVID meds and essential items.
"""
# Import the necessary modules...
import tweepy
import time
import logging
from random import choice, randint
import sqlite3
import glob
import c

# For logging informations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#credentials
CONSUMER_KEY = c.ck
CONSUMER_SECRET = c.cs
ACCESS_KEY = c.ak
ACCESS_SECRET = c.ast

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# use this object to communicate with twitter
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
recent_id = c.recent_id

try:
    api.verify_credentials()
    logger.info("Authentication OK...")
except:
    logger.error("Error during authentication", exc_info=True)

def search():
    logger.info("Searching ...")
    date_since = c.recent_date
    date_since1 = c.recent_date1
    query = ["covid", "Remdesivir", "help"]
    tweets = tweepy.Cursor(api.search, query, count = 200, since = date_since).items(10)
    q = ["oxygen", "help"]
    tweets1 = tweepy.Cursor(api.search, q, count = 200, since = date_since1).items(10)
    for tweet in tweets:
        status = api.get_status(tweet.id)
        print("user's name: ", tweet.user.name, " ", tweet.created_at)
        c.recent_date = tweet.created_at
         # Like the tweet where it is tweeted(if not faved)
        if (not status.favorited) and (tweet.user.name != "art_ideas"):
            logger.info(f'Liking the tweet of {tweet.user.name}')
            try:
                tweet.favorite()
            except Exception as e:
                logger.error('Error while fav process .The error is :\n{}'.format(e), exc_info=True)    

        # Retweet the tweet which includes the hashtag(if not retweeted)
        if (not status.retweeted) and (tweet.user.name != "art_ideas"):
            logger.info(f'retweeting the tweet of {tweet.user.name}')
            try:
                tweet.retweet()
            except:
                logger.error('Error while retweeting.', exc_info=True)

    for tweet in tweets1:
        status = api.get_status(tweet.id)
        print("user's name: ", tweet.user.name, " ", tweet.created_at)
        c.recent_date1 = tweet.created_at
         # Like the tweet where it is tweeted(if not faved)
        if (not status.favorited) and (tweet.user.name != "art_ideas"):
            logger.info(f'Liking the tweet of {tweet.user.name}')
            try:
                tweet.favorite()
            except Exception as e:
                logger.error('Error while fav process .The error is :\n{}'.format(e), exc_info=True)    

        # Retweet the tweet which includes the hashtag(if not retweeted)
        if (not status.retweeted) and (tweet.user.name != "art_ideas"):
            logger.info(f'retweeting the tweet of {tweet.user.name}')
            try:
                tweet.retweet()
            except:
                logger.error('Error while retweeting.', exc_info=True)


while True:
    search()
    time.sleep(5)