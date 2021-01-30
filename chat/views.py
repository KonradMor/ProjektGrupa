# from django.shortcuts import render
from django.views.generic import ListView, CreateView
from chat.models import ChatMessages
# from chat.models import Chats
# from django.db.models import CharField, Model
from django.urls import reverse_lazy


# Create your views here.

class ChatMessagesListView(ListView):
    template_name = "chat.html"
    model = ChatMessages

    # def get_queryset(self)
    #     self.
    #     return


class ChatMessagesCreateView(CreateView):
    template_name = "form.html"
    model = ChatMessages
    fields = ["message", "member_name", "chat_number"]
    success_url = reverse_lazy("chat")
