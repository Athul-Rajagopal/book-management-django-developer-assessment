from django.urls import path
from .views import *

urlpatterns = [
    
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('reading-lists/', ReadingListAPI.as_view(), name='reading-lists'),
    path('create-reading-list/',ReadingListCreate.as_view(),name='create-reading-list'),
    path('reading-lists/<int:pk>/', ReadingListDetailAPI.as_view(), name='reading-list-detail'),
    
]
