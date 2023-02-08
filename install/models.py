import requests
import json
from datetime import datetime
from accounts.models import User, UserData
from languages.models import Language, CountryLanguage
from addresses.models import City, Country, State


class InstallManager:

    def set_default_users(self):
        '''Creates the default superusers'''
        default_users = [
            {'email': 'amgrcia97@gmail.com', 'full_name': 'Andrés Murcia García', 'password': 'Eko@uh2020'},
        ]

        for user in default_users:
            if not User.objects.filter(email=user['email']).exists():
                User.objects.create_superuser(**user)
            if 'password' in user.keys():
                user1 = User.objects.get(email=user['email'])
                user1.set_password(user['password'])
                user1.save()
            if not UserData.objects.filter(user__email=user['email']).exists():
                UserData.objects.create(
                    user=User.objects.get(email=user['email']),
                    type=3,
                    phone='11 992638529',
                    gender=1,
                    birthday=datetime(day=19, month=1, year=1997),
                    document='12345678965',
                    born_country=Country.objects.get(name='Cuba'),
                    born_language=CountryLanguage.objects.get(code='es-cu'),
                    country=Country.objects.get(name='Brazil'),
                    state=State.objects.get(initial='SP'),
                    city=City.objects.get(name='Osasco'),
                    interest_language=Language.objects.get(code='pt')
                )

    def set_default_languages(self):
        '''Creates the default languages'''
        # Reference in https://www.dca.fee.unicamp.br/pgp/codes.shtml
        default_languages = [
            {'title': 'Português', 'code': 'pt'},
            {'title': 'Español', 'code': 'es'},
            {'title': 'English', 'code': 'en'},
            {'title': 'Français', 'code': 'fr'},
            {'title': 'Deutsch', 'code': 'de '},
        ]
        list_languages = []
        for language in default_languages:
            if not Language.objects.filter(title=language['title']).exists():
                list_languages.append(Language(
                    title=language['title'],
                    code=language['code'],
                ))
        if len(list_languages) > 0:
            Language.objects.bulk_create(list_languages)

    def set_default_countries(self):
        '''Creates the default countries'''
        # Reference in 'https://restcountries.com/v2/all'
        languages_codes_list = Language.objects.all().values_list('code', flat=True)
        rest_countries = requests.get('https://restcountries.com/v2/all').json()
        for country in rest_countries:
            if not Country.objects.filter(alpha3Code=country['alpha3Code']).exists():
                Country.objects.create(
                    name=country['name'],
                    alpha2Code=country['alpha2Code'],
                    alpha3Code=country['alpha3Code'],
                    flag=country['flags']['png'],
                )
            for language in country['languages']:
                if 'iso639_1' in language.keys() and language['iso639_1'] in languages_codes_list:
                    code = language['iso639_1'] + '-' + country['alpha2Code'].lower()
                    if not CountryLanguage.objects.filter(code=code).exists():
                        CountryLanguage.objects.create(
                            code=code,
                            country=Country.objects.get(alpha3Code=country['alpha3Code']),
                            language=Language.objects.get(code=language['iso639_1']),
                        )

    def set_default_states_and_cities(self):
        country = Country.objects.get(name='Brazil')
        brazil_states = open('install/utils/brazil/states.json', encoding='utf-8')
        brazil_states = json.load(brazil_states)
        for state in brazil_states:
            if not State.objects.filter(name=state['name'], initial=state['initial']).exists():
                State.objects.create(name=state['name'], initial=state['initial'], country=country)

        brazil_cities = open('install/utils/brazil/cities.json', encoding='utf-8')
        brazil_cities = json.load(brazil_cities)
        for state in brazil_cities:
            st = State.objects.get(initial=state)
            for city in brazil_cities[state]:
                if not City.objects.filter(name=city, state=st).exists():
                    City.objects.create(name=city, state=st)
