from rest_framework import viewsets  # , status
from rest_framework.decorators import action
# from rest_framework.response import Response
# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework.exceptions import ValidationError
# from rest_framework import serializers
# # from django.utils.translation import gettext_lazy as _
# from accounts.models import User, UserData
# from addresses.models import Country, State, City
# from languages.models import Language
# from accounts.serializers import UsersSerializer, UserDataSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''API for Discere Linguis Users'''
    # serializer_class = UserRetrieveSerializer
    # permission_classes = (IsAuthenticated, UserPermission)
    # pagination_class = DataTables
    # # Classes para filtros específicos, abertos & ordenação
    # filter_backends = (
    #     filters.DjangoFilterBackend,
    #     rest_framework_filters.SearchFilter,
    #     rest_framework_filters.OrderingFilter,
    # )
    # # Campos de pesquisa específicos
    # filterset_fields = [
    #     # 'id',
    #     # 'full_name',
    #     # 'nick_name',
    #     # 'email',
    #     # 'date_joined',
    #     # 'date_updated',
    #     # # 'status',
    #     # 'user_data__document',
    #     # 'user_data__register',
    #     # 'user_data__gender__slug',
    #     # 'user_data__birthday',
    #     # 'user_clients__profile__id',
    # ]
    # # Campos de pesquisa abertos
    # search_fields = [
    #     # 'id',
    #     # 'full_name',
    #     # 'nick_name',
    #     # 'email',
    #     # 'date_joined',
    #     # 'date_updated',
    #     # # 'status',
    #     # 'user_data__document',
    #     # 'user_data__register',
    #     # 'user_data__gender__slug',
    #     # 'user_data__birthday',
    #     # 'user_data__companies__name',
    #     # 'user_data__companies__document',
    #     # 'user_data__company_branches__name',
    #     # 'user_data__company_branches__document',
    #     # 'user_data__company_branches__register',
    #     # 'user_clients__profile__id',
    # ]
    # # Campos de ordenação
    # ordering_fields = search_fields

    def get_queryset(self):
        # from areas.models import Area, AreaCountry
        # '''Lista apenas as categorias do cliente selecionado'''
        # user = self.request.user
        # queryset = User.objects.prefetch_related(
        #     Prefetch(
        #         lookup='user_badges',
        #         queryset=BadgeUser.objects.prefetch_related(
        #             'badge__badge_images',
        #         ).filter(
        #             badge__clients__in=[user.selected_client],
        #             badge__countries__in=[user.selected_country.id],
        #             badge__status=1
        #         ),
        #         to_attr='list_user_badges'
        #     ),
        #     Prefetch(
        #         lookup='user_data',
        #         queryset=UserData.objects.prefetch_related(
        #             'addresses',
        #             'branch_regional',
        #             'companies',
        #             'phones',
        #             Prefetch(
        #                 lookup='managers',
        #                 to_attr='list_user_managers'
        #             ),
        #             Prefetch(
        #                 lookup='company_branches',
        #                 queryset=Branch.objects.prefetch_related(
        #                     Prefetch(
        #                         lookup='managers',
        #                         to_attr='list_managers'
        #                     )
        #                 ).filter(status__in=[1, 4]).distinct(),
        #                 to_attr='list_company_branches',
        #             ),
        #             Prefetch(
        #                 lookup='addresses',
        #                 queryset=Address.objects.prefetch_related(
        #                     'city',
        #                     'city__state',
        #                     'city__state__country'
        #                 ),
        #                 to_attr='user_address'
        #             ),
        #         ),
        #         to_attr='user_user_data'
        #     ),

        #     Prefetch(
        #         lookup='user_data__companies',
        #         queryset=Company.objects.filter(status=1, clients__in=[user.selected_client]).distinct(),
        #         to_attr='list_companies',
        #     ),
        #     Prefetch(
        #         lookup='user_data__company_branches',
        #         queryset=Branch.objects.filter(status__in=[1, 4]).distinct(),
        #         to_attr='list_company_branches',
        #     ),
        #     Prefetch(
        #         lookup='user_clients',
        #         queryset=UserClient.objects.prefetch_related(
        #             'client',
        #             'client__profiles',
        #             'countries',
        #             'profile',
        #             'areas',
        #             Prefetch(
        #                 lookup='areas',
        #                 to_attr='list_areas'
        #             ),
        #             Prefetch(
        #                 lookup='main_areas',
        #                 queryset=Area.objects.prefetch_related(
        #                     Prefetch(
        #                         lookup='area_countries',
        #                         queryset=AreaCountry.objects.filter(
        #                             status=1,
        #                             country_id=user.selected_country.id
        #                         ),
        #                         to_attr='list_country_areas'
        #                     ),
        #                 ).filter(
        #                     area_countries__country_id=user.selected_country.id
        #                 ).distinct(),
        #                 to_attr='list_main_areas'
        #             ),
        #             'module_items'
        #         ).filter(
        #             countries__id__in=[user.selected_country.id],
        #         ).distinct(),
        #         to_attr='list_user_clients'
        #     ),
        #     Prefetch(
        #         lookup='user_clients',
        #         queryset=UserClient.objects.prefetch_related(
        #             'client',
        #             'client__profiles',
        #             'countries',
        #             'profile',
        #             'areas',
        #             'module_items'
        #         ).filter(
        #             client=user.selected_client
        #         ).distinct(),
        #         to_attr='user_selected_client'
        #     ),
        #     Prefetch(
        #         lookup='user_trail_complete_result',
        #         queryset=TrailCompleteUserResult.objects.prefetch_related('trail_complete', 'trail_complete__clients', 'trail_complete__countries').filter(
        #             status=1,
        #             trail_complete__status=1,
        #             trail_complete__clients__in=[user.selected_client.id],
        #             trail_complete__countries__in=[user.selected_country.id],
        #         ),
        #         to_attr='list_trail_user_results'
        #     ),
        #     Prefetch(
        #         lookup='group_training_user_result_user',
        #         queryset=GroupTrainingUserResult.objects.prefetch_related('group_training', 'group_training__clients', 'group_training__countries').filter(
        #             status=1,
        #             group_training__clients__in=[user.selected_client.id],
        #             group_training__countries__in=[user.selected_country.id],
        #         ),
        #         to_attr='list_group_training_user_results'
        #     ),
        #     Prefetch(
        #         lookup='user_accept_terms',
        #         queryset=UserAcceptTermsAndConditions.objects.all(),
        #         to_attr='list_user_accept_terms'
        #     )
        # ).filter(
        #     user_clients__client_id=user.selected_client.id,
        #     user_clients__countries__id__in=[user.selected_country.id],
        # ).distinct()

        # # TODO - ANOTATE: profile, status, companies, company_branches, areas

        # if not user.is_superuser:
        #     # Somente os perfis permitidos
        #     queryset = queryset.filter(
        #         user_clients__profile_id__in=list(user.profiles.values_list('id', flat=True))
        #     )
        #     # Caso a flag de perfil do usuário permita ignorar áreas
        #     if user.profile.ignore_areas is False:
        #         queryset = queryset.filter(
        #             user_clients__areas__in=list(user.user_clients.values_list('areas', flat=True)),
        #         )
        #     # Caso a flag de perfil do usuário não permite listar usuários do mesmo perfil
        #     if user.profile.list_same_profile is False:
        #         queryset = queryset.exclude(
        #             user_clients__profile_id=user.profile.id,
        #         )
        #     # Aplica os filtros de Regional, Rede, Loja e Manager, de acordo com o perfil do usuário
        #     if user.profile.filter_regional:
        #         user_regional = list(user.user_data.branch_regional.values_list('id', flat=True))
        #         if len(user_regional) > 0:
        #             # Caso o usuário possua alguma rede, filtra apenas usuários da empresa
        #             queryset = queryset.filter(
        #                 Q(user_data__branch_regional__in=user_regional) |
        #                 Q(user_data__managers__in=[user])
        #             )
        #     elif user.profile.filter_company:
        #         # Caso o perfil do usuário utilize filtro de empresas
        #         user_companies = list(user.user_data.companies.values_list('id', flat=True))
        #         company_branches = list(Branch.objects.filter(company_id__in=user_companies).values_list('id', flat=True))
        #         if len(user_companies) > 0:
        #             # Caso o usuário possua alguma rede, filtra apenas usuários da empresa
        #             queryset = queryset.filter(
        #                 Q(user_data__companies__in=user_companies) |
        #                 Q(user_data__company_branches__in=company_branches) |
        #                 Q(user_data__managers__in=[user])
        #             )
        #     elif user.profile.filter_branch:
        #         if 'elanco' in str(settings.SYSTEM_NAME).lower():
        #             # Regra Elanco - O filtrar loja só pode mostrar usuários da loja onde o usuário é gerente e não todos da loja do usuário
        #             # TODO - PROVAVELMENTE ISSO TERÁ QUE IR PARA UMA FLAG DE PERFIL filter_manager, aguardando necessidade do cliente\
        #             # A correção que precisamos é: gerente visualizar usuários da sua loja ou usuários em que o gerente está cadastrado como responsável.
        #             # O gerente não deve visualizar usuários que fazem parte da mesma loja em que ele esteja cadastrado,
        #             # mas somente da loja em que ele é gerente.
        #             user_branches = list(user.branch_managers.values_list('id', flat=True))
        #             user_managers = list(user.user_managers.values_list('user_id', flat=True))
        #             if len(user_branches) > 0 or len(user_managers) > 0:
        #                 queryset = queryset.filter(Q(user_data__company_branches__in=user_branches) | Q(pk__in=user_managers)).distinct()
        #             else:
        #                 queryset = queryset.filter(Q(user_data__company_branches__isnull=True)).distinct()
        #         else:
        #             user_branches = list(user.user_data.company_branches.values_list('id', flat=True))
        #             user_branches += list(user.branch_managers.values_list('id', flat=True))
        #             if len(user_branches) > 0:
        #                 # Caso o usuário possua alguma loja, filtra apenas usuários da loja
        #                 queryset = queryset.filter(
        #                     Q(user_data__company_branches__in=user_branches) |
        #                     Q(branch_managers__in=user_branches) |
        #                     Q(user_data__managers__in=[user])
        #                 ).distinct()
        #             else:
        #                 queryset = queryset.filter(Q(user_data__company_branches__isnull=True)).distinct()
        # return queryset
        pass

    def list(self, request):
        # # TODO - MÉTODO COMPROMETIDO
        # queryset = self.get_queryset().distinct()
        # filter_profile = request.GET.getlist('profile', None)
        # filter_status = request.GET.getlist('status', None)
        # filter_companies = request.GET.getlist('companies', None)
        # filter_branches = request.GET.getlist('company_branches', None)
        # filter_areas = request.GET.getlist('areas', None)

        # if len(filter_profile) > 0:
        #     queryset = queryset.filter(user_clients__profile__id__in=filter_profile)

        # if len(filter_status) > 0:
        #     # Caso o status 3 tenha sido selecionado, então mostra os deletados, se não não
        #     queryset = queryset.exclude(status=3) if 3 not in filter_status else queryset
        #     queryset = queryset.filter(status__in=filter_status)
        # else:
        #     queryset = queryset.exclude(status=3)

        # if len(filter_companies) > 0:
        #     queryset = queryset.filter(user_data__companies__id__in=filter_companies)

        # if len(filter_branches) > 0:
        #     queryset = queryset.filter(user_data__company_branches__id__in=filter_branches)

        # if len(filter_areas) > 0:
        #     queryset = queryset.filter(user_clients__areas__id__in=filter_areas)

        # queryset = self.filter_queryset(queryset)
        # # Campo de Pesquisa Paralelo
        # if request.GET.get('ordering', None) in ['profile', '-profile']:
        #     queryset = queryset.order_by('user_clients__profile__name') if request.GET.get('ordering', None) == 'profile' else queryset.order_by('-user_clients__profile__name')
        # elif request.GET.get('ordering', None) in ['birthday', '-birthday']:
        #     queryset = queryset.order_by('user_data__birthday') if request.GET.get('ordering', None) == 'birthday' else queryset.order_by('-user_data__birthday')
        # elif request.GET.get('ordering', None) in ['document', '-document']:
        #     queryset = queryset.order_by('user_data__document') if request.GET.get('ordering', None) == 'document' else queryset.order_by('-user_data__document')
        # elif request.GET.get('ordering', None) in ['gender', '-gender']:
        #     queryset = queryset.order_by('user_data__gender__title') if request.GET.get('ordering', None) == 'gender' else queryset.order_by('-user_data__gender__title')
        # elif request.GET.get('ordering', None) in ['register', '-register']:
        #     queryset = queryset.order_by('user_data__register') if request.GET.get('ordering', None) == 'register' else queryset.order_by('-user_data__register')
        # else:
        #     queryset = queryset.order_by('-id' if request.GET.get('ordering', None) in [None, ''] else request.GET.get('ordering'))
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = UserListSerializer(page, many=True, context={'request': request, 'client_id': request.user.selected_client.id})
        #     return self.get_paginated_response(serializer.data)
        pass

    def retrieve(self, request, pk=None):
        # queryset = get_object_or_404(self.get_queryset(), pk=pk)
        # serializer = UserRetrieveSerializer(queryset, many=False, context={'request': request, 'client_id': request.user.selected_client.id})
        # return Response(serializer.data, status=status.HTTP_200_OK)
        pass

    def create(self, request):
        # '''Solicita a criação de um usuário'''
        # data = request.data
        # data = UserRetrieveSerializer.validate_user_data(data=data, user_changing=request.user)
        # serializer = UserRetrieveSerializer(data=data, partial=True, context={'request': request, 'client_id': request.user.selected_client.id})
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save(password_to_change=request.data.get('password_to_change', None), **data)
        # pk = serializer.data.get('id')
        # user = get_object_or_404(User.objects.filter(pk=pk))
        # if user.status in [1, 6]:  # Caso seja ativo, ou pré-cadastro
        #     welcome_email(request, user)
        # return self.retrieve(request, pk)
        pass

    def update(self, request, pk=None):
        # '''Solicita a criação de um usuário'''
        # user = get_object_or_404(User, pk=pk)
        # data = request.data
        # data.update({'user_id': pk})
        # data = UserRetrieveSerializer.validate_user_data(data=data, user_changing=request.user)
        # serializer = UserRetrieveSerializer(user, data=data, partial=True, context={'request': request, 'client_id': request.user.selected_client.id})
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save(password_to_change=request.data.get('password_to_change', None), **data)
        # return self.retrieve(request, pk)
        pass

    def destroy(self, request, pk=None):
        # user = get_object_or_404(User.objects.filter(pk=pk))
        # user.status = 3
        # user.date_updated = timezone.now()
        # user.save()
        # return Response({'detail': 'deleted'}, status=status.HTTP_202_ACCEPTED)
        pass

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
