from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def avasus(request):
    return render(request,'avasus.html')