import tweepy, time, auth, Beep

# start api session
CONSUMER_KEY = auth.CONSUMER_KEY
CONSUMER_SECRET = auth.CONSUMER_SECRET
ACCESS_KEY = auth.ACCESS_KEY
ACCESS_SECRET = auth.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


class TwitterFeed:

    def __init__(self, screen_name, current_id=0):

        self.screen_name = screen_name
        self.current_id = current_id
        self.current_status = None

    def get_new_status(self):
        new_status = api.user_timeline(id=self.screen_name, count=1)[0]
        new_id = new_status.id
        if new_id > self.current_id:
            self.current_id = new_id
            self.current_status = new_status
            # TODO remove print statement
            print(new_status.text)
            Beep.beep(duration=1)
            return new_status
        else:
            return None


def main():

    CNN_feed = TwitterFeed('CNN')

    while True:
        CNN_feed.get_new_status()
        time.sleep(30)


if __name__ == "__main__":
    main()
