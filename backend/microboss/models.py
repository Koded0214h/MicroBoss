from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('founder', 'Founder'),
        ('mentor', 'Mentor'),
        ('admin', 'Admin'),
    ]
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    startup_stage = models.CharField(max_length=50, choices=[
        ('idea', 'Idea'),
        ('mvp', 'MVP'),
        ('scaling', 'Scaling')
    ], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class ContentType(models.Model):
    name = models.CharField(max_length=21)
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
class Toolkit(models.Model):
    CONTENT_TYPES = [
        ('pdf', 'PDF'),
        ('notion', 'Notion'),
        ('video', 'Video'),
        ('google_doc', 'Google Doc'),
    ]
    LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    resource_link = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='toolkits/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    level = models.CharField(max_length=20, choices=LEVELS)
    tags = models.ManyToManyField('Tag', blank=True)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Invites(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    school = models.CharField()
    idea = models.TextField()
    
    def __str__(self):
        return self.idea
    
