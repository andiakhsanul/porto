from django.db import models
from django.contrib.auth.models import AbstractUser

ARTICLE_STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('inprogress', 'In Progress'),
]

class UserProfile(AbstractUser):

    # jika login pakai username (default), boleh kosongkan;
    # eksplisit tetap oke:
    REQUIRED_FIELDS = []  # diminta saat createsuperuser selain username & password

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    word_count = models.PositiveIntegerField(default=0)
    twitter_post = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=ARTICLE_STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
