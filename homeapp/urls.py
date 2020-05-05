from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="indexpage"),
    path('add',views.addarticle,name="addpage"),
    path('edit',views.editarticle,name="editpage"),
]
