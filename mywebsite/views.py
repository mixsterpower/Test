

# Create your views here.
from multiprocessing import context
from .models import Blog
from django.shortcuts import render
from bitkub import Bitkub

def index(request):

    blogs = Blog.objects.all()
    contxt = {
        'blogs' : blogs

    }
    return render(request, 'index.html',contxt)

def blog_detail(request,slug=None):
    blog  = Blog.objects.get(slug=slug)
    contxt = {
        'blog':blog
       

    }
    return render(request, 'blog_detail.html',contxt)

    
def blog(request):
    return render(request, 'blog.html')

def bitkub(request):
    API_KEY = '69b00d6e5d4a0c485f578551ed4bcecf'
    API_SECRET = '63ab8dfb763d1661348d98e7b1bba64e'
    # initial obj only non-secure
    bitkub = Bitkub()
    # initial obj non-secure and secure
    bitkub = Bitkub(api_key=API_KEY, api_secret=API_SECRET)
    bitkub.status()
    valuechk = 0
    chk = bitkub.ticker('THB_BTC')
    value = chk['THB_BTC']  
    valuechk = value['last']
    contxt = {
        'valuechk' : valuechk
    }
    return render(request, 'bitkub.html',contxt)



