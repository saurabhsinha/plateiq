import flask
import logging
import flask_cors
import datetime
import werkzeug.contrib.fixers
from server.resources.ocr import ocr_resources
from server.resources.internal_resource import internal_resource
from threading import Thread

from flask import make_response

app = flask.Flask(__name__)
app2=flask.Flask(__name__)
flask_cors.CORS(app)
flask_cors.CORS(app2)

app.wsgi_app = werkzeug.contrib.fixers.ProxyFix(app.wsgi_app)
app.register_blueprint(ocr_resources.ocr, url_prefix='/ocr')

app2.wsgi_app = werkzeug.contrib.fixers.ProxyFix(app2.wsgi_app)
app2.register_blueprint(internal_resource.ocr_internal, url_prefix='/ocr_internal')


@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')

@app2.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')

@app.route('/ping', methods=['GET'])
def health_check():
    logging.info('ping --> pong')
    return 'pong'
@app2.route('/ping', methods=['GET'])
def health_check():
    logging.info('ping --> pong')
    return 'pong2'
# ---------------------------------------- ERROR HANDLING ----------------------------------------------------------- #

def log_request(request):
    if 'Accept' in request.headers and 'text/html' in request.headers['Accept']:
        logging.critical('    '.join([datetime.datetime.today().ctime(),
                                        request.remote_addr, request.method,
                                        request.url, request.get_data(as_text=True),
                                        ', '.join([': '.join(x) for x in request.headers])]))
@app.errorhandler(404)
def not_found(error):
    log_request(flask.request)
    logging.error('Resource not found: ' + str(error))
    return make_response(flask.jsonify({'error': 'Resource not found', 'error_code': 404,
                                               'error_description': 'Specified resource does not exist on the server',
                                               'error_stack': None,
                                               'result': None}, code=404))

@app2.errorhandler(404)
def not_found(error):
    log_request(flask.request)
    logging.error('Resource not found: ' + str(error))
    return make_response(flask.jsonify({'error': 'Resource not found', 'error_code': 404,
                                               'error_description': 'Specified resource does not exist on the server',
                                               'error_stack': None,
                                               'result': None}, code=404))

def main():
    app.run(host='0.0.0.0', use_reloader=False, debug=True, port=3001)

def main2():
    app2.run(host='0.0.0.0', use_reloader=False, debug=True, port=3002)

if __name__ == '__main__':
    Thread(target = main).start()
    Thread(target = main2).start()