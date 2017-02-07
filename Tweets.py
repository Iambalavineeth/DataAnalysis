import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
 
consumer_key = '0NkHawj0dWMQRtWK7HaHOut1w'
consumer_secret = 'eBeSwKj0t49DiryQNclbf0FiG1TnO59JmrM8y15U5AkLYnrk1c'
access_token = '779852978048032768-ldAnwI2g0vME6hflDzkNSJDz0F5AUJO'
access_secret = 'nMSTNyJbbtvCuXsrinQo6i7jOqJa2Yjk9sIsZv7SmPCPf'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('ClemVSCuse.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error occured "+str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 

while True:
	try:
		twitter_stream = Stream(auth, MyListener())
		twitter_stream.filter(track=['Dabo', 'Dabo Swinney',  'dabo', 'Deshaun Watson', 'Deshaun', 'deshaun', 'Clemson Tigers', 'clemson tigers', 'Clemson Football', 'clemson football', 'ClemsonFB','#clemson', '#Clemson', 'Dino Babers', 'Dino', 'dino','Eric Dungey', 'Eric', 'eric', 'Syracuse Football', 'syracuse football', 'CuseFootball', '#CUSEvsCLEM', '#CLEMvsCUSE'])
	except IncompleteRead:
		print ("Try again once!")
		continue
	except KeyboardInterrupt:
		stream.disconnect()
		break