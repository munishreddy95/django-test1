from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="homepage"),
    path('add',views.addarticle,name="addpage"),
    path('edit/<articleid>',views.editarticle,name="editpage"),
]

