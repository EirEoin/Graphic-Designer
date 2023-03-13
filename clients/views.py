from django.shortcuts import render
from .models import Clients


def clients(request):
    clients = Clients.objects.all()
    return render(request, 'clients.html', {'clients': clients})
