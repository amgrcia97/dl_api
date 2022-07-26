from genders.models import Gender


def create_default_genders():
    '''Generate system default genders'''
    default_genders = [
        {"id": 1, "title": "Male", "slug": "male", "status": 1},
        {"id": 2, "title": "Female", "slug": "female", "status": 1},
        {"id": 3, "title": "None", "slug": "none", "status": 1},
       ]

    for gender in default_genders:
        Gender.objects.create(
            id=gender['id'],
            title=gender['title'],
            slug=gender['slug'],
            status=gender['status'])
