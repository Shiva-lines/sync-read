from django.shortcuts import render

def reader_app(request):
    return render(request, 'reader/reader.html')