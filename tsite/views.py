from django.http import HttpResponse, Http404
import datetime

def current_datetime(request):

    '''Dispplay current datetime
    '''

    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def love_jiajia(request):

    '''Display time I met Jia from first time
    '''

    now = datetime.datetime.now()
    first = datetime.datetime.strptime("1/10/13 9:02", "%d/%m/%y %H:%M")
    deltaDays = (now - first).days
    deltaSeconds = (now - first).seconds
    head = "<html><body></body></html>"
    text = "We have met each other %s days %s seconds.<p></p>" % (deltaDays, deltaSeconds) + \
        "I will always love you, JiaJia<p></p>"
    sign = "Yours,<p></p>Wei"
    end = "</body></html>"
    return HttpResponse(head + text + sign + end)

def hours_ahead(request, offset):

    '''Calculate time after given hours
    '''

    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s), it will be %s.<body></html>" % (offset, dt)
    return HttpResponse(html)