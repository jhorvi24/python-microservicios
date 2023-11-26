#servicio web para mostrar información sobre autores de libros

from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify("Listo para recibir una solicitud")

@app.route('/autores')
def autores():
    json_file = open('autores.json')
    data = json.load(json_file)   
    return jsonify(data), 200

#Leer el id del archivo json
@app.route('/autores/<int:id>', methods=['GET'])
def reviewID(id):
    with open('autores.json') as json_file:
        data = json.load(json_file)        
    rev=data['users']  
    for i in rev:        
        if i["id"]==id:
            return jsonify(i)        
    return jsonify("No se encotró el autor")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)