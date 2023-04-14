from django.shortcuts import render, redirect
from account.models import Book
import ebooklib
from bs4 import BeautifulSoup

def reader_app(request):
    if request.method == 'POST':
        book_pk = request.POST.get('book_pk')
        b = Book.objects.get(pk=book_pk)
        path = b.path.replace('/app/media/', '')

        context = {
            'path': path,
        }
        return render(request, 'reader/reader.html', context)
    return redirect('books')