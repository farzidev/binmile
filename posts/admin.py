from django.contrib import admin

from .models import Post, Category, Form, Author


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "get_purpose")
    list_filter = ("category", "timestamp", "purpose", "read_minutes")
    search_fields = ("title", "content", "read_minutes")

    def get_purpose(self, obj):
        return obj.get_purpose_display()

    get_purpose.short_description = "Purpose"


admin.site.register(Category)
admin.site.register(Author)


@admin.register(Form)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company")
    list_filter = ("timestamp",)
    search_fields = ("name", "email", "message", "company")
