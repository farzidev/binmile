from django.urls import path

from .views import IndexView, BlogView, ServicesView, PostSampleView, PostDetailView

app_name = 'posts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('services', ServicesView.as_view(), name='services'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', PostSampleView.as_view(), name='post-sample'),
]
