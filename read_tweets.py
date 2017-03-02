import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret) 

api = tweepy.API(auth)

statuses = api.user_timeline()


tweets = api.user_timeline()
 
for tweet in tweets: 
    print(tweet.id, ": ", (tweet.text.encode("utf-8"))) 