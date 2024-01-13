# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
#from api.models import hives

def beeyards(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def hives(request):
    registration = Registration.objects.all()
    return render(request, 'hives.html', {'registration': registration, 'beeyard': beeyard})
