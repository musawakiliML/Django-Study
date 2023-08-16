from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('messageboard/', HomePageView.as_view(), name='messageboard')
]