from django.urls import path
from .views import MessageListView, MessageCreateView, ContentCreateView


urlpatterns = [
    path('', MessageListView.as_view(), name="MessListView"),
    path('create/', MessageCreateView.as_view(), name="MessCreateView"),
    path('create_to/<int:pk>', ContentCreateView.as_view(), name='message_to')
]