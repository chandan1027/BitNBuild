from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Occasion(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clothes')
    photo = models.ImageField(upload_to='clothes_pics/')
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='clothes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='clothes')
    date_added = models.DateField(default=timezone.now)
    location = models.CharField(max_length=255)
    occasion = models.ForeignKey(
        Occasion, on_delete=models.SET_NULL, null=True, related_name='clothes')

    # Extra attributes
    is_favorite = models.BooleanField(default=False)
    worn_today = models.BooleanField(default=False)
    donated = models.BooleanField(default=False)
    in_laundry = models.BooleanField(default=False)
    recycled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Accessories(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='accessories')
    photo = models.ImageField(upload_to='accessories_pics/')
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True, related_name='accessories')
    date_added = models.DateField(default=timezone.now)
    location = models.CharField(max_length=255)
    occasion = models.ForeignKey(
        Occasion, on_delete=models.SET_NULL, null=True, related_name='accessories')

    # Extra attributes
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Grooming(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='grooming')
    photo = models.ImageField(upload_to='grooming_pics/')
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True, related_name='grooming')
    date_added = models.DateField(default=timezone.now)
    location = models.CharField(max_length=255)
    occasion = models.ForeignKey(
        Occasion, on_delete=models.SET_NULL, null=True, related_name='grooming')

    # Extra attributes
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ToBuyItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # Link to User model
    content = models.TextField()
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content}'
