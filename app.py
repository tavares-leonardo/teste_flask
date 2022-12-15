from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello Mundo!</h1>'

@app.route('/posicao')
def posicao():
  return '<h1>Posicao!</h1>'

app.run()

