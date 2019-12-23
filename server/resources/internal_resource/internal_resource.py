import flask
import logging
import random

from flask import Blueprint, request, make_response
from server.utils.utils import Utils

ocr_internal = Blueprint('ocr_internal', __name__)

@ocr_internal.route('/addDigitized', methods=['POST'])
def add():
    try:
        generate_request = Utils.get_string_request(request)
        addToFile = Utils.addToFile(generate_request)
        return make_response(flask.jsonify(generate_request), 200)
    except Exception as e:
        logging.exception(e)