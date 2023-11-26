#aplicación utilizando microservicios y flask para solicitar una lista de libros disponibles

from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify("Esperando recibir una solicitud")
     
     
@app.route('/libros', methods=['GET'])
def libros():
    #Read the json file
    json_file = open('libros.json')
    data = json.load(json_file)       
    return jsonify(data), 200

#Leer el id del archivo json
@app.route('/libros/<int:id>', methods=['GET'])
def reviewID(id):
    with open('libros.json') as json_file:
        data = json.load(json_file)        
    rev=data['libros']  
    for i in rev:        
        if i["book-id"]==id:
            return jsonify(i)        
    return jsonify("No se encotró el libro")  
   

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    

