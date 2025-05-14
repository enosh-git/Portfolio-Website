from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request): 
    return render(request, 'about/index.html')  # Updated to the correct template path