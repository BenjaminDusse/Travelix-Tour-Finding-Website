from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Post, Comment, Category, Tag, Social_Network_Post, Social_Network
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['social_nets'] = Social_Network.objects.all()
        context['posts'] = Post.objects.all().order_by('-date_created')[:3]
        context['soc_posts'] = Social_Network_Post.objects.all()[:12]
        return context


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/blog_detail.html'
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post'] = Post.objects.get(id=2)
#         context['categories'] = Category.objects.all()
#         context['tags'] = Tag.objects.all()
#         context['social_nets'] = Social_Network.objects.all()
#         context['soc_posts'] = Social_Network_Post.objects.all()[:9]
#         return context

def post_detail(request, pk):
    posts = Post.objects.all().order_by('-date_created')[:3]
    post = Post.objects.get(pk=pk)
    categories = post.tags.all()
    tags = Tag.objects.all()
    rel_posts = Post.objects.all()[:2]
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=self.pk)

    context = {
        'posts': posts,
        'post': post,
        'form': form,
        'categories': categories,
        'tags': tags,
        'rel_posts': rel_posts
    }

    return render(request, 'blog/blog_detail.html', context)
