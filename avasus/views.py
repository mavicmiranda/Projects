from django.shortcuts import render
from .models import Avasus

def index(request):
    avasus = Avasus.objects.all()

    dados = {
        'avasus' : avasus
    }

    return render(request,'index.html',dados)

def avasus(request):
    return render(request,'avasus.html')