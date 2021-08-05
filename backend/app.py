from flask import Flask, request, jsonify, abort, url_for
from flask_cors import CORS
import urllib
import re
import json

#from manage import list_routes

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
            'GET,POST,OPTIONS')
        return response


    """
    function to get API routes/endpoints
    """

    def list_routes(prefix):
        links = []
        for rule in app.url_map.iter_rules():
            methods = ','.join(rule.methods)
            line = urllib.parse.unquote("{}".format(rule))
            if line.startswith(prefix):
                links.append(line)

        return links  

    """
    Check if app is running
    """
    @app.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify("Healthy")


    """
    GET /api
    Get all registered store device types
    [1st level -> Starting point for the Chatbot]
    """

    @app.route("/api")
    def get_devices():
        try:
            links = list_routes("/api") 
            device_types = []         

            # only return routes for device types (1st level)
            for link in links:
                level_number = link.count('/')
                if level_number == 2:
                    device_types.append(link)

            return jsonify({
                "success": True,
                "device_types": device_types
            })

        except BaseException:
            abort(422)



    # Pfandautomat

    """
    GET /api/pfandautomaten
    Get all available devices of type Pfandautomat in the store
    [2nd level]
    """    
    @app.route('/api/pfandautomaten', methods=['GET'])
    def get_pfandautomaten():
        
        try:

            json_dummy = [  
                { 
                    "id": 1, 
                    "name" : "Einwegautomat P001",
                    "link" : "/api/pfandautomaten/1"
                },
                { 
                    "id": 2, 
                    "name" : "Mehrwegautomat P002",
                    "link" : "/api/pfandautomaten/2"
                },
                { 
                    "id": 3, 
                    "name" : "Mehrwegautomat P003",
                    "link" : "/api/pfandautomaten/3"
                } 
            ]

            pfandautomaten = json_dummy

            devices = [] 

            """
            for pfandautomat in pfandautomaten:
                device = []
                device_link = "/api/pfandautomaten/{}".format(pfandautomat["id"])
                device_name = pfandautomat["name"]

                device = [device_link , device_name]
                print(device)
                devices.append(device)
            """

            devices = pfandautomaten 

            return jsonify({
                "success": True,
                "device_type": "Pfandautomat",
                "devices": devices
            })


        except BaseException:
            abort(422)


    """
    GET /api/pfandautomaten/{id}
    Get all available services of specfific Pfandautomat with id
    [3rd level]
    """  
    @app.route('/api/pfandautomaten/<int:pfandautomat_id>', methods=['GET'])
    def get_pfandautomaten_services(pfandautomat_id):
        
        try:

            links = list_routes("/api/pfandautomaten/<int:pfandautomat_id>/")        
            services = []

            # only return routes for services of corresponding device from device type pfandautomat (3rd level)
            for link in links:
                level_number = link.count('/')
                if level_number == 4:
                    link = link.replace("<int:pfandautomat_id>",str(pfandautomat_id))
                    services.append(link)
            

            return jsonify({
                "success": True,
                "device_id": pfandautomat_id,
                "device_type": "Pfandautomat",
                "services": services
            })

        except BaseException:
            abort(422)


    """
    GET /api/pfandautomaten/{id}/füllstand
    Get füllstand of Pfandautomat with id
    [4th Level]
    """    
    @app.route('/api/pfandautomaten/<int:pfandautomat_id>/füllstand', methods=['GET'])
    def get_pfandautomaten_services_füllstand(pfandautomat_id):
        
        try:
   
            füllstand = "50%"
        
            return jsonify({
                "success": True,
                "device_id": pfandautomat_id,
                "device_type": "Pfandautomat",
                "füllstand": füllstand
            })


        except BaseException:
            abort(422)

    """
    GET /api/pfandautomaten/{id}/störungen
    Get störungen of Pfandautomat with id
    [4th Level]
    """    
    @app.route('/api/pfandautomaten/<int:pfandautomat_id>/störungen', methods=['GET'])
    def get_pfandautomaten_services_störungen(pfandautomat_id):
        
        try:
   
            störungen = { 
                "Komponente":"Band",
                "Beschreibung":"Flascheneinfuhrband läuft nicht mehr."
            }
            return jsonify({
                "success": True,
                "device_id": pfandautomat_id,
                "device_type": "Pfandautomat",
                "störungen": störungen
            })


        except BaseException:
            abort(422)



    # Waage

    """
    GET /api/waagen
    Get Get all available devices of type Waage in the store
    [2nd level]
    """    
    @app.route('/api/waagen', methods=['GET'])
    def get_waagen():
        
        try:

            json_dummy = [  
                { 
                    "id": 1, 
                    "name" : "Obstwaage P001",
                    "link" : "/api/waagen/1"
                },
                { 
                    "id": 2, 
                    "name" : "Gemüsewaage P002",
                    "link" : "/api/waagen/2"
                }
            ]

            waagen = json_dummy

            devices = [] 
            devices = waagen

            return jsonify({
                "success": True,
                "device_type": "Waage",
                "devices": devices
            })
        except BaseException:
            abort(422)


    """
    GET /api/waagen/{id}
    Get all available services of specfific Waage with id
    [3rd level]
    """    
    @app.route('/api/waagen/<int:waage_id>', methods=['GET'])
    def get_waagen_services(waage_id):
        
        try:

            links = list_routes("/api/waagen/<int:waage_id>/")        
            services = []

            # only return routes for services of corresponding device from device type waage (3rd level)
            for link in links:
                level_number = link.count('/')
                if level_number == 4:
                    link = link.replace("<int:waaget_id>",str(pfandautomat_id))
                    services.append(link)
            

            return jsonify({
                "success": True,
                "device_id": waage_id,
                "device_type": "Waage",
                "services": services
            })


        except BaseException:
            abort(422)


        
    """
    GET /api/waagen/{id}/störungen
    Get Störungen of Waage with id
    [4th level]
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
                "device_id": waage_id,
                "device_type": "Waage",
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

