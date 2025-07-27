"""
URL configuration for movie_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list_view, name='movie_list'),
    path('add/', views.movie_add_view, name='movie_add'),
    path('edit/<int:pk>/', views.movie_edit_view, name='movie_edit'),
    path('delete/<int:pk>/', views.movie_delete_view, name='movie_delete'),
]

