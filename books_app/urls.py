from django.urls import path
from .views import book_detail_view, book_list_views

urlpatterns = [
    path('',book_list_view, name='book_detail'),
    path('<int:pk>',book_detail_view, name='book-detail'),
    
]