import string

from django.utils.text import slugify
from django.utils.crypto import get_random_string


def create_post_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug

    Post = instance.__class__
    qs = Post.objects.filter(slug=slug[:255])  # all 255 chars

    if qs.exists():
        num = get_random_string(length=5, allowed_chars=string.digits)
        # ensuring that total chars are 255
        new_slug = "%s-%s" % (slug[:249], num)
        return create_post_slug(instance, new_slug=new_slug)
    return slug
