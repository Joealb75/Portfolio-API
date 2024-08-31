from django.db import models

class LanguageTag(models.Model):
    name = models.CharField(max_length=20, unique=True)

class Project(models.model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=2000)
    deployed = models.BooleanField(default=False)
    tags = models.ManyToManyField(LanguageTag, related_name="projects")


class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="projectImages/")
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True, null=True)