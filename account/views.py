from django.shortcuts import render
from django.views import View
import os
from syncread import settings

# Create your views here.

def books(request):
    return render(request, 'account/books.html')

def add(request):
    return render(request, 'account/add.html')


class Add(View):
    def get(self, request):
        return render(request, 'account/add.html')

    def post(self, request):
        uploads = request.FILES.getlist('files')
        if uploads:
            for file in uploads:
                # Создаем директорию, если она не существует
                media_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
                os.makedirs(media_dir, exist_ok=True)
                
                # Сохраняем файл
                with open(os.path.join(media_dir, file.name), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            return render(request, 'account/books.html')
        else:
            return render(request, 'account/add.html')

