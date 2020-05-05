from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requests):
    return HttpResponse("Index Page")

def addarticle(requests):
    return HttpResponse("Add Article Page")

def editarticle(requests):
    return HttpResponse("Edit Article Page")
    
    