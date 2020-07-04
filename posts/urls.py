from django.urls import path

from .views import (
    IndexView, InsightsView, ServicesView, PostDetailView,
    AboutUsView, ContactUsView, MicrosoftDynamicsView, PowerPFView, CareerView, QualityView
)

app_name = 'posts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('insights/', InsightsView.as_view(), name='insights'),
    path('services', ServicesView.as_view(), name='services'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('microsoft-dynamics-365/', MicrosoftDynamicsView.as_view(), name='microsoft-dynamics-365'),
    path('power-platform/', PowerPFView.as_view(), name='power-platform'),
    path('career/', CareerView.as_view(), name='career'),
    path('quality/', QualityView, name='quality'),
]
