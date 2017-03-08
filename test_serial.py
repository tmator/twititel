import serial
import tweepy
import time



api = tweepy.API(auth)

ser = serial.Serial('COM9', 9600, timeout=1)

while 1:
 try:
  tweet = ser.readline()
  if len(tweet) > 0:
    print(str(tweet))
    api.update_status(status=tweet)
  
 except ser.SerialTimeoutException:
  print('Data could not be read')
  
  
  
  

 

 

 
