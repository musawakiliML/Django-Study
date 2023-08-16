from django.urls import path

from .views import homePageView, HomePageView, AboutPageView

urlpatterns = [
    # path('', homePageView, name='home')
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]