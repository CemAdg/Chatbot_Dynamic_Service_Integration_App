from flask import Flask, request, jsonify, abort, url_for
from flask_cors import CORS
import urllib
import re
import json


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

    @app.route("/api", methods=['GET'])
    def get_devices():
        try:
            links = list_routes("/api") 

            device_types = {}   
            counter = 0
            questions = [
                "Zu welchem Gerätetyp in der Filiale möchtest du Informationen haben?"
            ]

            # only return routes for device types (1st level)
            for link in links:
                
                device_type = {}
                tags = []

                level_number = link.count('/')
                if level_number == 2:
                    # ToDo: tags in jeder API als Metadaten hinterlegen und beim Abgreifen aller Routes auch die Tags abgreifen 
                    counter = counter + 1
                    if "pfandautomaten" in link:
                        tags = [ 
                            "Pfandflaschenautomat",
                            "Leergutautomat",
                            "leergutautomat",
                            "leergut",
                            "Leergut",
                            "pfand",
                            "Pfand",
                            "Pfandautomat",
                            "pfandautomat",
                            "pfandflaschenautomat",
                            "pfandflaschen automat",
                            "pfand automat",
                            "deposit machine",
                            "depositMachine"
                        ]
                    if "waagen" in link:
                        tags = [ 
                            "Wiegegerät",
                            "Waage",
                            "waage",
                            "wiegen",
                            "waagen",
                            "wiegegerät",
                            "Waagen",
                            "gemüsewaage",
                            "obstwaage",
                            "Gemüsewaage",
                            "Obstwaage"
                        ]

                    device_type = { 
                        counter :  {
                            "uri" : link,
                            "tags" : tags
                        }
                    }

                    print(device_type)

                    device_types.update(device_type)

            return jsonify({
                "success": True,
                "questions": questions,
                "device_types": device_types
            })            

        except BaseException:
            abort(422)



    """
    Pfandautomat APIs

    ####################=-...-=####################
    ##################=-.......-=##################
    ################=-...........-=################
    ##############=-...............-=##############
    ############=-...................-=############
    ###########-..............*==:.....-###########
    #########-................+==-.......-#########
    #######-.................:====.........-#######
    #####-..................-=====*..........-#####
    ###-....................*======:...........-###
    #-.....................-=======*.............-#
    ........................=======*...............
    .................:*****+..*====*...............
    .................=======:.*====*...............
    .................=======:.*====*.+****:........
    .................=======:.*====*.*#######+.....
    .................=======:.*====*.::::+####=....
    .................=======:.*====*.......*###*...
    ..........+:.....=======:.*===*-.......:###=...
    ........*##+.....-+++++:...............*###=...
    .....:#####=*************************=#####-...
    ...-#####################################*.....
    .....-=####=**************************+-.......
    ........+##+...................................
    ..........::...................................
    ...............................................
    ########=.............................=########
    ########=.............................=########
    ########=.............................=########
    ########=.............................=########

    """

    """
    GET /api/pfandautomaten
    Get all available devices of type Pfandautomat in the store
    [2nd level]
    """    
    @app.route('/api/pfandautomaten', methods=['GET'])
    def get_pfandautomaten():

        try:
            questions = [
                "Bitte nennen Sie die ID eines der Geräte, für welchen Sie einen Service aufrufen wollen."
            ]

            json_dummy = { 
                1: { 
                    "id": 1, 
                    "name" : "Einwegautomat P001",
                    "uri" : "/api/pfandautomaten/1"
                },
                2: { 
                    "id": 2, 
                    "name" : "Mehrwegautomat P002",
                    "uri" : "/api/pfandautomaten/2"
                },
                3: { 
                    "id": 3, 
                    "name" : "Mehrwegautomat P003",
                    "uri" : "/api/pfandautomaten/3"
                } 
            }

            pfandautomaten = json_dummy

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
                "questions": questions,
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
            services = {}   
            counter = 0

            questions = [
                "Welchen Service möchten Sie aufrufen?"
            ]

            # only return routes for services of corresponding device from device type pfandautomat (3rd level)
            for link in links:
                service_type = {}
                tags = []

                level_number = link.count('/')
                if level_number == 4:
                    link = link.replace("<int:pfandautomat_id>",str(pfandautomat_id))
                    
                    counter = counter + 1
                    # ToDo: tags in jeder API als Metadaten hinterlegen und beim Abgreifen aller Routes auch die Tags abgreifen 
                    if "füllstand" in link:
                        tags = [ 
                            "Füllstand",
                            "füllstand",
                            "fillLevel",
                            "Ladung",
                            "fill level",
                            "fill",
                            "ladung",
                            "füllung",
                            "Füllung",
                            "wie voll"
                        ]
                    if "störungen" in link:
                        tags = [ 
                            "störung",
                            "Störung",
                            "störungen",
                            "Störungen",
                            "error",
                            "Error",
                            "fehler",
                            "Fehler"
                        ]

                    service_type = {
                        counter : {
                            "uri" : link,
                            "tags" : tags 
                        }
                    }

                    services.update(service_type)
            

            return jsonify({
                "success": True,
                "questions": questions,
                "device_type": "Pfandautomat",
                "device": pfandautomat_id,
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

            füllstand = [
                { 
                    "Füllstand":"75%",
                    "Beschreibung":"Füllstand beträgt 75 %. Bitte Pfandautomat demnächst leeren, um Überfüllung zu vermeiden."
                } 
            ]  

            return jsonify({
                "success": True,
                "device": pfandautomat_id,
                "device_type": "Pfandautomat",
                "service" : "Füllstand",
                "service_message" : füllstand
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
   
            störungen = [
                { 
                    "Komponente":"Band",
                    "Beschreibung":"Flaschen-Einfuhrband läuft nicht mehr."
                },
                { 
                    "Komponente":"Drucker",
                    "Beschreibung":"Pfandbon-Drucker funktioniert nicht mehr."
                }
            ]

            return jsonify({
                "success": True,
                "device": pfandautomat_id,
                "device_type": "Pfandautomat",
                "service" : "Störungen",
                "service_message" : störungen
            })


        except BaseException:
            abort(422)


 
    """
    Waage APIs
    ...............................................................................
    ...............................................................................
    .....................................=WWWW*....................................
    .....................................=WWWW*....................................
    .....................................=WWWW*....................................
    .....................................=WWWW*...............-=@#:................
    ................*WWWW#...............=WWWW*..............+WWWWW=...............
    ...............-WWWWWW#*+:-..........=WWWW*.......-:+*=#@WWWWWW#...............
    ................=WWWW@-+@WWWWWWWWWW@#@WWWW@WWWWWWWWWWW#+..*WWW#-...............
    .................=@=W-.....-+@WWWWWWWWWWWWWWWWWWW@+-......:W*W*................
    ................*W-.##..........-*@WWWWWWWWW@*-..........-W*.:W:...............
    ...............+W:...@=..............=WWWW*..............@#...*W-..............
    ..............-W*....-W*.............=WWWW*.............=@.....=@..............
    ..............@=......+W:............=WWWW*............*W-......@#.............
    .............#@........*W-...........=WWWW*...........:W:.......-W*............
    ............*W-.........##...........=WWWW*..........-W*.........:W:...........
    ...........:W:..........-@=..........=WWWW*..........##...........*W-..........
    ..........-W*............:W+.........=WWWW*.........*W-............##..........
    ..........##..............*W-........=WWWW*........+W:.............-@=.........
    .......#@@W@@@@@@@@@@@@@@@@WW@@-.....=WWWW*.....+@@WW@@@@@@@@@@@@@@@@W@@*......
    .......+WWWWWWWWWWWWWWWWWWWWWW#......=WWWW*......@WWWWWWWWWWWWWWWWWWWWWW:......
    ........:WWWWWWWWWWWWWWWWWWWW=.......=WWWW*.......#WWWWWWWWWWWWWWWWWWW@-.......
    ..........:@WWWWWWWWWWWWWWW*...-:::::#WWWW*:::::...-=WWWWWWWWWWWWWWW#-.........
    ..............:*#@WW@#=+-......:WWWWWWWWWWWWWWWW-......-*=@@W@@#*:.............
    ...............................:WWWWWWWWWWWWWWWW-..............................
    ...............................................................................
    ........................*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:.......................
    ........................*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:.......................
    ........................*WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW:.......................
    ...............................................................................
    ...............................................................................
    """

    """
    GET /api/waagen
    Get Get all available devices of type Waage in the store
    [2nd level]
    """    
    @app.route('/api/waagen', methods=['GET'])
    def get_waagen():
        
        try:
            questions = [
                "Bitte nennen Sie die ID eines der Geräte, für welchen Sie einen Service aufrufen wollen."
            ]

            json_dummy = { 
                1: { 
                    "id": 1, 
                    "name" : "Obstwaage P001",
                    "uri" : "/api/waagen/1"
                },
                2: { 
                    "id": 2, 
                    "name" : "Gemüsewaage P002",
                    "uri" : "/api/waagen/2"
                }
            }

            waagen = json_dummy

            devices = waagen

            return jsonify({
                "success": True,
                "questions": questions,
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
            services = {}
            counter = 0

            questions = [
                "Welchen Service möchten Sie aufrufen?"
            ]

            # only return routes for services of corresponding device from device type pfandautomat (3rd level)
            for link in links:
                service_type = {}
                tags = []

                level_number = link.count('/')
                if level_number == 4:
                    link = link.replace("<int:waage_id>",str(waage_id))
                    
                    counter = counter + 1
                    # ToDo: tags in jeder API als Metadaten hinterlegen und beim Abgreifen aller Routes auch die Tags abgreifen 
                    if "störungen" in link:
                        tags = [ 
                            "störung",
                            "Störung",
                            "Störungen",
                            "störungen",
                            "error",
                            "Error",
                            "fehler",
                            "Fehler"
                        ]

                    service_type = {
                        counter : {
                            "uri" : link,
                            "tags" : tags
                        }
                    }

                    services.update(service_type)
            

            return jsonify({
                "success": True,
                "questions": questions,
                "device_type": "Waage",
                "device": waage_id,
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
   
            störungen = [
                { 
                    "Komponente":"Drucker",
                    "Beschreibung":"Drucker ist defekt."
                }
            ]

            return jsonify({
                "success": True,
                "device": waage_id,
                "device_type": "Waage",
                "service" : "Störungen",
                "service_message" : störungen
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

