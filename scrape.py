from typing import Any
import praw
import random


class Obj:
    def __init__(self, client_id, secret, user_agent):
        reddit = praw.Reddit(
            client_id=client_id, client_secret=secret, user_agent=user_agent)
        self.r = reddit.subreddit("dailyprogrammer")

    def getRandomSubmissions(self, difficulty: str, count: int) -> object:
        query = "title:" + difficulty
        submissions = []
        for submission in self.r.search(query, limit=None):
            submissions.append(submission)
        return random.sample(submissions, count)

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
