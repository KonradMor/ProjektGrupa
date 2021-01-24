from django.urls import path
from .views import View_to_change

urlpatterns = [
    path('', View_to_change, name='home')
]