from django.urls import path
from . import views

urlpatterns = [
    # Маршруты для веб-страниц (HTML шаблоны)
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('books/', views.book_list, name='book_list'),
    
    # API эндпоинты (Задание 3)
    # 1. Для получения списка и создания новых записей (GET, POST)
    path('api/media/', views.media_api, name='media_api'),
    
    # 2. Для работы с конкретным элементом (GET, PUT, DELETE)
    # <int:pk> позволяет передавать ID фильма или книги прямо в URL
    path('api/media/<int:pk>/', views.media_detail_api, name='media_detail_api'),
]