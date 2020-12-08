from django.http import HttpRequest

def Update(request):
    p = request.POST["p"]
    n = request.POST["q"]

    request.session[p] = str(int(request.session.get(p,0)) + int(n))

def Delete(request):
    p = request.GET["p"]
    request.session[p] = 0