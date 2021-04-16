from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.


def landing_view(request, language=''):
    
    args = {}
   
    return TemplateResponse(request, 'landing/index.html', args)
 
