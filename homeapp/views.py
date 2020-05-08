from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requests):
    return render(requests,"homeapp/index.html")

def addarticle(requests):
    return render(requests,"homeapp/add.html")

def editarticle(requests):
    return render(requests,"homeapp/add.html")
    
    