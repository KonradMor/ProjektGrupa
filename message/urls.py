from django.urls import path
from .views import MessageListView, MessageCreateView
urlpatterns = [
    path('', MessageListView.as_view(), name="MessListView"),
    path('create/', MessageCreateView.as_view(), name="MessCreateView")
]