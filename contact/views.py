from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()
            # Display a success message to the user
            messages.success(request, 'Thank you for reaching out!')
            # Redirect the user back to the contact page with an empty form
            return redirect('contact')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)
