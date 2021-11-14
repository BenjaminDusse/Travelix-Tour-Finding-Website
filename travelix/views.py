from django.shortcuts import render

from .models import Tag, Category, Rest_area


def home(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    rests = Rest_area.objects.all()
    cheap_rests = Rest_area.objects.filter(price__lt=100)[:4]

    context = {
        'tags': tags,
        'categories': categories,
        'rests': rests[:3],
        'cheap_rests': cheap_rests
    }

    return render(request, 'travelix/index.html', context)


def like_rest(request):
    pass

def dislike_rest(request):
    pass