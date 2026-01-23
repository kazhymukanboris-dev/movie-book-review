from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MediaItem
from .serializers import MediaItemSerializer

# Web Views
def home(request):
    return render(request, 'reviews/home.html')

def movie_list(request):
    movies = MediaItem.objects.filter(category='Movie').prefetch_related('reviews')
    return render(request, 'reviews/list.html', {'items': movies, 'title': 'Movies'})

def book_list(request):
    books = MediaItem.objects.filter(category='Book').prefetch_related('reviews')
    return render(request, 'reviews/list.html', {'items': books, 'title': 'Books'})

# API View for Task 6
@api_view(['GET', 'POST'])
def media_api(request):
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