from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    page = loader.get_template('welcome.html')
    return HttpResponse(page.render())