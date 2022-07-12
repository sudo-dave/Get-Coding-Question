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
        self.reddit = r

    def getRandomSubmission(self, lvl=""):
        sub = None
        while True:
            submission = self.reddit.subreddit("dailyprogrammer").random()

            title = submission.title

            if "Challenges" not in title and lvl in title and "Challenge" in title:
                sub = submission
                break
        return sub

    def getFileName(self, sub):
        left = sub.title.split("#")[1]
        res = ""
        for char in left:
            if char == " ":
                break
            res += char

        return "Q#" + res

    def createFile(self, sub):
        file_name = self.getFileName(sub)
        with open(file_name + ".md", "w") as f:
            f.write("# "+sub.title + "\n")
            f.write(sub.selftext)
