from django.db import models
from django.urls import reverse_lazy
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from .utils import create_post_slug


def post_img_dir(instance, filename):
    return f"posts/{filename}"


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    thumbnail_img = models.ImageField(upload_to=post_img_dir)
    highlight = models.TextField()
    tags = models.TextField()

    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
        blank=True, null=True)

    PURPOSES = (
        ('BG', 'Blog'),
        ('CS', 'Case Study'),
    )
    purpose = models.CharField(max_length=2, choices=PURPOSES)

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy('posts:detail', kwargs={'slug': self.slug})


@receiver(pre_save, sender=Post)
def pre_save_post_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_post_slug(instance)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.IntegerField(validators=[MinValueValidator(0)],
        null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
