"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publishers/', views.publishers),
    path('publisher_add/', views.publisher_add),
    path('publisher_del/', views.publisher_del),
    path('publisher_update/', views.publisher_update),
    path('all_book/', views.book_list),
    path('book_add/', views.book_add),
    path('book_del/', views.book_del),
    path('book_update/', views.book_update),
    path('all_author/', views.author_list),
    path('author_add/', views.author_add),
    path('author_update/', views.author_update),
    path('author_del/', views.author_del),
    path('temp_test/', views.temp_test),
    path('get_json/', views.get_json),
    path('upload/', views.Upload.as_view()),
    path('test/', views.test),
]
