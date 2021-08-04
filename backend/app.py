import os
import json
import time

from flask import Flask, request, jsonify, abort
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    CORS(app)

    """
    CORS Headers
    after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,POST,PATCH,DELETE,OPTIONS')
        return response


    """
    Check if app is running
    """
    @app.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify("Healthy")


    """
    GET /api
    Get all registered store device types
    """    
    @app.route('/api', methods=['GET'])
    def get_devices():
        
        try:
   
            devices = {
                1: "Pfandautomat",
                2: "Waage"
            }
        
            return jsonify({
                "success": True,
                "device": devices
            })


        except BaseException:
            abort(422)

    """
    GET /api/pfandautomaten
    Get all available devices of type Pfandautomat in the store
    """    
    @app.route('/api/pfandautomaten', methods=['GET'])
    def get_pfandautomaten():
        
        try:
   
            pfandautomaten = {
                1: "P001",
                2: "P002",
                3: "P003"
            }
        
            return jsonify({
                "success": True,
                "pfandautomaten": pfandautomaten
            })


        except BaseException:
            abort(422)


    """
    GET /api/pfandautomaten/{id}
    Get all available services of specfific Pfandautomat with id
    """    
    @app.route('/api/pfandautomaten/<int:pfandautomat_id>', methods=['GET'])
    def get_pfandautomaten_services(pfandautomat_id):
        
        try:
   
            pfandautomat_services = {
                1: "Füllstand",
                2: "Störungen",
                3: "Wartungsaktivitäten"
            }
        
            return jsonify({
                "success": True,
                "pfandautomat_id": pfandautomat_id,
                "pfandautomat_services": pfandautomat_services
            })


        except BaseException:
            abort(422)


    """
    GET /api/pfandautomaten/{id}/füllstand
    Get füllstand of Pfandautomat with id
    """    
    @app.route('/api/pfandautomaten/<int:pfandautomat_id>/füllstand', methods=['GET'])
    def get_pfandautomaten_services_füllstand(pfandautomat_id):
        
        try:
   
            füllstand = "50%"
        
            return jsonify({
                "success": True,
                "pfandautomat_id": pfandautomat_id,
                "füllstand": füllstand
            })


        except BaseException:
            abort(422)



    """
    GET /api/waagen
    Get Get all available devices of type Waage in the store
    """    
    @app.route('/api/waagen', methods=['GET'])
    def get_waagen():
        
        try:

            waagen = {
                1: "W001",
                2: "W002"
            }
        
            return jsonify({
                "success": True,
                "waagen": waagen
            })


        except BaseException:
            abort(422)


    """
    GET /api/waagen/{id}
    Get all available services of specfific Waage with id
    """    
    @app.route('/api/waagen/<int:waage_id>', methods=['GET'])
    def get_waagen_services(waage_id):
        
        try:
   
            waage_services = {
                1: "Füllstand",
                2: "Störungen",
                3: "Wartungsaktivitäten"
            }
        
            return jsonify({
                "success": True,
                "waage_services": waage_services
            })


        except BaseException:
            abort(422)

        
    """
    GET /api/waagen/{id}/störungen
    Get Störungen of Waage with id
    """    
    @app.route('/api/waagen/<int:waage_id>/störungen', methods=['GET'])
    def get_waagen_services_störungen(waage_id):
        
        try:
   
            störungen = { 
                "Komponente":"Drucker",
                "Beschreibung":"Drucker ist defekt."
            }
        
            return jsonify({
                "success": True,
                "waage_id": waage_id,
                "störungen": störungen
            })


        except BaseException:
            abort(422)





    '''
    error handlers for aborts
    '''

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host = "0.0.0.0")

