import praw

r = praw.Reddit(
    client_id="BjNgO8Rdn6HXC4mWexLViw", client_secret="n91DK-oJrcP4Yy9Nj997qTYpaaj9lQ", user_agent="Code_Scrape")

for sub in r.subreddit("dailyprogrammer").search("title:Intermediate AND title:#", limit=None):
    print(sub.title)
