from flask import Flask, Response, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime
import time
import requests
import html 
# importi

app = Flask(__name__, static_url_path="/static") # static lai varētu ielikt bildes html un styles css
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/borabora')
def borabora():
   return render_template('borabora.html')
@app.route('/maui')
def maui():
   return render_template('maui.html')
@app.route('/kreta')
def kreta():
   return render_template('kreta.html')
@app.route('/kapri')
def kapri():
   return render_template('kapri.html')
@app.route('/palavana')
def palavana():
   return render_template('palavana.html')
@app.route('/fernando')
def fernando():
   return render_template('fernando.html')
@app.route('/bali')
def bali():
   return render_template('bali.html')
@app.route('/time_feed') # laiks kas rādās labajā augšā, dažiem lietotājiem tas var noderēs priekš ērtības
def time_feed():
    def generate():
        yield datetime.now().strftime("Tagadējais laiks: <br>Datums: %Y.%m.%d <br> Laiks: %H:%M:%S")  
    return Response(generate(), mimetype='text')
if __name__ == '__main__': 
    app.run(debug=True)








