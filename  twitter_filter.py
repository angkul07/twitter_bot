import tweepy
import keys

client = tweepy.Client(consumer_key=keys.api_key, consumer_secret=keys.api_secret, access_token=keys.access_token, access_token_secret=keys.access_token_secret)

auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)

api = tweepy.API(auth)
client.create_tweet(text="after trying countless time, finally I was able to use X api to work (btw this is tweeted with X api)")
