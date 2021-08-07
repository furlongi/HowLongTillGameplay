from django.http import JsonResponse


class Response:
    result_codes = {
        'default':        {'response': 500, 'code': -1, 'message': 'Internal Server Error.'},
        'success':        {'response': 200, 'code': 100},
        'required':       {'response': 400, 'code': 101},
        'does_not_exist': {'response': 400, 'code': 102, 'message': "Object value does not exist."},
        'incorrect_type': {'response': 400, 'code': 103, 'message': "Received incorrect data type"},
        'invalid_type':   {'response': 400, 'code': 103},
        'invalid':        {'response': 400, 'code': 103},
        'invalid_format': {'response': 400, 'code': 104}
    }

    def __init__(self):
        self._response = 500
        self._code = -1
        self._message = ''

    def _copy_response(self, new_response, attribute=None, message=''):
        self._response = new_response.get('response', 500)
        self._code = new_response.get('code', -1)

        string = new_response.get('message', '') if 'message' in new_response else str(message)
        if attribute:
            string = f"{str(attribute).capitalize()} Error: " + string

        self._message = string

    def create_response(self):
        resp = {'code': self._code}
        if self._message:
            resp['message'] = self._message
        return JsonResponse(resp, status=self._response)


class InvalidResponse(Response):

    def read_error(self, error):
        print(error)
        for e, desc in error.items():
            if len(desc):
                err = desc[0]
                if err.code in self.result_codes:
                    self._copy_response(self.result_codes[err.code], attribute=e, message=err)
                    return


class CustomResponse(Response):

    def read_response(self, resp, attribute=None, message=''):
        if resp in self.result_codes:
            self._copy_response(self.result_codes[resp], attribute=attribute, message=message)
