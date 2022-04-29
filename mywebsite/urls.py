from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/detail/<slug:slug>', views.blog_detail, name='blog_detail'),
    path('bitkub/', views.bitkub, name='bitkub'),
 

]