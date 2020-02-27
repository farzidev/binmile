# from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from .models import Post, Category


class IndexView(TemplateView):
    template_name = "index.html"


class BlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
        context["posts"] = Post.objects.all()
        return context


class ServicesView(TemplateView):
    template_name = "service.html"


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = "binmile_article.html"


class AboutUsView(TemplateView):
    template_name = "aboutUs.html"


class ContactUsView(TemplateView):
    template_name = "contact.html"


class MicrosoftCrmView(TemplateView):
    template_name = "microsoftCRM.html"
