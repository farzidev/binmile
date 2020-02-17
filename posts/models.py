from django.db import models

from ckeditor.fields import RichTextField


def post_img_dir(instance, filename):
    return f"posts/{filename}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    thumbail_img = models.ImageField(upload_to=post_img_dir)
    highlight = models.TextField()
    tags = models.TextField()

    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
        blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Form(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    query = models.TextField()

    def __str__(self):
        return str(self.name)
