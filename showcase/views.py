import os
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(f"Repsonse Ok from 'home'")


def about(request):
    return HttpResponse(f"Repsonse Ok from 'about'")


def certs(request):
    return HttpResponse(f"Repsonse Ok from 'certs'")

