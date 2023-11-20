# Django---projects
Django-урок-projects
--------------------------------саздат vertual enve  и скачат django-------------------------------------
>>py -m venv myworld
>>myworld\Scripts\activate.bat
>>py -m pip install Django
>>django-admin --version
>>django-admin startproject myproject
>>py manage.py runserver
>>CTRL+C
>>cd myporoject
>>py manage.py stert myapp
>>py manage.py runserver

------------------------------settings.py--Добавить вложение-----------------------------------------------
DEBUG = False #now

ALLOWED_HOSTS = ["*"] #now


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'errorhandler.apps.ErrorHandlerConfig', #Now 
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,"templates"], #Now 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


-----------------------------projects>urls.py------------------------------------------------
from django.contrib import admin
from django.urls import include, path
 
urlpatterns = [
    path('', include('errorhandler.urls'))
]
 

# этот обработчик-handling 404 error
# ishlov beruvchi
handler404 = 'errorhandler.views.error_404_view'

--------------------------------------------------------------------------------------------
------------------------------------------views.py-----------------------------------------

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.
#саздат views
 
 
def error_404_view(request, exception):
   
    # we add the path to the handler404.html file
    # here. The name of our HTML file is 404.html

    # здесь. Имя нашего HTML-файла — 404.html.
    # добавляем путь к файлу handler404.html

    
    return render(request, 'handler404.html')
-----------------------------------------------------------------------------------------
-----------------------------------templates>handler404.html-----------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error404</title>
</head>
<body style="background-color: beige;">
    <h1>404 Not Found</h1>
   
    <h1 style="font-size: 22px; text-align: center; background-color: blanchedalmond; color: rgb(63, 59, 59);">404 topilmadi javobi; Bu noto'g'ri so'rov tufayli, chunki foydalanuvchi so'rayapti
        mavjud bo'lmagan hujjat.
    </h1>
        <br>
    <h1 style="font-size: 22px; text-align: center; background-color: blanchedalmond; color: rgb(63, 59, 59);">
        ответ 404 Not Found; это связано с неправильным запросом, поскольку клиент запрашивает
        документ, которого нет.
    </h1>
        <br>
       
    <h1 style="font-size: 22px; text-align: center; background-color: blanchedalmond; color: rgb(63, 59, 59);"> a 404 Not Found response; this is due to a bad request because the client is requesting 
            a document that does not exist. </h1>
    <br>
</body>
</html>
_______________________________________________________________________________________


