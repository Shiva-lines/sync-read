from django.shortcuts import render, redirect
from django.views import View
import os
from syncread import settings
from ebooklib import epub
from .models import Book
from syncread.settings import MEDIA_ROOT

def remove(request):
    if request.method == 'POST':
        book_pk = request.POST.get('book_pk')
        book = Book.objects.get(pk=book_pk)
        file_path = os.path.join(MEDIA_ROOT, book.path)
        if os.path.isfile(file_path):  # проверяем, является ли указанный путь файлом
            book.delete()
            os.remove(file_path)  # удаляем файл
        else:
            print("Error: {} is not a file".format(file_path))
    return redirect('books')




def books(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return redirect('log_in')
    
    books = Book.objects.filter(user_id=request.user.pk)

    context = {
        'username': username,
        'books': books
    }
    return render(request, 'account/books.html', context)


class Add(View):
    def get(self, request):
        if request.user.is_authenticated:
            username = request.user.username
        else:
            return redirect('log_in')
        
        context = {
            'username': username
        }
        return render(request, 'account/add.html', context)

    def post(self, request):
        uploads = request.FILES.getlist('files')
        if uploads:
            for file in uploads:
                # checking extention
                ALLOWED_EXTENSIONS = ['.epub']
                filename = file.name
                file_ext = os.path.splitext(filename)[1]
                if file_ext.lower() not in ALLOWED_EXTENSIONS:
                    error = 'Invalid extention. Upload only .epub flies'
                    return render(request, 'account/add.html', {'error': error})
 
                # creation user's dir for uploads
                media_dir = os.path.join(settings.MEDIA_ROOT, f'uploads/{request.user.pk}')
                os.makedirs(media_dir, exist_ok=True)
                
                # writing files to user's dir
                with open(os.path.join(media_dir, file.name), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                # write data about book in db
                path = os.path.join(media_dir, file.name)

                book = epub.read_epub(path)
                title = book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else 'Unknown'
                authors = ', '.join(author[0] for author in book.get_metadata('DC', 'creator')) if book.get_metadata('DC', 'creator') else 'Unknown'

                new_book = Book(title=title, authors=authors, user_id=request.user.pk, path=path)
                new_book.save()

                                
                
            return redirect('books')
        else:
            username = request.user.username
            return render(request, 'account/add.html', {'username': username})

