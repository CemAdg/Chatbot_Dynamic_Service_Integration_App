from flask_script import Manager
from app import app
from flask import url_for

manager = Manager(app)

@manager.command
def list_routes():
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        #link = urllib.parse.unquote("{} {} {}".format(rule.endpoint, methods, rule))
        line = urllib.parse.unquote("{}".format(rule))
        output.append(line)

    for line in sorted(output):
        print(line)
        #print(link)


        
if __name__ == '__main__':
    manager.run()