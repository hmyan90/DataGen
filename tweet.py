from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

access_token = "953767787255574528-8RMQvZN4cepfdMpe11e3KGNn01OBA72"
access_token_secret = "4JlLPqgUTM108ja2Q5kO0rc4KptlwL1DSfpTQVqEKSE9d"
consumer_key = "7rV3VEWDUfbiYWP1mm55lK9Jx"
consumer_secret = "4kXLQmUPCcu9NPJE8k7j7gLHXTgagqnxepIR65vH4EksYeTD0m"

class StdoutListener(StreamListener):
    def on_data(self, data):
        try:
            savefile = open("tw_data.txt", "a")
            savefile.write(data)
            #savefile.write("\n")
            savefile.close()
            return True
        except BaseException as e:
            time.sleep(5)

    def on_error(self, status):
        print (status)


if __name__ == "__main__":
    l = StdoutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=["salesforce", "javascript", "python"])
