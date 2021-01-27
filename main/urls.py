from django.urls import path
from .views import (TeamMembersListView, TaskListView, TaskUpdateView,
                    TaskCreateView, TaskDeleteView, ManagerChangeView,
                    TeamCreateView, TeamMemberCreateView, TeamMemberDeleteView,
                    TeamDeleteView, MemberTasksListView
                    )


urlpatterns = [
    path('', TeamMembersListView.as_view(), name='team_members'),
    path('team_add', TeamCreateView.as_view(), name='team_add'),
    path('team_delete/', TeamDeleteView.as_view(), name='team_delete'),
    path('tasks/', TaskListView.as_view(), name='tasks_list'),
    path('task_end/<int:pk>', TaskUpdateView.as_view(), name='task_end'),
    path('task_add/', TaskCreateView.as_view(), name='task_add'),
    path('task_delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('manager_change/', ManagerChangeView.as_view(), name='manager_change'),
    path('member_add/', TeamMemberCreateView.as_view(), name='member_add'),
    path('member_delete/<int:pk>', TeamMemberDeleteView.as_view(), name='member_delete'),
    path('member_tasks/<int:pk>', MemberTasksListView.as_view(), name='member_tasks')
]
