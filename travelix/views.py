from django.shortcuts import render

from .models import Tag, Category, Rest_area, Client


def home(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    rests = Rest_area.objects.all()
    cheap_rests = Rest_area.objects.filter(price__lt=100)[:4]
    client_tems = Client.objects.all()[:4]
    trending = Rest_area.objects.all().order_by('likes')

    context = {
        'tags': tags,
        'categories': categories,
        'rests': rests[:3],
        'cheap_rests': cheap_rests,
        'clients': client_tems[:4],
        'trending': trending[:8]
    }

    return render(request, 'travelix/index.html', context)


def about(request):
    context = {}

    return render(request, 'travelix/about.html', context)


def like_rest(request):
    pass


def dislike_rest(request):
    pass


def base(request):
    tags = Tag.objects.all()

    context = {
        'tags': tags
    }
    return render(request, 'base.html', context)
