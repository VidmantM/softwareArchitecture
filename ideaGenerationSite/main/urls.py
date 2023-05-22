from django.urls import path
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView, project_find, like_project, liked_projects
)
from . import views
urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='post-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='post-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='post-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='post-delete'),
    path('project/suggestions/', project_find, name='post-suggest'),
    path('like_project/<int:project_id>/', like_project, name='like-project'),
    path('liked_projects/', liked_projects, name='liked-projects'),
    path('project/approval/', views.project_approval, name='project_approval'),
    path('project/approve/<int:project_id>/', views.approve_project, name='approve_project'),
    path('project/deny/<int:project_id>/', views.deny_project, name='deny_project'),
]
