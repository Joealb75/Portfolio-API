from django.db import models
from .languageTag import LanguageTag

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=2000)
    deployed = models.BooleanField(default=False)
    tags = models.ManyToManyField(LanguageTag, related_name="projects")


class GitHubStats(models.Model):
    repos = models.IntegerField(null=True, blank=True, default=30)
    YTDcontributions = models.IntegerField(null=True, blank=True, default=431)
    updateDate = models.DateField(auto_now_add=True)