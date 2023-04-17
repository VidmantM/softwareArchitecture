from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView
)
from . import views
urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='post-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='post-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='post-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='post-delete'),
]
