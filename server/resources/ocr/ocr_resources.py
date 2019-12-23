import flask
import logging
import os

from flask import Blueprint, request, make_response
from server.utils.utils import Utils

ocr = Blueprint('ocr', __name__)
path = "/Users/saurabhkumar/plateiq/server/upload"
@ocr.route('/uploadPDF', methods=['POST'])
def upload():
    try:
        # generate_request = Utils.get_pdf_request(request)
        data = request.get_data()
        file = request.files['image']
        print(file)
        print(os.path.exists(path))
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, 'test.pdf'), "wb") as fp:
            fp.write(request.data)
        # file.save(os.path.join(path), 'hi')
        print('image saved')
        # return make_response(flask.jsonify({'hi'}), 200)
    except Exception as e:
        logging.info('test')

