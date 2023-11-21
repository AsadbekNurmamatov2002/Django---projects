from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.
 
 
def error_404_view(request, exception):
   
    # we add the path to the handler404.html file
    # here. The name of our HTML file is 404.html

    # здесь. Имя нашего HTML-файла — 404.html.
    # добавляем путь к файлу handler404.html

    
    return render(request, 'handler404.html', status=404)


def error_500_view(request):
    return render(request, 'handler500.html', status=500)
