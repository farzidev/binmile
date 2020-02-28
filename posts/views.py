# from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, FormView
from django.contrib import messages

from .models import Post, Category, Form
from .forms import ContactForm


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = self.get_object().category
        context["related_posts"] = Post.objects.filter(
            category=category).order_by("-id")[:3]
        return context


class AboutUsView(TemplateView):
    template_name = "aboutUs.html"


class ContactUsView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "#contactForm"
    page = "contact"

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update({'page': self.page})
        return kwargs

    def form_valid(self, form):
        form.cleaned_data.pop('captcha')
        Form.objects.get_or_create(**form.cleaned_data)
        messages.success(self.request, "Thanks for submitting the form.")
        form.send_mail()
        return super().form_valid(form)


class MicrosoftCrmView(FormView):
    template_name = "microsoftCRM.html"
    form_class = ContactForm
    success_url = "#consultForm"
    page = "microsoft"

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update({'page': self.page})
        return kwargs

    def form_valid(self, form):
        Form.objects.get_or_create(**form.cleaned_data)
        messages.success(self.request, "Thanks for submitting the form.")
        form.send_mail()
        return super().form_valid(form)
