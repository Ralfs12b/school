from bs4 import BeautifulSoup

# HTML kods

html_code = "<html><body><h1><Hello, World!></h1><body>"

soup = BeautifulSoup(html_code, 'html.parser')

text = soup.h1.text

print('Teksts:', text)