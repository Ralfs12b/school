import requests


url = input("Ielieciet saiti: ")

r = requests.get(url)

if r.status_code == 200:
    print("Dotais url ir labs")
else:
    print("Dotais url is slikts")