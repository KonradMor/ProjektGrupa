# from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import ChatMessages, Chats
# from chat.models import Chats
# from django.db.models import CharField, Model
from django.urls import reverse_lazy


# Create your views here.

class ChatMessagesListView(ListView):
    template_name = "chat.html"
    model = ChatMessages

    def get_queryset(self):
        self.extra_context = {'chat': Chats.objects.get(pk=self.kwargs['pk'])}
        return ChatMessages.objects.filter(chat_number=self.request.resolver_match.kwargs['pk'])


class ChatMessagesCreateView(CreateView):
    template_name = "form.html"
    model = ChatMessages
    fields = ["message"]
    # success_url = reverse_lazy("user_dashboard")

    def form_valid(self, form):
        form.instance.chat_number = Chats.objects.get(pk=self.kwargs['pk'])
        form.instance.member_name = self.request.user.users
        return super(ChatMessagesCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("chat:chat", kwargs={'pk': self.kwargs['pk']})
