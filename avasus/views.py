from django.shortcuts import render , get_list_or_404, get_object_or_404
from .models import Avasus

def index(request):
    avasus = Avasus.objects.order_by('-data_curso').filter(publicada=True)

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

def buscar(request):

    lista_curso = Avasus.objects.order_by('-data_curso').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_curso = lista_curso.filter(nome_curso__icontains=nome_a_buscar)

    dados = {
        'avasus' : lista_curso
    }

    return render(request, 'buscar.html', dados)
