import sys

from django_filters import FilterSet, CharFilter, ModelChoiceFilter

sys.path.append("..")
from .models import *
from users.models import *

import django_filters

class ProjectFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    skills = ModelChoiceFilter(queryset=Skill.objects.all(), label='Skills')


    class Meta:
        model = Project
        fields = ["title", "skills"]