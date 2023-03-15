from django.shortcuts import render
from .models import PreviousWork

# Create your views here.


def work(request):
    gallery = PreviousWork.objects.all()
    return render(request, 'work.html', context=context)
