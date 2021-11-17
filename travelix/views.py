from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }

    return render(request, 'travelix/about.html', context)


class OfferListView(ListView):
    model = Rest_area
    template_name = 'travelix/offers.html'
    context_object_name = 'rests'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rests'] = Rest_area.objects.all().order_by('price')
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class OfferDetailView(DetailView):
    model = Rest_area
    context_object_name = 'rests'


def offer_detail(request, pk):
    rest_area = Rest_area.objects.get(pk=pk)
    categories = Category.objects.all()
    related_offers = Rest_area.objects.filter(price__exact=99)[:2]

    context = {
        'categories': categories,
        'rest_area': rest_area,
        'bottom_images': rest_area.bottom_images,
        'rel_offers': related_offers.filter(price__exact=99)[:2]
    }

    return render(request, 'travelix/offer_detail.html', context)


def contact(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }

    return render(request, 'travelix/contact.html', context)


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
