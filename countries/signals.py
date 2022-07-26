from countries.models import Country


def create_default_countries():
    '''Generate system default countries'''
    default_countries = [
        {"id": 1, "name": "Brazil", "code": "br", "status": 1},
        {"id": 2, "name": "Spain", "code": "sp", "status": 1},
        {"id": 3, "name": "United States", "code": "us", "status": 1},
       ]

    for country in default_countries:
        Country.objects.create(
            id=country['id'],
            name=country['name'],
            code=country['code'],
            status=country['status'])
