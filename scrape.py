from typing import Any
import praw
import os


class Obj:
    def __init__(self, client_id, secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id, client_secret=secret, user_agent=user_agent)

    def getRandomSubmission(self, difficulty: str) -> object:
        sub = None
        while True:
            submission = self.reddit.subreddit("dailyprogrammer").random()

            title = submission.title

            if "Challenges" in title:
                continue

            if "Challenge" in title and difficulty in title:
                sub = submission
                break
        return sub

    def getFileName(self, sub: Any) -> str:
        left = sub.title.split("#")[1]
        res = ""
        for char in left:
            if char == " ":
                break
            res += char

        return "Q#" + res

    def createFile(self, sub) -> None:
        file_name = self.getFileName(sub)
        with open(file_name + ".md", "w") as f:
            f.write("# "+sub.title + "\n")
            f.write(sub.selftext)
