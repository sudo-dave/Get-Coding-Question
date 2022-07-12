from operator import sub
import praw
from dotenv import load_dotenv
import os


class Obj:
    def __init__(self) -> None:
        load_dotenv()

        self.client_id = os.getenv("client_id")
        self.secret = os.getenv("secret")
        self.user_agent = os.getenv("user_agent")
        r = praw.Reddit(
            client_id=self.client_id, client_secret=self.secret, user_agent=self.user_agent)
        # self.reddit = r.subreddit("dailyprogrammer")
        self.reddit = r

    def getRandomChallenge(self):
        sub = None
        while True:
            submission = self.reddit.subreddit("dailyprogrammer").random()
            if submission and "Challenges" not in submission and "Challenge" in submission:
                sub = submission
                break
