# Create your views here.

from django.shortcuts import render
from app.models import *

def index(request):
    context = {
    }
    return render(request, 'index.html', context)


