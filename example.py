import argparse

from disqusting.disqus import Disqus

parser = argparse.ArgumentParser()
parser.add_argument("api_key", help="Disqus API key")
parser.add_argument("forum", help="Short name of the forum")
parser.add_argument("url", help="Url of a post to view comments on")

args = parser.parse_args()

disq = Disqus(api_key=args.api_key, forum=args.forum)

# get all threads from a certain date
# threads = list(disq.list_threads(from_date=iso("2020-04-11T00:00:00")))


# get a single thread details
print(f"Forum {disq.forum} post {args.url}")
thread = disq.thread_details(args.url)
print(f"Total {thread['posts']} posts, {thread['likes']} likes")

# get all posts from a thread
for p in disq.thread_posts(args.url):
    print(f'- {p["author"]["name"]}: {p["raw_message"]}')