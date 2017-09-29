import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
result = "https://www.spartan.com/en/race/detail/2620/results?fullResults=true"
page = urllib.request.urlopen(result)
#print(page.read())
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "html.parser")
print (soup.prettify())