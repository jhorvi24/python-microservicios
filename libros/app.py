#aplicación utilizando microservicios y flask para solicitar una lista de libros disponibles

from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)


@app.route('/')

def index():
    return "Listo para recibir una solicitud"
     
@app.route('/libros', methods=['GET'])
def libros():
    #Read the json file
    json_file = open('libros.json')
    data = json.load(json_file)    
    print(data['libros'][2])    
    return jsonify(data)

#Leer el id del archivo json

@app.route('/libros/<int:id>', methods=['GET'])
def libro(id):
    json_file = open('libros.json')
    data = json.load(json_file)
    print(data['libros'][id])     
    
    return jsonify(data['libros'][id])    
   
    
    
  
    
        
  
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    

