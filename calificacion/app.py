#aplicación utilizando flask que hace parte de una tienda de libros para solicitar un libro para compra 

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify("Listo para recibir una solicitud")
     
@app.route('/review', methods=['GET'])
def review():
    #Read the json file
    json_file = open('calificacion.json')
    data = json.load(json_file)          
    return jsonify(data), 200
    


#Leer el id del archivo json
@app.route('/review/<int:id>', methods=['GET'])
def reviewID(id):
    with open('calificacion.json') as json_file:
        data = json.load(json_file)        
    rev=data['reviews']  
    for i in rev:        
        if i["id"]==id:
            return jsonify(i)        
    return jsonify("No se encotró el libro")
      
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    