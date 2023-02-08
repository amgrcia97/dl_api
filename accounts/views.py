from rest_framework import viewsets  # , status
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import serializers
from accounts.models import User
from accounts.serializers import UsersSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''API for Discere Linguis Users'''
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)  # UserPermission)
    # Classes para filtros específicos, abertos & ordenação
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.SearchFilter,
        rest_framework_filters.OrderingFilter,
    )
    # Campos de pesquisa específicos
    filterset_fields = []
    # Campos de pesquisa abertos
    search_fields = []
    # Campos de ordenação
    ordering_fields = search_fields

    def get_queryset(self):
        return User.objects.all().distinct().order_by('id')

    # def list(self, request):
    #     serializer = UserListSerializer(page, many=True, context={'request': request, 'client_id': request.user.selected_client.id})
    #     return self.get_paginated_response(serializer.data)
    #     pass

    # def retrieve(self, request, pk=None):
    #     # queryset = get_object_or_404(self.get_queryset(), pk=pk)
    #     # serializer = UserRetrieveSerializer(queryset, many=False, context={'request': request, 'client_id': request.user.selected_client.id})
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
    #     pass


class EmptySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterUserView(viewsets.GenericViewSet):
    serializer_class = EmptySerializer
#     @action(detail=False, methods=['POST'], name='Solicita a gravação de um usuário')
#     def register_user(self, request):
#         '''Solicita a criação de um usuário e o mesmo poderá utilizar o sistema assim que redefinir sua senha via e-mail'''
#         # Valida os dados
#         data = self.__load_user_areas_from_branch(data=request.data)
#         data, extra_data = UserRetrieveSerializer.validate_user_data(data=data, is_register=True)
#         data.update({'status': 6})
#         extra_data.update({'receive_email': request.data.get('receive_email', True)})
#         # Grava o usuário
#         serializer = UserRetrieveSerializer(data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(**data)
#         # Efetua a leitura do usuário
#         user_id = serializer.data.get('id')

#         user = get_object_or_404(User.objects.filter(pk=user_id))

#         # Define se o usuário quer ou não receber emails
#         User.objects.allow_receive_email(user=user, receive_email=extra_data.get('receive_email', True))

#         if extra_data.get('accept_terms_and_conditions'):
#             # Caso tenha sido definido o aceite dos termos e condições, grava
#             self.accept_terms_and_conditions(user)
#         # Efetua o disparo do welcome e-mail caso send_welcome_email seja true
#         if extra_data.get('send_welcome_mail') is True:
#             # Caso o pré cadastro esteja forçando o processo de enviar o welcome e-mail, ou não esteja definido
#             print("Disparando o welcome email", extra_data.get('language', None))
#             welcome_email(request, user, extra_data.get('language'))
#         if extra_data.get('webservice_login', False) is True:
#             # Caso trata-se de um login via webservice então retorna um OAuth token para que o usuário acesse
#             context = request_oauth2_token(user_email=user.email)
#             return Response(context, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST', 'GET'], name='Verifica a existência de um usuário com o e-mail')
    def check_email_existance(self, request):
        # '''Verifica se um e-email existe para outro usuário'''
        # if not request.POST.get('email', None):
        #     raise ValidationError({'email': _('É necessário informar o email')})
        # email = request.POST.get('email')
        # if not request.POST.get('id_user', None):
        #     raise ValidationError({'id_user': _('É necessário informar o código do usuário')})
        # id_base_user = request.POST.get('id_user')

        # exists, id_user = check_email_existance(email, id_base_user)
        # return Response({'email': email, 'exists': exists, 'id_user': id_user}, status=status.HTTP_200_OK)
        pass

    @action(detail=False, methods=['POST', 'GET'], name='Verifica a existência de um usuário pelo documento')
    def check_document_existance(self, request):
        # '''Verifica se um documento existe para uma outra Loja'''
        # if not request.POST.get('document', None):
        #     raise ValidationError({'document': _('É necessário informar o documento')})
        # document = request.POST.get('document')
        # if not request.POST.get('id_user', None):
        #     raise ValidationError({'id_user': _('É necessário informar o código do usuário')})
        # id_base_user = request.POST.get('id_user')

        # exists, id_user = check_document_existance(document, id_base_user)
        # return Response({'document': document, 'exists': exists, 'id_user': id_user}, status=status.HTTP_200_OK)
        pass

    @action(detail=False, methods=['POST'], name='Dispara o welcome e-mail para o usuário')
    def welcome_email(self, request):
        # """Dispara o e-mail de boas vindas para um usuário"""
        # if not request.POST.get('user_id', None):
        #     raise ValidationError({'user_id': _('É necessário informar o id do usuário')})
        # user_id = request.POST.get('user_id')
        # user = get_object_or_404(User.objects.filter(pk=user_id))
        # return welcome_email(request, user)
        pass

        # def welcome_email(request, user, language=None):
        #     '''Solicita o envio do link para alteração de senha via e-mail'''
        #     data = {'message': 'POST'}
        #     request_language = get_language()
        #     data = send_welcome_email(user, data)
        #     activate(request_language)
        #     return Response(data)
