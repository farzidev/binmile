# from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, FormView, ListView
from django.contrib import messages
from django.db.models import Q

from .models import Post, Category, Form
from .forms import ContactForm


class IndexView(TemplateView):
    template_name = "index.html"


class InsightsView(ListView):
    template_name = "blog.html"
    model = Post

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            # change icontains becaues it does not take spaces in query
            queryset = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__name__icontains=query) |
                Q(category__name__icontains=query) |
                Q(purpose__icontains=query) |
                Q(timestamp__icontains=query)
            ).distinct()
            return queryset
        return Post.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["categories"] = Category.objects.all()
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


# Power Platform View
class PowerPFView(FormView):
    template_name = "powerBI.html"
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


class ContactUsView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "#"
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


class MicrosoftDynamicsView(FormView):
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
