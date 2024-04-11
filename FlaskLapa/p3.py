from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt&type=single")
    if response.status_code == 200:
        data = response.json()
        joki = data['value']
        return render_template('p3.html', joke=joki)
    else:
        return "Nevar saņemt joku"

if __name__ == '__main__':
    app.run(debug=True)
