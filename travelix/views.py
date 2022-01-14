from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

from blog.models import Post
from .models import Tag, Category, Rest_area, Client
from .forms import CommentForm


# Home search
def search(request):
    tags = Tag.objects.all()
    posts = Post.objects.all().order_by('-date_created')[:3]


    if 'q' in request.GET:
        q = request.GET['q']
        data = Rest_area.objects.filter(title__icontains=q)
    else:
        data = Rest_area.objects.all()

    context = {
        'data': data,
        'tags': tags,
        'posts': posts
    }
    return render(request, 'travelix/search.html', context)


def home(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    rests = Rest_area.objects.all()
    cheap_rests = Rest_area.objects.filter(price__lt=100)
    client_tems = Client.objects.all()[:4]
    trending = Rest_area.objects.all().order_by('likes')
    posts = Post.objects.all().order_by('-date_created')[:3]

    context = {
        'tags': tags,
        'categories': categories,
        'rests': rests[:3],
        'cheap_rests': cheap_rests[:4],
        'clients': client_tems[:4],
        'trending': trending[:8],
        'posts': posts[:3]
    }

    return render(request, 'travelix/index.html', context)


def about(request):
    tags = Tag.objects.all()
    posts = Post.objects.all().order_by('-date_created')[:3]

    context = {
        'tags': tags,
        'posts': posts
    }

    return render(request, 'travelix/about.html', context)


class OfferListView(ListView):
    model = Rest_area
    template_name = 'travelix/offers.html'
    context_object_name = 'rests'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rests'] = Rest_area.objects.all().order_by('price')
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['posts'] = Post.objects.all().order_by('-date_created')[:3]

        return context


# class OfferDetailView(DetailView):
#         model = Rest_area
#         template_name = 'travelix/offer_detail.html'
#         context_object_name = 'rests'


def offer_detail(request, pk):
    rest_area = Rest_area.objects.get(pk=pk)
    categories = Category.objects.all()
    related_offers = Rest_area.objects.all()[:2]
    bottom_images = rest_area.bottom_images
    tags = rest_area.tags.all()
    posts = Post.objects.all().order_by('-date_created')[:3]
    form = CommentForm()
    comments = rest_area.comments.all()
    rest_map_url = rest_area.map_url

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.rest_area = rest_area
            form.save()

            return redirect('travelix:offer_detail.html', pk=rest_area.pk)
        else:
            form = CommentForm()

    context = {
        'categories': categories,
        'rest_area': rest_area,
        'bottom_images': bottom_images,
        'rel_offers': related_offers,
        'tags': tags,
        'form': form,
        'rest_map_url': rest_map_url,
        'comments': comments,
        'posts': posts
    }

    return render(request, 'travelix/offer_detail.html', context)


def contact(request):
    posts = Post.objects.all().order_by('-date_created')[:3]
    tags = Tag.objects.all()



    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        context = {
            'message_name', message_name,
            'message_email', message_email,
            'message', message
        }

        send_mail(
            message_name,           # subject
            message,            # message
            message_email,                # from email
            ['abduhakimovfazliddin2002@gmail.com']            # To email,

        )

        return render(request, 'travelix/contact.html', context)

    context = {
        'tags': tags,
        'posts': posts
    }

    return render(request, 'travelix/contact.html', context)


def base(request):
    posts = Post.objects.all().order_by('-date_created')[:3]
    tags = Tag.objects.all()

    context = {
        'tags': tags,
        'posts': posts
    }
    return render(request, 'base.html', context)


@login_required(login_url='accounts:login')
def like_rest(request, pk):
    post = get_object_or_404(Rest_area, id=request.POST.get('rest_area_id'))
    post.likes.add(request.user)
    return redirect('travelix:offer_detail', pk)


@login_required(login_url='accounts:login')
def dislike_rest(request, pk):
    post = get_object_or_404(Rest_area, id=request.POST.get('rest_area_id'))
    post.dislikes.add(request.user)
    return redirect('travelix:offer_detail', pk)


def book(request):
    tags = Tag.objects.all()
    posts = Post.objects.all().order_by('-date_created')[:3]

    context = {
        'tags': tags,
        'posts': posts
    }
    return render(request, 'travelix/book.html', context)
