#Microservicios para implementar una tienda de libros online utilizando el framework flask

from flask import Flask, jsonify

@app.route('/')

def index():
    return jsonify({'message': 'Hola mundo'})

@app.route('/books')

def books():
    return jsonify({'books': ['El señor de los anillos', 'El hobbit']})
   
if __name__ == '__main__':
    app.run(debug=True)
     
