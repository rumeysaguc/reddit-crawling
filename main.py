import praw
import json
import io

from google.protobuf.json_format import MessageToJson

# Crawling Definition
def crawl(arg1, user_agent=None, client_secret=None, client_id=None, page_limit=None):
    outfile = open('result.json', 'w')
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    hot_posts = reddit.subreddit(arg1).hot(limit=10)
    for post in hot_posts:
        data = {
            'counts_comment': post.num_comments,
            'score': post.score,
            'title': post.title,
            'selftext': post.selftext,
        }
        print(data)
        json.dump(data, outfile)


# Main
print("Enter a word for reddit seaching:")
arg1 = str(input())
# print("Enter secret key reddit api:")
# client_secret = str(input())

client_secret = 'iZ4jVxCsMgiqPu8nhUOFUOGX9yHeSA'
user_agent = 'monologProject'
client_id = 'b_WeKBW7ylvocu1a39SYzw'
crawl(arg1, user_agent, client_secret, client_id)
