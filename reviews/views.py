from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MediaItem, Review
from .forms import MediaForm, ReviewForm
from .serializers import MediaItemSerializer

# --- Web Views ---

def home(request):
    return render(request, 'reviews/home.html')

def movie_list(request):
    items = MediaItem.objects.filter(category='Movie')
    return render(request, 'reviews/list.html', {'items': items, 'title': 'Movies'})

def book_list(request):
    items = MediaItem.objects.filter(category='Book')
    return render(request, 'reviews/list.html', {'items': items, 'title': 'Books'})

def item_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    
    # Handle "Add Review" form directly on this page
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.item = item
            review.user = request.user
            review.save()
            return redirect('item_detail', pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'reviews/detail.html', {'item': item, 'form': form})

@login_required
def add_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MediaForm()
    return render(request, 'reviews/add_media.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# --- API Views (Keep these!) ---

@api_view(['GET', 'POST'])
def media_list_api(request):
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
    item = get_object_or_404(MediaItem, pk=pk)
    if request.method == 'GET':
        serializer = MediaItemSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MediaItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)