from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('books/', views.book_list, name='book_list'),
    
    # New API endpoint for Task 6
    path('api/media/', views.media_api, name='media_api'),
]