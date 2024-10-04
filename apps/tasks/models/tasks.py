from django.contrib.auth.models import User
from django.db import models

from apps.project.models.project import Project
from apps.tasks.choices.priority import Priority
from apps.tasks.choices.statuses import Statuses
from apps.tasks.models.tag import Tag
from apps.tasks.utils.set_datetime import last_day_of_month


class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=Statuses.choices, default=Statuses.New)
    priority = models.SmallIntegerField(choices=Priority.choices, default=Priority.MEDIUM[0])
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)