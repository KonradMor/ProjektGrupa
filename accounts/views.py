from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import SignUpForm


# Create your views here.


class MySignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('user_dashboard')


class MyLoginView(LoginView):
    template_name = 'form.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('user_dashboard')
