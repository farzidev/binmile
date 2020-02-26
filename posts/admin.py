from django.contrib import admin

from .models import Post, Category, Form


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    list_filter = ("category", "timestamp")
    search_fields = ("title", "content")


admin.site.register(Category)
admin.site.register(Form)
