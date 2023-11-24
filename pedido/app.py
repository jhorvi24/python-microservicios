#aplicación utilizando flask que hace parte de una tienda de libros para solicitar un libro para compra 

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return "Inicio"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=6000 )
