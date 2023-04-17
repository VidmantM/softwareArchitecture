from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
import sys

from django_filters.views import FilterView

sys.path.append("..")
from users.models import Project
from .filters import ProjectFilter
import django_filters

def home(request):
    return render(request, 'main/home.html')


class ProjectListView(FilterView):
    model = Project
    template_name = 'main/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    filterset_class = ProjectFilter  # Add this line to specify the filter class to be used


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'skills']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'description', 'skills']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})