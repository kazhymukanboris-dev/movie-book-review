from django.db import models
from django.contrib.auth.models import User

class MediaItem(models.Model):
    CATEGORY_CHOICES = [('Movie', 'Movie'), ('Book', 'Book')]
    title = models.CharField(max_length=255)
    author_or_director = models.CharField(max_length=255)
    description = models.TextField()  # Ensure this matches Task 4
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    release_year = models.IntegerField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    item = models.ForeignKey(MediaItem, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)