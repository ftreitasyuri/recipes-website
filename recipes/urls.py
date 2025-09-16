from django.urls import path
from django.http import HttpResponse
from recipes.views import home, contact, about


urlpatterns = [
    path('', home), #Home
    path('sobre/', about), #About
    path('contato/', contact), #Contact
]
