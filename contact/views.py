from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("IT WORKS")
            pass
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)
