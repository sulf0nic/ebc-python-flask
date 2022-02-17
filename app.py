from crypt import methods
from flask import Flask, request, render_template

#Inicializar
app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("Index.html")
    #return "<a href='#'>Hello Word Flask :))</a>"
    #return "<h1>hello world flask</h1>"
    #return "<a href='#'>hello world flask</a>"

@app.route("/ebc")
def HolaEBC():
  return "Hola ebc"

@app.route("/ebc/random")
def UnGetRandom():
  return "Hola ebc/Random"

##@app.route("/", methods=['POST'])
##def AddNewTask():
##    if request.method == 'POST':

if __name__ == "__main__":
  app.run(port=5000, debug=True)