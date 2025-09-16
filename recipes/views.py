from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('HOME 1')

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Yuri Dev'
    })

def about(request):
    return HttpResponse('SOBRE')

def contact(request):
    return HttpResponse('CONTATO')