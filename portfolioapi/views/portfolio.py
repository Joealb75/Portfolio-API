from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from portfolioapi.models import Project, LanguageTag, Image

class LanguageTagSerializer(serializers.Serializer):
    class Meta:
        model = LanguageTag
        fields = '__all__'

class LanguageTagViewSet(ViewSet):

    def create(self, request):
        return
    
    def retrieve(self, request, pk=None):
        return
    
    def update(self, request, pk=None):
        return
    
    def destroy(self, request, pk=None):
        return
    
    def list(self, request):
        return



class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectViewSet(ViewSet):

    def create(self, request):
        return
    
    def retrieve(self, request, pk=None):
        return
    
    def update(self, request, pk=None):
        return
    
    def destroy(self, request, pk=None):
        return
    
    def list(self, request):
        return
    

class ImageSerializer(serializers.Serializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageViewSet(ViewSet):

    def create(self, request):
        return
    
    def retrieve(self, request, pk=None):
        return
    
    def update(self, request, pk=None):
        return
    
    def destroy(self, request, pk=None):
        return
    
    def list(self, request):
        return
