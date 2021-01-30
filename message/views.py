from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MessageListView(LoginRequiredMixin, ListView):
    model = Messages
    template_name = "message.html"

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Messages
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("MessListView")