import praw
import json
import io

from google.protobuf.json_format import MessageToJson


# client_secret = 'iZ4jVxCsMgiqPu8nhUOFUOGX9yHeSA'
# user_agent = 'monologProject'
# client_id = 'b_WeKBW7ylvocu1a39SYzw'

# Crawling Definition
def crawl(arg1, user_agent=None, client_secret=None, client_id=None, page_limit=None):
    outfile = open('result.json', 'w')
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    hot_posts = reddit.subreddit(arg1).hot(limit=page_limit)
    data = {
        'counts_comment': [],
        'score': [],
        'title': [],
        'selftext': [],
    }
    for post in hot_posts:
        data['counts_comment'].append(post.num_comments)
        data['score'].append(post.score)
        data['title'].append(post.title)
        data['selftext'].append(post.selftext)
        print(data)
        print("SAVED DATA RESULT JSON FILE!")
    json.dump(data, outfile)


# Main
def main():
    arg1 = str(input("Enter a word for reddit seaching:"))
    page_limit = str(input("Enter page limit:"))
    client_secret = str(input("Enter secret key reddit api:"))
    user_agent = str(input("Enter user_agent key reddit api:"))
    client_id = str(input("Enter client_id key reddit api:"))
    crawl(arg1, user_agent, client_secret, client_id, page_limit)


main()
