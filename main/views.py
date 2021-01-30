from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Teams, TeamMembers, Tasks
from accounts.models import Users
# Create your views here.


def View_to_change(request):
    context = {'welcome': "Hello on our site"}
    return render(request, template_name='index.html', context=context)


class TeamsListView(LoginRequiredMixin, ListView):
    # model = TeamMembers
    model = Teams
    template_name = 'teams_list.html'

    def get_queryset(self):
        # for record in TeamMembers.objects.filter(member_name=self.request.user.id):
        #     return record.member_name
        # return TeamMembers.objects.filter(member_name=self.request.user.id)
        # self.extra_context = {'members': TeamMembers.objects.filter(team_name=)}
        # filter2 = TeamMembers.objects.filter(team_name__in=filter1)
        manager_filter = Teams.objects.filter(manager=self.request.user.id-1)
        filter1 = TeamMembers.objects.filter(member_name=self.request.user.id)
        if self.request.user.is_superuser:
            return Teams.objects.all()
        elif len(manager_filter) > 0:
            all_teams = [team for team in manager_filter] + [i.team_name for i in filter1]
            return [team for team in all_teams]
        else:
            return [i.team_name for i in filter1]


class TeamMembersListView(LoginRequiredMixin, ListView):
    model = TeamMembers
    template_name = 'team_members_list.html'

    def get_queryset(self):
        self.extra_context = {'tasks': Tasks.objects.filter(team_name=self.request.resolver_match.kwargs['pk'], actual_end_date__isnull=True)
                              , 'team': Teams.objects.filter(id=self.request.resolver_match.kwargs['pk']).first()
                              # ,'manager': Teams.objects.get(team_name=self.request.resolver_match.kwargs['pk']).manager.id
                              , 'user_id': Users.objects.get(pk=self.request.user.id).id-1
                              }
        return TeamMembers.objects.filter(team_name=self.request.resolver_match.kwargs['pk'])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     if self.request.user.id == Teams.objects.get(team_name=self.request.resolver_match.kwargs['pk']).manager.id:
    #         context.update({'is_manager': 1})
    #     return context


class TaskListView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks_list.html'

    def get_queryset(self):
        self.extra_context = {'members': TeamMembers.objects.filter(team_name=self.request.resolver_match.kwargs['pk'])}
        return Tasks.objects.filter(team_name=self.request.resolver_match.kwargs['pk'])


class MemberTasksListView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks_list.html'

    def get_queryset(self):
        return Tasks.objects.filter(team_name=self.request.resolver_match.kwargs['pk'])


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'form.html'
    fields = ['actual_end_date']
    # success_url = reverse_lazy('user_dashboard')

    def get_success_url(self):
        filter1 = Tasks.objects.get(pk=self.request.resolver_match.kwargs['pk']).team_name.id
        return reverse_lazy("team_dashboard", kwargs={'pk': filter1})


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = 'form.html'
    fields = ['task_name', 'member_name', 'plan_end_date']
    # success_url = reverse_lazy('user_dashboard')

    def form_valid(self, form):
        form.instance.team_name = Teams.objects.get(pk=self.kwargs['pk'])
        return super(TaskCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("team_dashboard", kwargs={'pk': self.kwargs['pk']})

    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        filter1 = TeamMembers.objects.filter(team_name=self.request.resolver_match.kwargs['pk'])
        filter2 = Teams.objects.filter(id=self.request.resolver_match.kwargs['pk'])
        filter3 = [i.member_name.user for i in filter1] + [i.manager.user for i in filter2]
        form.fields['member_name'].queryset = Users.objects.filter(user__in=filter3)
        return form

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(TodoView, self).form_valid(form)


class ManagerChangeView(LoginRequiredMixin, UpdateView):
    model = Teams
    template_name = 'form.html'
    fields = ['manager']
    # success_url = reverse_lazy('user_dashboard')

    def get_success_url(self):
        return reverse_lazy("team_dashboard", kwargs={'pk': self.kwargs['pk']})


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Teams
    template_name = 'form.html'
    fields = '__all__'
    success_url = reverse_lazy('user_dashboard')


class TeamMemberCreateView(LoginRequiredMixin, CreateView):
    model = TeamMembers
    template_name = 'form.html'
    fields = ['member_name']
    # success_url = reverse_lazy('user_dashboard')

    def form_valid(self, form):
        form.instance.team_name = Teams.objects.get(pk=self.kwargs['pk'])
        return super(TeamMemberCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("team_dashboard", kwargs={'pk': self.kwargs['pk']})


class TeamMemberDeleteView(LoginRequiredMixin, DeleteView):
    model = TeamMembers
    template_name = 'delete.html'
    # success_url = reverse_lazy('user_dashboard')

    def get_success_url(self):
        filter1 = TeamMembers.objects.get(pk=self.request.resolver_match.kwargs['pk']).team_name.id
        return reverse_lazy("team_dashboard", kwargs={'pk': filter1})


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    Model = Teams
    template_name = 'delete.html'
    success_url = reverse_lazy('user_dashboard')

    def get_queryset(self):
        return Teams.objects.filter(pk=self.request.resolver_match.kwargs['pk'])


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'delete.html'
    # success_url = reverse_lazy('user_dashboard')

    def get_success_url(self):
        filter1 = Tasks.objects.get(pk=self.request.resolver_match.kwargs['pk']).team_name.id
        return reverse_lazy("team_dashboard", kwargs={'pk': filter1})
