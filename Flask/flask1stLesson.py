from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello world"

@app.route('/user')
def hello_world2():
   return "Sup"

@app.route('/admin')
def hello_world3():
   return "Sveiks, admin"

@app.route('/user/<name>')
def hello_user(name):
   return "Sveiks, admin" + str(name)

@app.errorhandler(404)
def error(error):
   return "Saite nepareiza"


app.run()