from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def splash_page (request):
    return render(request, "../static_pages/about_me.html")