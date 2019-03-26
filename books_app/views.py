from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list_views(request):

    books = get_list_or_404
    context= {
        'books':books
    }
    return render(request,'books/book_list.html', context)

def book_detail_view(request, pk=None):
    note = get_object_or_404(Book,id=pk)
    context{
        'book': book
    }
    return render(request,'books/book_detail.html',)