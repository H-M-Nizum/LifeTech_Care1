from django.shortcuts import render

# Create your views here.

def contactViews(request):
    return render(request, 'contact.html')