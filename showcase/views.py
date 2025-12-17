import os
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = os.environ.get('TESTNAME')
    return HttpResponse(f"Hello {name}! this is repsonse from showcase")
