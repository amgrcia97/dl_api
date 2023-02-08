from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from accounts.models import User
from accounts.serializers import EmptySerializer, UsersSerializer


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


class RegisterUserView(viewsets.GenericViewSet):
    serializer_class = EmptySerializer
    permission_classes = ()

    @action(detail=False, methods=['POST', 'GET'], name='Solicita a gravação de um usuário')
    def user(self, request):
        '''Solicita a criação de um usuário'''
        serializer = UsersSerializer(data=request.data, partial=False, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save(**request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
