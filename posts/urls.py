from django.urls import path

from .views import (
    IndexView, BlogView, ServicesView, PostSampleView, PostDetailView,
    AboutUsView, ContactUsView, MicrosoftCrmView
)

app_name = 'posts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('services', ServicesView.as_view(), name='services'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', PostSampleView.as_view(), name='post-sample'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('microsoft-crm/', MicrosoftCrmView.as_view(), name='microsoft-crm'),
]
