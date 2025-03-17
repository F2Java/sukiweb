from django.urls import path
from webapp import views



urlpatterns = [
    path('', views.index, name='index'), 
    path('home', views.home, name='home'),
    path('ourmenu', views.ourmenu, name='ourmenu'),
    path('ourloc', views.ourloc, name='ourloc'),
    path('busops', views.busops, name='busops'),
    path('contact', views.contact, name='contact'),
   
]