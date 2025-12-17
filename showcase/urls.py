from django.urls import path
from . import views

app_name = 'showcase'

urlpatterns = [
    # /showcase/
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('certs/', views.certs, name='certs')
]