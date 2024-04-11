from bs4 import BeautifulSoup
import requests

url = "https://www.delfi.lv/"

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

headlines = soup.find_all(class_='headline')

print("Virsraksti: ")
for headline in headlines:
    print(headline.text.strip())