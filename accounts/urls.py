from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import MySignUpView, MyLoginView, MyPasswordChangeView

app_name = 'accounts'
urlpatterns = [
    path('signup/', MySignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('change_password', MyPasswordChangeView.as_view(), name='change-password')
]
