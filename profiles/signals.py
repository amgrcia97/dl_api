from profiles.models import Profile


def create_default_profiles():
    '''Generate system default profiles'''
    default_profiles = [
        {"id": 1, "title": "Admin Master", "slug": "admin_master", "status": 1},
        {"id": 2, "title": "Admin", "slug": "admin", "status": 1},
        {"id": 3, "title": "Staff", "slug": "staff", "status": 1},
        {"id": 4, "title": "Teacher", "slug": "teacher", "status": 1},
        {"id": 5, "title": "Student", "slug": "student", "status": 1},
        {"id": 6, "title": "Teacher and student", "slug": "teacher_and_student", "status": 1}
        ]

    for profile in default_profiles:
        Profile.objects.create(id=profile['id'], title=profile['title'], slug=profile['slug'], status=profile['status'])
