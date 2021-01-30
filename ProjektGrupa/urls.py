"""ProjektGrupa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import (TeamsListView, TeamCreateView, TaskUpdateView,
                        TeamMemberCreateView, TeamMemberDeleteView,
                        TaskDeleteView,
                        )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', TeamsListView.as_view(), name='user_dashboard'),
    path('team_panel/<int:pk>/', include('main.urls')),
    path('team_add/', TeamCreateView.as_view(), name='team_add'),
    path('message/', include('message.urls')),

    path('chat/<int:pk>/', include('chat.urls')),

    path('member_delete/<int:pk>', TeamMemberDeleteView.as_view(), name='member_delete'),
    path('task_delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('task_end/<int:pk>', TaskUpdateView.as_view(), name='task_end'),
    # path('task_end/<int:pk>', TaskUpdateView.as_view(), name='task_end')

]
