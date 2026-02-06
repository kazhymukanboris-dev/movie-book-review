from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MediaItem
from .serializers import MediaItemSerializer

# ==========================================
# Web Views (Отображение HTML-шаблонов)
# ==========================================

def home(request):
    """Главная страница проекта."""
    return render(request, 'reviews/home.html')

def movie_list(request):
    """Список фильмов с использованием DTL для отображения динамических данных."""
    # Используем prefetch_related для оптимизации запросов к отзывам [cite: 11]
    movies = MediaItem.objects.filter(category='Movie').prefetch_related('reviews')
    return render(request, 'reviews/list.html', {'items': movies, 'title': 'Movies'})

def book_list(request):
    """Список книг с использованием DTL."""
    books = MediaItem.objects.filter(category='Book').prefetch_related('reviews')
    return render(request, 'reviews/list.html', {'items': books, 'title': 'Books'})


# ==========================================
# API Endpoints (Задание №3)
# ==========================================

@api_view(['GET', 'POST'])
def media_api(request):
    """
    Эндпоинт для работы со списком объектов.
    Поддерживает: GET (получение всех) и POST (создание)[cite: 21, 22].
    """
    if request.method == 'GET':
        items = MediaItem.objects.all()
        serializer = MediaItemSerializer(items, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MediaItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def media_detail_api(request, pk):
    """
    Эндпоинт для работы с конкретным объектом по его ID (pk).
    Поддерживает: GET, PUT (обновление) и DELETE (удаление)[cite: 21, 23, 24].
    """
    item = get_object_or_404(MediaItem, pk=pk)
    
    if request.method == 'GET':
        serializer = MediaItemSerializer(item)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Частичное или полное обновление данных [cite: 24]
        serializer = MediaItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Удаление объекта из базы данных [cite: 23]
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)