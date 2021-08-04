from flask import Flask, request, jsonify, abort, url_for
from flask_cors import CORS
import urllib
import re

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
            'GET,POST,PATCH,DELETE,OPTIONS')
        return response


    """
    Check if app is running
    """
    @app.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify("Healthy")



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
    GET /api
    Get all registered store device types
    """

    @app.route("/api")
    def get_devices():
        try:
            links = list_routes("/api")            

            return jsonify({
                "success": True,
                "devices": links
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

            links = list_routes("/api/pfandautomaten/<int:pfandautomat_id>/")        
            services = []

            #replace <int:pfandautomat_id> with actual id by using regex
            for link in links:
                link = link.replace("<int:pfandautomat_id>", pfandautomat_id)
                services.append(link)

            return jsonify({
                "success": True,
                "pfandautomat_id": pfandautomat_id,
                "services": services
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
   
            links = list_routes("/api/waagen/<int:waage_id>/")   
            print(links)         

            return jsonify({
                "success": True,
                "waage_id": waage_id,
                "services": links
            })

        except BaseException:
            abort(422)


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

