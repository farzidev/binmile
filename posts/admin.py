from django.contrib import admin, messages
from django.db.models import IntegerField
from django.db.models.functions import Cast

from .models import Post, Category, Form, Author, AboutUs, MicrosoftDynamics365, PowerPlatform, ServiceNow


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
admin.site.register(AboutUs)
admin.site.register(ServiceNow)


@admin.register(MicrosoftDynamics365)
class MicrosoftDynamics365Admin(admin.ModelAdmin):
    list_display = ('title', 'show_order')

    def show_order(self, obj):
        return obj.order if obj.order else "Not Showing"

    show_order.short_description = "Order"

    def save_model(self, request, obj, form, change):
        if 'order' in form.changed_data:
            changed_order = form.cleaned_data.get('order')
            messages.info(request, f'Order changed to "{changed_order}" for Solution - "{obj.title}"')
        super().save_model(request, obj, form, change)


@admin.register(PowerPlatform)
class PowerPlatformAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_order')

    def show_order(self, obj):
        return obj.order if obj.order else "Not Showing"

    show_order.short_description = "Order"

    def save_model(self, request, obj, form, change):
        if 'order' in form.changed_data:
            changed_order = form.cleaned_data.get('order')
            messages.info(request, f'Order changed to "{changed_order}" for Point - "{obj.title}"')
        super().save_model(request, obj, form, change)


@admin.register(Form)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company")
    list_filter = ("timestamp",)
    search_fields = ("name", "email", "message", "company")
