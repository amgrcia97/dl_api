from languages.models import Language, CountryLanguage


def create_default_languages():
    '''Generate system default languages'''
    default_languages = [
        {"id": 1, "title": "Portuguese", "code": "pt", "status": 1},
        {"id": 2, "title": "Spanish", "code": "es", "status": 1},
        {"id": 3, "title": "English", "code": "en", "status": 1},
       ]

    for language in default_languages:
        Language.objects.create(
            id=language['id'],
            title=language['title'],
            code=language['code'],
            status=language['status'])


def create_default_country_languages():
    '''Generate system default languages'''
    default_country_languages = [
        {"id": 1, "title": "Portuguese Brazil", "country": 1, "language": 1, "code": "pt-br", "status": 1},
        {"id": 2, "title": "Spanish Spain", "country": 2, "language": 2, "code": "es-es", "status": 1},
        {"id": 3, "title": "English United States", "country": 3, "language": 3, "code": "en-us", "status": 1},
       ]

    for country_language in default_country_languages:
        CountryLanguage.objects.create(
            id=country_language['id'],
            title=country_language['title'],
            country=country_language['country'],
            language=country_language['language'],
            code=country_language['code'],
            status=country_language['status'])
