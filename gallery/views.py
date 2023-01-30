from django.shortcuts import render
from .models import PreviousWork

# Create your views here.

def work(request):
    images = ["Rinse_JohnDaly.jpg", "Rinse_Shampain.jpg", "Guiness_Skeleton.jpg", "Rinse_Crabs.jpg", "Rinse_Ducks.jpg", "Skeleton_Feet.jpg"]
    return render(request, 'work.html', {'images': images})

