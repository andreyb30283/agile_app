from django.urls import path

from apps.project.views.project_views import ProcjectsApi
from apps.tasks.views.tag_views import  TagApi

urlpatterns = [
    path('project/<int:pk>', ProcjectsApi.as_view())
]
