from typing import Any
from django.shortcuts import redirect, render
from django.views import View
from blog.forms import ShareForm
from .models import Post, Category
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.core.mail import send_mail


def list_view(request):
    posts = Post.objects.filter(status=Post.StatusChoices.PUBLISHED, )
    return render(request, 'list.html', {'posts': posts})


def detail_view(request, year, month, day, slug):
    post = get_object_or_404(Post, status=Post.StatusChoices.PUBLISHED,
                             publish_time__year=year,
                             publish_time__month=month,
                             publish_time__day=day, slug=slug)
    return render(request, 'detail.html', {'post': post})


class CategoryListView(TemplateView):
    template_name = 'category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = kwargs['category_slug']
        category = get_object_or_404(Category, title=category_slug)
        posts = Post.objects.filter(category=category)
        context['category'] = category
        context['posts'] = posts
        return context


class SharePost(View):
    def get(self, request, pk):
        form = ShareForm()
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'share.html', {'form': form, 'post': post}, )

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = ShareForm(request.POST)
        if form.is_valid():
            send_mail(
                "sharing a Post".format(post.title),
                form.cleaned_data.get('comment'),
                form.cleaned_data.get('email'),
                [form.cleaned_data.get('to')],
                fail_silently=False,
            )
        else:
            return render(request, 'share.html', {'form': form,
                                                  'post': post})


class NewestPostViews(TemplateView):
    template_name = 'newest_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newest_posts = Post.objects.filter(status=Post.StatusChoices.PUBLISHED)[:5]
        context['newest_posts'] = newest_posts
        return context