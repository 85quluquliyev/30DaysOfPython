import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/'

response = requests.get(url)
status = response.status_code
print(status)