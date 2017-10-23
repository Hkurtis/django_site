from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from django.shortcuts import render
from .models import Show
def index(request):
    all_shows = Show.objects.all()
    #template = loader.get_template('sound/index.html')
    context = { 'all_shows': all_shows }
    return render(request, 'sound/index.html', context)

def detail(request, show_num):
    try:
        s = Show.objects.get(pk=show_num)
    except Show.DoesNotExist:
        raise Http404("There is no podcast under this index yet!")
    #return HttpResponse('<h1> This is show #'+str(show_num)+'</h1>')
    return render(request, 'sound/detail.html', {'s': s})
