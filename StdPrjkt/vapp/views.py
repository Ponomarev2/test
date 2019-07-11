from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

def index(request):
    return render(request, 'vapp/homePage.html')

def search(request):
    n = (request.POST['name'] + request.POST['surname'])
    prfl = Profile.objects.filter(nomerZachetki=n).order_by("subjectName")
    mydict = {'nomer': n, 'prfl': prfl}
    # return render(request, 'vapp/searchres.html', {'prfl': prfl})
    if len(prfl)>0:
        #return render(request, 'vapp/searchres.html', {'nomer': n, 'prfl': prfl})
        return render(request, 'vapp/table.html', mydict)
    else:
        return HttpResponse(request.POST['name'] + ' ' + request.POST['surname'])

