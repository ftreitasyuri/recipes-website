from django.urls import path
from django.http import HttpResponse
from recipes.views import home


urlpatterns = [
    path('', home), #Home
   
]
