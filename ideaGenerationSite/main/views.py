import random
from collections import Counter
import sys

from django.contrib import messages

sys.path.append("..")
from django.shortcuts import redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.decorators import login_required
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django_filters.views import FilterView

from users.models import Profile
from users.models import Weight
from users.models import Project
from .filters import ProjectFilter
import django_filters
from .forms import WeightFormulaForm


def home(request):
    return render(request, 'main/home.html')

@login_required
def liked_projects(request):
    user_profile = request.user.profile
    liked_projects = user_profile.liked_projects.all()
    context = {'liked_projects': liked_projects}
    return render(request, 'main/liked_projects.html', context)


@login_required
def like_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    user_profile = request.user.profile
    user_profile.liked_projects.add(project)
    project.likes += 1
    project.save()
    liked_projects = user_profile.liked_projects.all()
    context = {'liked_projects': liked_projects}
    return render(request, 'main/liked_projects.html', context)

class ProjectListView(FilterView):
    model = Project
    template_name = 'main/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    filterset_class = ProjectFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        filtered_queryset = self.filterset_class(self.request.GET, queryset=queryset).qs

        # Filter by approved projects
        approved_queryset = filtered_queryset.filter(approved=True)

        if len(approved_queryset) == 0:
            messages.warning(self.request, "No approved projects found.")

        return approved_queryset


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


# expand later
def skill_match(request):
    user_profile = Profile.objects.get(user=request.user)
    all_projects = Project.objects.all()
    matching_projects = []
    for project in all_projects:
        matching_skills_count = 0
        for skill in project.skills.all():
            if skill in user_profile.skills.all():
                matching_skills_count += 1
        if matching_skills_count > 0:
            matching_projects.append((project, matching_skills_count))

    # for project, matching_skills_count in matching_projects:
    #     print(f"Project: {project.title}")
    #     print(f"Matching Skills: {matching_skills_count}")
    #     print("\n")
    return matching_projects


def skill_unmatch(request):
    user_profile = Profile.objects.get(user=request.user)
    all_projects = Project.objects.all()
    non_matching_projects = []
    for project in all_projects:
        matching_skills_count = 0
        for skill in project.skills.all():
            if skill in user_profile.skills.all():
                matching_skills_count += 1
        if matching_skills_count == 0:  # Only consider projects with no matching skills
            non_matching_projects.append(project)
    return non_matching_projects


@login_required
def project_find(request):
    matching_projects = skill_match(request)
    prev_recommendations = request.session.get('prev_recommendations', [])
    unique_prev_recommendations = list(set(prev_recommendations))

    if request.method == 'POST':
        form = WeightFormulaForm(request.POST)
        if form.is_valid():
            weight_formula = form.cleaned_data['weight_formula'].formula
            project_weights = []

            # For matching
            for project, matching_skills_count in matching_projects:
                weight = round(eval(weight_formula) * random.uniform(1, 3), 2)
                project_weights.append((project, weight))

            weighted_projects = [project for project, weight in project_weights]
            weights = [weight for project, weight in project_weights]

            filtered_weighted_projects = [p for p in weighted_projects if p.id not in unique_prev_recommendations]
            filtered_weights = [w for p, w in zip(weighted_projects, weights) if
                                p.id not in unique_prev_recommendations]

            if len(filtered_weighted_projects) == 0:
                request.session['prev_recommendations'] = []
                messages.warning(request, "No new recommendations available.")
                return redirect('home')

            selected_project = random.choices(filtered_weighted_projects, weights=filtered_weights, k=1)[0]
            unique_prev_recommendations.append(selected_project.id)
            request.session['prev_recommendations'] = unique_prev_recommendations

            context = {
                'post_id': selected_project.id
            }

            if context['post_id']:
                project = get_object_or_404(Project, pk=context['post_id'])
                context['post'] = project

            return render(request, 'main/suggestion.html', context)
    else:
        form = WeightFormulaForm()

    context = {
        'form': form,
    }

    return render(request, 'main/project_find.html', context)

@staff_member_required  # Ensures only staff members can access this view
def project_approval(request):
    projects = Project.objects.filter(approved=False)  # Get unapproved projects
    context = {'projects': projects}
    return render(request, 'main/project_approval.html', context)

@staff_member_required  # Ensures only staff members can access this view
def approve_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.approved = True
    project.save()
    return redirect('project_approval')

@staff_member_required  # Ensures only staff members can access this view
def deny_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('project_approval')