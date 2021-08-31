from django.urls import path
from . import views

urlpatterns = [
    #Index Page
    path('',views.home,name='home'),
    
]