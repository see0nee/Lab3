"""lab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Импортируем настройки проекта. Это позволяет нам использовать конфигурации, такие как пути к статическим файлам
from django.conf import settings
#Импортируем функцию для обработки статических файлов. Она поможет нам правильно настроить доступ к статическим ресурсам в режиме разработки.
from django.conf.urls.static import static
#Импортируем админ-панель Django, которая позволяет управлять данными через веб-интерфейс.
from django.contrib import admin
#Импортируем функции для работы с URL. path используется для определения маршрутов, а include позволяет подключать другие файлы маршрутов.
from django.urls import path, include

#список, который содержит все маршруты (URL) проекта.
urlpatterns = [
    path('admin/', admin.site.urls),

    #Этот маршрут указывает, что если пользователь заходит на корневой адрес, 
    # то будут использоваться URL из файла urls.py, который находится в приложении courses.
    #Функция include() позволяет подключать другие файлы маршрутов, что делает код более организованным.
    path('', include('courses.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:: Проверяем, включен ли режим отладки. Если он включен (обычно это так в процессе разработки), выполняется следующий код.
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT):
#Эта строка добавляет маршруты для доступа к статическим файлам (например, CSS и изображениям).
#settings.STATIC_URL — это URL-адрес для доступа к статическим файлам.
#document_root=settings.STATIC_ROOT — это путь на сервере к директории со статическими файлами.