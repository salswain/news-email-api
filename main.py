import requests

api_key = "1cf316e28b1a4c76ada6e2b585356e1c"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&" \
      "apiKey=1cf316e28b1a4c76ada6e2b585356e1c"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content ["articles"]:
      print(article["title"])
      print(article["description"])


