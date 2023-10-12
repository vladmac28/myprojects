from django.urls import path
from .views import IndexPageView


urlpatterns = [
    path('menu/',  IndexPageView.as_view(), name='index'),
]