from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def work(request):
    images = ["Rinse_JohnDaly.jpg", "Rinse_Shampain.jpg", "Guiness_Skeleton.jpg", "Rinse_Crabs.jpg", "Rinse_Ducks.jpg", "Skeleton_Feet.jpg"]
    return render(request, 'work.html', {'images': images})
