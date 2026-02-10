from django import forms
from .models import MediaItem, Review

class MediaForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'author_or_director', 'category', 'description', 'release_year', 'image_url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }