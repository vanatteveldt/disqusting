# A disqusting API library

Very simple and incomplete (but easily expandable) library for interacting with Discqus API

# Installing

```
pip install disqusting
```

# Usage

First, [create a disqus account, app, and get the API key](https://help.disqus.com/en/articles/1717083-how-to-create-an-api-application).

Next, install `disqusting` as above and use it like this:

```
disq = Disqus(api_key=API_KEY, forum=FORUM_SHORT_NAME)
for thread in disq.list_threads(max_n=5):
  print(thread['link'])
```

See [example.py](example.py) for another example
