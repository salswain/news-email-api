import requests
from send_email import send_email

api_key = "1cf316e28b1a4c76ada6e2b585356e1c"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&" \
      "apiKey=1cf316e28b1a4c76ada6e2b585356e1c"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content ["articles"]:
      if article["title"] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)



