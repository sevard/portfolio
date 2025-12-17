from django.urls import path
from . import views

app_name = 'showcase'

urlpatterns = [
    # /showcase/
    path('', views.index, name='index')
]