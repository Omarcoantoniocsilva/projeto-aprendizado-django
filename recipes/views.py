from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Marco Antônio'
    })

def sobre(request):
    return render(request, 'temp.html')

def contato(request):
    return HttpResponse('CONTATO')