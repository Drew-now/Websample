from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import ListView, DetailView


# Create your views here.
def main(request):
    return render(request, "home.html")



