import os
from datetime import date
path = "/Users/saurabhkumar/plateiq/server/upload"
class Utils(object):
    @staticmethod
    def prepare_response_object(result=None, error_message=None, error_code=None, error_description=None,
                                error_stack=None):
        return {
            'result': result,
            'error': Utils.prepare_error_object(error_message, error_code, error_description, error_stack)
        }
    @staticmethod
    def prepare_error_object(error_message=None, error_code=None, error_description=None, error_stack=None):
        return {
            'message': error_message,
            'code': error_code,
            'description': error_description,
            'stack': error_stack
        }
    @staticmethod
    def importData(request):
        try:
            file = request.files['image']
            print(file)
            print(os.path.exists(path))
            if not os.path.exists(path):
                os.makedirs(path)
            with open(os.path.join(path, 'test.pdf'), "wb") as fp:
                fp.write(request.data)
            return {'result':'successfully uploaded'}
        except Exception as e:
            print(e)

    @staticmethod
    def getMockData():
        mockdata = {
            'invoiceNo':1234,
            'date':date.today().strftime("%d/%m/%Y"),
            'item':{
                'type':'pen',
                'quantity':2000
            }
        }
        return {'result':mockdata}


