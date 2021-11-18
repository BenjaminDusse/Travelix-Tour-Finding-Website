from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Category(models.Model):
    category = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='children',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    text = RichTextField()
    image = models.ImageField(upload_to='posts/', default='default.png')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='post_dislikes', blank=True)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return f"{self.author} committed {self.title}"

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    profile_pic = models.ImageField(upload_to='reviews/', default='default.png')
    comment = models.TextField()

    def __str__(self):
        return f"Commented {self.author.name}"

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Social_Network(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Social_Network_Post(models.Model):
    soc_net_name = models.ForeignKey(
        Social_Network,
        on_delete=models.ForeignKey,
        related_name='net'
    )
    link = models.CharField(max_length=500)
    image = models.ImageField(upload_to='social_networks/')

    def __str__(self):
        return self.soc_net_name.name
