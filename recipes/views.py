from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('HOME 1')

def home(request):
    numero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Yuri Dev',
        'qtd': numero
    })
