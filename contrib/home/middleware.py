from urllib import response


class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('testttttttttttttttttttttttttaaaaaaaaaaaaaaaaaaaa Midleware')
        response = self.get_response(request)
        return response