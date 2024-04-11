import requests 
   
r = requests.get('https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,political,explicit&format=txt&type=single') 



print(r.text)










