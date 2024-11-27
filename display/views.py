from django.shortcuts import render
from .models import DisplayPage

def display_page_view(request, page_id):
    page = DisplayPage.objects.get(id=page_id)
    context = {
        'page': page,
    }
    return render(request, 'display/display-page.html', context)
