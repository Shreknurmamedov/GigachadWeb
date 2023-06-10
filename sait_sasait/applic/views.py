from django.shortcuts import render
from .models import State


# Create your views here.
def index(request):
    data ={
        'title': 'Немного о Natus Vincere',
        'values': ['some', 'hello', '123'],
            }
    return render(request, 'applic/index.html', data)

def about(request):
    return render(request, 'applic/about.html')

def help(request):
    magazine = State.objects.order_by('date')
    return render(request, 'applic/help.html', {'magazine': magazine})




