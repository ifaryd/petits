from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.template import RequestContext
from . models import *

def index(request):
    acti=activité.objects.all().order_by('-id') [:3]
    actif=activité.objects.all().order_by('-id') [:2]
    data = {
        'acti':acti,
        'actif':actif

    }
    return render(request, 'base.html', data)

def contacts(request):
    return render(request, 'contacts.html')