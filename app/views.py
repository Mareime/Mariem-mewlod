from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def Home(request):
    template = loader.get_template('Accceuil.html')
    return HttpResponse(template.render())
