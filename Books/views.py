from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from .models import *
# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello Tarek</h1>')

def book_list(request):
    context={}
    books=Book.objects.all()
    context['books']=books
    return render(request,'list.html',context)

def book_add(request):
    return render(request,'add.html')

def book_update(request,name):
    return HttpResponse(f'<h1>update Book {name}</h1>')

def book_delete(request,id):
    Book.objects.filter(id=id).delete()
    return HttpResponseRedirect('/book/list')
    return HttpResponse(f'<h1>Book deleted  {id}</h1>')

def book_view(request,id):
    context={'book':Book.objects.get(id=id)}
    return render(request,'view.html',context)
