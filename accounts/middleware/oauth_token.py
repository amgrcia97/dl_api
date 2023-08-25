class BeforeTokenMiddleware:
    '''
    Método responsável por efetuar processamentos pré-rotas & pós-rotas
    '''
    get_response = None

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if '/o/token/' in request.path:
            print(request.path)
        return response
