from django.http import HttpResponse
from django.utils import timezone
from install.models import InstallManager


def __log(data, title, line_end=False):
    data.append('<li><strong>'+title+'</strong>: ' + timezone.now().strftime("%d-%m-%Y - %H:%M:%S") + '</li>')
    if line_end:
        data.append('<hr>')
    return data


def installer(request):
    data = []
    data = __log(data, 'Superusers start...')
    InstallManager().set_default_users()
    data = __log(data, 'Superusers end...', True)
    data = __log(data, 'Languages start...')
    InstallManager().set_default_languages()
    data = __log(data, 'Languages end...', True)
    data = __log(data, 'Countries and country languages start...')
    InstallManager().set_default_countries()
    data = __log(data, 'Countries and country languages end...', True)

    return HttpResponse(data)
