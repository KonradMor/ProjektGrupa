from django.urls import path
from .views import (TeamMembersListView, TaskListView, TaskUpdateView,
                    TaskCreateView, TaskDeleteView, ManagerChangeView,
                    TeamCreateView, TeamMemberCreateView, TeamMemberDeleteView,
                    TeamDeleteView, MemberTasksListView
                    )


urlpatterns = [
    path('', TeamMembersListView.as_view(), name='team_dashboard'),
    path('team_delete/', TeamDeleteView.as_view(), name='team_delete'),
    # path('tasks/', TaskListView.as_view(), name='tasks_list'),
    # path('task_end/<int:pk>', TaskUpdateView.as_view(), name='task_end'),
    path('task_add/', TaskCreateView.as_view(), name='task_add'),
    # path('task_delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('manager_change/', ManagerChangeView.as_view(), name='manager_change'),
    path('member_add/', TeamMemberCreateView.as_view(), name='member_add'),
    # path('member_delete/', TeamMemberDeleteView.as_view(), name='member_delete'),
    # path('member_tasks/', MemberTasksListView.as_view(), name='member_tasks') jak to zrobic, zeby korzystac z dwoch pk tj. pk zespolu i pk osoby
]
