import json


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
            #     # Caso seja uma URL de autenticação
            try:
                auth = json.loads(response.content)
            # Ex de resposta
            # {"access_token": "S0408QfL4eJe7PNcnubPPMcbYY0DO7", "expires_in": 36000, "token_type": "Bearer", "scope": "read", "refresh_token": "8pKglS82NC7CfDwBQwAVS1bykSLMGm"}
                print('Token->>>', auth)
            except Exception as e:
                print(e)
        return response
