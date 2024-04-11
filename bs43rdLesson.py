from bs4 import BeautifulSoup
import requests

url = "https://www.delfi.lv/"

res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')

title = soup.find("title")

print(title.text)