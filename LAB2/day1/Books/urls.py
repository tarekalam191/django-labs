from django.urls import path

from . views import *

urlpatterns = [
    
    path('list/', book_list, name='book_list'),
    path('listing/', BookList.as_view(), name='book_listing'),
    path('add/', book_add, name='book_add'),
    path('Addclass/',AddBook.as_view(), name='book_add'),
    path('addmodel/', book_addmodel, name='book_addmodel'),
    path('Update/<str:name>/', book_update, name='book_update'),
    path('Delete/<int:id>/', book_delete, name='book_delete'), 
    path('View/<int:id>/', book_view, name='book_view'),   
]