from django.shortcuts import render, get_list_or_404,get_object_or_404
from .models import Book

# Create your views here.
def book_list_view(request):

    books = get_list_or_404(Book)
    context= {
        'books':books
    }
    return render(request,'books/book_list.html', context)

def book_detail_view(request, pk=None):
    book = get_object_or_404(Book,id=pk)
    context = {
        'book': book
    }
    return render(request,'books/book_detail.html',context)