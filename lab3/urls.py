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

#����������� ��������� �������. ��� ��������� ��� ������������ ������������, ����� ��� ���� � ����������� ������
from django.conf import settings
#����������� ������� ��� ��������� ����������� ������. ��� ������� ��� ��������� ��������� ������ � ����������� �������� � ������ ����������.
from django.conf.urls.static import static
#����������� �����-������ Django, ������� ��������� ��������� ������� ����� ���-���������.
from django.contrib import admin
#����������� ������� ��� ������ � URL. path ������������ ��� ����������� ���������, � include ��������� ���������� ������ ����� ���������.
from django.urls import path, include

#������, ������� �������� ��� �������� (URL) �������.
urlpatterns = [
    path('admin/', admin.site.urls),

    #���� ������� ���������, ��� ���� ������������ ������� �� �������� �����, 
    # �� ����� �������������� URL �� ����� urls.py, ������� ��������� � ���������� courses.
    #������� include() ��������� ���������� ������ ����� ���������, ��� ������ ��� ����� ��������������.
    path('', include('courses.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:: ���������, ������� �� ����� �������. ���� �� ������� (������ ��� ��� � �������� ����������), ����������� ��������� ���.
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT):
#��� ������ ��������� �������� ��� ������� � ����������� ������ (��������, CSS � ������������).
#settings.STATIC_URL � ��� URL-����� ��� ������� � ����������� ������.
#document_root=settings.STATIC_ROOT � ��� ���� �� ������� � ���������� �� ������������ �������.