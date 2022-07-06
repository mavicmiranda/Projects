from django.shortcuts import render , get_list_or_404, get_object_or_404
from .models import Avasus

def index(request):
    avasus = Avasus.objects.all()

    dados = {
        'avasus' : avasus
    }

    return render(request,'index.html',dados)

def avasus(request,avasus_id):
    avasus = get_object_or_404(Avasus,pk= avasus_id)

    curo_a_exibir = {
        'avasus' : avasus
    }

    return render(request,'avasus.html',curo_a_exibir)