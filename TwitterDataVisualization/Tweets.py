import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = '<consumer key from twitter>'
consumer_secret = '<consumer secret key from twitter>'
access_token = '<twitter account access keytoken>'
access_secret = '<twitter account access secret keytoken>'

# Authenticating and Connecting to Twitter API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Twitter StreamListener
class MyListener(StreamListener):
    # On Getting Twitter Stream Data
    def on_data(self, data):
        try:
            # Writing into JSON File
            with open('ClemVSCuse.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error occured "+str(e))
        return True

    # On error show the error message
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
