from django.urls import path
from .views import ChatMessagesListView, ChatMessagesCreateView

app_name = 'chat'

urlpatterns = [
    path('', ChatMessagesListView.as_view(), name="chat"),
    path('new/', ChatMessagesCreateView.as_view(), name="new")
]
