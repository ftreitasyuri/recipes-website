from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('HOME 1')

def home(request):
    numero = [1, 2, 3, 4]
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Yuri Dev',
        'qtd': numero
    })

def recipe(request, id):
    
    # numero = [1, 2, 3, 4]
    numero = [id]
    # id = numero[2]
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Yuri Dev',
        'qtd': numero,
        # 'recipe': id
    })