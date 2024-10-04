from django.urls import path

from apps.tasks.views.tag_views import  TagApi

urlpatterns = [
    path('tag/<int:pk>', TagApi.as_view())
]
