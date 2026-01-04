from django.contrib import admin
from .models import MediaItem, Review

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author_or_director', 'release_year')
    list_filter = ('category', 'release_year')
    search_fields = ('title', 'author_or_director')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment', 'user__username', 'item__title')
