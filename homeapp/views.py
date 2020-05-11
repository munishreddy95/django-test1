from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
# Create your views here.
def index(requests):
    context = {
        "articlelist":Article.objects.all(),
    }
    return render(requests,"homeapp/index.html",context)

def addarticle(requests):
    if requests.method == "POST":
        title = requests.POST.get('title')
        description = requests.POST.get('description')
        articleimage = requests.FILES.get('articleimage')
        insertdata = Article(title=title,description=description,articleimage=articleimage)
        insertdata.save()
        return redirect(index)
    else:
        return render(requests,"homeapp/add.html")

def editarticle(requests,articleid):
    print(articleid)
    if requests.method == "POST":
        title = requests.POST.get('title')
        description = requests.POST.get('description')
        articleimage = requests.FILES.get('articleimage')
        getdata = Article.objects.get(pk=articleid)
        getdata.title=title
        getdata.description=description
        getdata.articleimage=articleimage
        getdata.save()
        return redirect(index)
    else:
        context = {
            "data":Article.objects.get(id=articleid),
        }
        return render(requests,"homeapp/edit.html",context)
    
    