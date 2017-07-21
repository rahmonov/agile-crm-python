

class SuccessResponse:
    def __new__(cls, data=None, text=None, *args, **kwargs):
        return {
            'status_code': 200,
            'ok': True,
            'data': data,
            'text': text
        }


class NonSuccessResponse:
    def __new__(cls, status=400, text=None, *args, **kwargs):
        return {
            'status_code': status,
            'ok': True,
            'text': text
        }


class ErrorResponse:
    def __new__(cls, status=400, text=None, *args, **kwargs):
        return {
            'status_code': status,
            'ok': False,
            'text': text
        }
