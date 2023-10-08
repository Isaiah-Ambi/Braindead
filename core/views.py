from django.shortcuts import render, get_object_or_404
from .models import musings

# Create your views here.

def index(request):
    musing = musings.objects.get()
    return render(request, 'core/index.html', {'musings':musing})

