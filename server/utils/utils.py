import os
from datetime import date
import json
import pickle
path = "/Users/saurabhkumar/plateiq/server/upload"
filepath = "/Users/saurabhkumar/plateiq/server/resources/mockdata.json"
class Utils(object):

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
    def get_string_request(request):
        """ :param Request request: Flask request object
        """
        data = {}
        args = {}
        if request.get_data(as_text=True):
            data = (request.get_data(as_text=True))
            return data
        if request.args:
            args = request.args.to_dict()
            print(args)
        return json.load(dict(data, **args))
    @staticmethod
    def addToFile(object):
        clone = {}
        obj = json.loads(object)
        with open(filepath, 'rb') as json_file:
            try:
                data = pickle.load(json_file)
                clone = data
                for i in obj:
                    if i.get('invoiceNo') is not None:
                        clone[i.get('invoiceNo')] = i

            except EOFError:
                for i in obj:
                    clone[i.get('invoiceNo')] = i
        json_file.close()
        with open(filepath, 'wb') as j:
            pickle.dump(clone, j)
            return {'result': 'successfully updated the data'}
            j.close()

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


