from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Messages
from django.urls import reverse_lazy
# Create your views here.

class MessageListView(ListView):
    model = Messages
    template_name = "message.html"

class MessageCreateView(CreateView):
    model = Messages
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy("MessListView")