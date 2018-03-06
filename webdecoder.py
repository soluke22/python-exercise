#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'http://nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for heading in soup.findAll(class_="story-heading"):
  if heading.a:
    print (heading.a.text.replace("\n", " ").strip())
  else:
    print(heading.contents[0].strip())
