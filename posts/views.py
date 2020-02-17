# from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from .models import Post


class IndexView(TemplateView):
    template_name = "index.html"


class BlogView(TemplateView):
    template_name = "blog.html"


class ServicesView(TemplateView):
    template_name = "service.html"


class PostSampleView(TemplateView):
    template_name = "binmile_article.html"


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = "binmile_article.html"
