import tweepy

  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret) 
 

 
api = tweepy.API(auth)
 
api.update_status(status="Tweet depuis tweepy.)")