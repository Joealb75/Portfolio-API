from django.db import models
from .project import Project

class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="projectImages/")
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    caption = models.CharField(max_length=255, blank=True, null=True)