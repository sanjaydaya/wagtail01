from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Process the form data (e.g., send an email, store in the database)
            # For now, we'll just display the submitted data
            context = {
                'name': name,
                'email': email,
                'message': message,
            }
            return render(request, 'contact_success.html', context)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
