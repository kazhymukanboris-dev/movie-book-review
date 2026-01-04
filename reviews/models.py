from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class MediaItem(models.Model):
    # Field to distinguish between a movie and a book
    CATEGORY_CHOICES = [
        ('Movie', 'Movie'),
        ('Book', 'Book'),
    ]
    
    title = models.CharField(max_length=255)
    author_or_director = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    release_year = models.IntegerField()
    image_url = models.URLField(blank=True) # Link to a cover image

    def __str__(self):
        return f"{self.title} ({self.category})"

class Review(models.Model):
    # Connects the review to a Movie/Book and a User
    item = models.ForeignKey(MediaItem, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Rating system (1 to 5 stars)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rated {self.item.title}: {self.rating}/5"
