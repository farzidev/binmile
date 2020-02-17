from django.urls import path

from .views import IndexView, BlogView, ServicesView

app_name = 'posts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('services', ServicesView.as_view(), name='services'),
]
