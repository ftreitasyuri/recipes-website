from django.urls import path
from django.http import HttpResponse

# Forma 1
# from recipes.views import home

#Forma 2
from . import views


urlpatterns = [
    path('', views.home), #Home
    path('recipes/<int:id>/', views.recipe), #Recipe
    # path('recipes/<slug:id>/', views.recipe), #Recipe
  
]
