import flask
import logging
import random

from flask import Blueprint, request, make_response
from server.utils.utils import Utils

ocr = Blueprint('ocr', __name__)
@ocr.route('/uploadPDF', methods=['POST'])
def upload():
    try:
        generate_request = Utils.importData(request)
        return make_response(flask.jsonify(generate_request), 200)
    except Exception as e:
        logging.exception(e)

@ocr.route('/getStatus', methods=['GET'])
def getStatus():
    try:
        statusList = ['processing','pending','processed']
        status = random.choice(statusList)
        return make_response(flask.jsonify({'result':status}), 200)
    except Exception as e:
        logging.exception(e)

