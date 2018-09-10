import os
import twitter

TwitApi = twitter.Api(consumer_key=os.environ.get('CONSKEY'),
consumer_secret=os.environ.get('CONSCRT'),
access_token_key=os.environ.get('ACSKEY'),
access_token_secret=os.environ.get('ACSSCRT'))