from professions.models import Profession


def create_default_professions():
    '''Generate system default professions'''
    default_professions = [
        {"id": 1, "title": "Software Developer", "status": 1},
       ]

    for profession in default_professions:
        Profession.objects.create(id=profession['id'], title=profession['title'], status=profession['status'])
