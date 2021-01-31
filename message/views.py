from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Messages
from accounts.models import Users
from main.models import TeamMembers
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class MessageListView(LoginRequiredMixin, ListView):
    model = Messages
    template_name = "message.html"

    def get_queryset(self):
        self.extra_context = {'to': Messages.objects.filter(id_user_from=self.request.user.users)}
        return Messages.objects.filter(id_user_to=self.request.user.users)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Messages
    template_name = "form.html"
    fields = ['content', 'id_user_to']
    success_url = reverse_lazy("MessListView")

    def form_valid(self, form):
        form.instance.id_user_from = self.request.user.users
        return super(MessageCreateView, self).form_valid(form)


class ContentCreateView(LoginRequiredMixin, CreateView):
    model = Messages
    template_name = "form.html"
    fields = ['content']
    success_url = reverse_lazy("MessListView")

    def form_valid(self, form):
        form.instance.id_user_from = self.request.user.users
        user_pk = TeamMembers.objects.get(pk=self.request.resolver_match.kwargs['pk']).member_name
        form.instance.id_user_to = Users.objects.get(pk=user_pk.id)
        return super(ContentCreateView, self).form_valid(form)
