from django.urls import path

from . views import *

urlpatterns = [
    
    path('list/', book_list, name='book_list'),
    path('add/', book_add, name='book_add'),
    path('Update/<str:name>/', book_update, name='book_update'),
    path('Delete/<int:id>/', book_delete, name='book_delete'), 
    path('View/<int:id>/', book_view, name='book_view'),   
]