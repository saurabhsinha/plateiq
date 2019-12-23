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
            requ = request.get_data()
            return requ.data;
        except Exception as e:
            print(e)


