import random

from django.db import models
from django.urls import reverse_lazy
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

from .utils import create_post_slug


def post_img_dir(instance, filename):
    return f"posts/{filename}"


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True,
        blank=True)

    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    thumbnail_img = models.ImageField(upload_to=post_img_dir)
    highlight = models.TextField(max_length=200, help_text='Maximum characters allowed are 200')
    tags = models.TextField()
    read_minutes = models.PositiveIntegerField(
        help_text="Time needed in minutes to read this Insight", blank=True)

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

    def save(self, *args, **kwargs):
        if not self.thumbnail_img:
            return

        if not self.read_minutes:
            self.read_minutes = random.randrange(5, 10)

        super().save()
        photo = Image.open(self.thumbnail_img)
        photo = photo.resize((412, 300), Image.ANTIALIAS)
        photo.save(self.thumbnail_img.path)


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


class AboutUs(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    linkedin_url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='aboutus')

    # (f'{i}', f'{i}') for i in range(1, AboutUs.objects.count())
    ORDERS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    )
    order = models.CharField(choices=ORDERS, max_length=2, blank=True, null=True)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
        ordering = ('order',)

    def __str__(self):
        return "%s - %s" % (self.name, self.title)

    def save(self, *args, **kwargs):
        if not self.image:
            return

        super().save()
        photo = Image.open(self.image)
        photo = photo.resize((1133, 1163), Image.ANTIALIAS)
        photo.save(self.image.path)

    def clean(self, *args, **kwargs):
        if self.order:
            qs = self.__class__.objects.filter(order=self.order).exclude(pk=self.pk)
            if qs.exists():
                url = reverse_lazy(f'admin:posts_aboutus_change', kwargs={'object_id': qs.first().id})
                print(url)
                raise ValidationError(
                    {"order": mark_safe(
                        f"Solution with this order already exists, you can change it <a target='_blank' href='{url}'>here</a>."
                    )}
                )
        return super().clean(*args, **kwargs)


class ServiceNow(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name = 'ServiceNow'
        verbose_name_plural = 'ServiceNow'

    def __str__(self):
        return self.title


class MicrosoftDynamics365(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=180)

    ORDERS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    )
    order = models.CharField(choices=ORDERS, max_length=2, blank=True, null=True)

    PURPOSES = (
        ('SS', 'Solutions'),
    )
    purpose = models.CharField(choices=PURPOSES, max_length=2, default='SS')

    def __str__(self):
        return "%s - %s" % (self.title, self.get_purpose_display())

    class Meta:
        verbose_name = 'Microsoft Dynamics 365'
        verbose_name_plural = 'Microsoft Dynamics 365'
        ordering = ('order',)

    def clean(self, *args, **kwargs):
        if self.order:
            qs = self.__class__.objects.filter(order=self.order).exclude(pk=self.pk)
            if qs.exists():
                url = reverse_lazy(f'admin:posts_microsoftdynamics365_change', kwargs={'object_id': qs.first().id})
                print(url)
                raise ValidationError(
                    {"order": mark_safe(
                        f"Solution with this order already exists, you can change it <a target='_blank' href='{url}'>here</a>."
                    )}
                )
        return super().clean(*args, **kwargs)


class PowerPlatform(models.Model):
    title = models.CharField(max_length=150)

    ORDERS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    order = models.CharField(choices=ORDERS, max_length=2, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)

    def clean(self, *args, **kwargs):
        if self.order:
            qs = self.__class__.objects.filter(order=self.order).exclude(pk=self.pk)
            if qs.exists():
                url = reverse_lazy(f'admin:posts_powerplatform_change', kwargs={'object_id': qs.first().id})
                print(url)
                raise ValidationError(
                    {"order": mark_safe(
                        f"Point with this order already exists, you can change it <a target='_blank' href='{url}'>here</a>."
                    )}
                )
        return super().clean(*args, **kwargs)


class CareerGallery(models.Model):
    image = models.ImageField(upload_to='gallery')

    ORDERS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    )
    order = models.CharField(choices=ORDERS, max_length=2, blank=True, null=True)

    def __str__(self):
        return self.image.name


class JobProfile(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)

    EXPERIENCE_YEARS = ((f'{i} - {i + 1}', f'{i} - {i + 1}') for i in range(0, 10))
    experience_years = models.CharField(choices=EXPERIENCE_YEARS, max_length=10)
    positions = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TechnologyPartner(models.Model):
    image = models.ImageField(upload_to='partners')

    def __str__(self):
        return self.image.name


class Form(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.BigIntegerField(validators=[MinValueValidator(0)],
        null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
