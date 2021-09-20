import requests
from bs4 import BeautifulSoup

URL = "https://www.feynmanlectures.caltech.edu/I_46.html"
# "https://www.sagedining.com/sites/ensworthschool/menu"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print (soup)