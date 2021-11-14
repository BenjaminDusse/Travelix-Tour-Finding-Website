from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(max_length=200)

    def __str__(self):
        return self.name


class Rest_area(models.Model):
    TYPE_CHOICES = (
        ('per night', 'per night'),
        ('for week', 'for week'),
        ('two days', 'two days'),
        ('three days', 'three days')
    )
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='recreation_pics/')
    bottom_images = models.ImageField(upload_to='recreation_pics/bottoms', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    text = RichTextField()
    type = models.CharField(max_length=300, choices=TYPE_CHOICES)
    tags = models.ManyToManyField(Tag)
    from_date = models.DateField('Enter valid starting date', default=0)
    limit_date = models.DateField('Enter valid ending date', default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    rest_views = models.IntegerField(default=0, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='post_dislikes', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    class Meta:
        ordering = ['date_created', ]


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    profile_pic = models.ImageField(upload_to=f'reviews/')
    content = RichTextField()

    def __str__(self):
        return f"{self.author.first_name}'s comment"


class Client(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='clients/')
    date_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"