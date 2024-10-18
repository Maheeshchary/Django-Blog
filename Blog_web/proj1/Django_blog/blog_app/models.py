from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Django(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
class Networking(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='networking_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
class Development(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='development_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class VisitCounter(models.Model):
    count = models.IntegerField(default=0)
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User  # The User model to be used
        fields = ['username', 'email', 'password1', 'password2'] 
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email   