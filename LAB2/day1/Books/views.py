from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from .models import *
from .forms import *
from django.views import View
from django.views.generic import ListView,CreateView
# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello Tarek</h1>')

class BookList(ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'books'

class AddBook(CreateView):
    model = Book
    template_name = 'addmodel.html'
    fields='__all__'
    success_url = 'list.html'
#     def get(self,request):
#         context={'form':AddBookModel(),'msg':'class get'}
#         return render(request,'addmodel.html',context)

#     def post(self,request):
#         context={}
#         form=AddBookModel(data=request.POST,files=request.FILES)
#         if(form.is_valid()):
#             form.save()
#             return HttpResponseRedirect('list.html')
#         else:
#             context['msg']=form.errors
#             context['form']=form
#         return render(request,'addmodel.html')
        
    #     if request.method == 'POST':
    #     form = Addbook(request.POST)
    #     if (form.is_valid()):
    #         title = form.cleaned_data['title']
    #         author_id = form.cleaned_data['author']
    #         image = form.cleaned_data['image']
    #         Book.objects.create(title=title, author_id=author_id,image=image)
    #         return HttpResponseRedirect('/book/list')
    #     else:
    #         context['msg'] = 'Please fill all fields'
    # return render(request, 'add.html', context)



def book_addmodel(request):
    context={'form':AddBookModel()}
    if(request.method=='POST'):
        form=AddBookModel(data=request.POST,files=request.FILES)
        print(form.is_valid())
        print(form.errors)
        if(form.is_valid()):
            form.save()
    return render(request,'addmodel.html',context)


def book_list(request):
    context={}
    books=Book.objects.all()
    context['books']=books
    return render(request,'list.html',context)


def book_add(request):
    context = {'form': AddBook()}
    if request.method == 'POST':
        form = Addbook(request.POST)
        if (form.is_valid()):
            title = form.cleaned_data['title']
            author_id = form.cleaned_data['author']
            image = form.cleaned_data['image']
            Book.objects.create(title=title, author_id=author_id,image=image)
            return HttpResponseRedirect('/book/list')
        else:
            context['msg'] = 'Please fill all fields'
    return render(request, 'add.html', context)


def book_update(request,name):
    # book=Book.objects.filter(title=name).first()
    # form=AddBookModel(data=book)
    context={'form':form}
    return render(request,'update.html',context)

def book_delete(request,id):
    Book.objects.filter(id=id).delete()
    return HttpResponseRedirect('/book/list')
    return HttpResponse(f'<h1>Book deleted  {id}</h1>')

def book_view(request,id):
    context={'book':Book.objects.get(id=id)}
    return render(request,'view.html',context)
