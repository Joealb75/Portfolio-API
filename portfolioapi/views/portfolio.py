from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from rest_framework.response import Response
from portfolioapi.models import Project, LanguageTag, Image, GitHubStats

class LanguageTagSerializer(serializers.Serializer):
    class Meta:
        model = LanguageTag
        fields = '__all__'

class LanguageTagViewSet(ViewSet):

    def create(self, request):
        serializer = LanguageTagSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self, request, pk=None):
        try:
            Language_Tag = LanguageTag.objects.get(pk=pk)
            serializer = LanguageTagSerializer(Language_Tag)
            return Response(serializer.data)
        
        except LanguageTag.DoesNotExist:
            return Response({'error': 'Tag Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            Language_Tag = LanguageTag.objects.get(pk=pk)
            serializer = LanguageTagSerializer(Language_Tag, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Language_Tag.DoesNotExist:
            return Response({'error': 'Tag Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        try:
            Language_Tag = LanguageTag.objects.get(pk=pk)
            Language_Tag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except LanguageTag.DoesNotExist:
            return Response({'error': 'Tag Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        Language_Tags = LanguageTag.objects.all()
        serializer = LanguageTagSerializer(Language_Tags, many=True)
        return Response(serializer.data)



class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectViewSet(ViewSet):

    def create(self, request):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        
        except Project.DoesNotExist:
            return Response({'error': 'Project Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        try:
            project = Project.objects.get()
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Project.DoesNotExist:
            return Response({'error': 'Consultation not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    

class ImageSerializer(serializers.Serializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageViewSet(ViewSet):

    def create(self, request):
        serializer = ImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
            serializer = ImageSerializer(image)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return Response({'error': 'Image Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
            serializer = ImageSerializer(image, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Image.DoesNotExist:
            return Response({'error': 'Image Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Image.DoesNotExist:
            return Response({'error': 'Image Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many = True)
        return Response(serializer.data)


class GitHubStatsSerializer(serializers.Serializer):
    class Meta:
        model = GitHubStats
        fields = '__all__'

class GitHubStatsViewSet(ViewSet):

    def create(self, request):
        serializer = GitHubStatsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            GitHubStat = GitHubStats.objects.get(pk=pk)
            serializer = GitHubStatsSerializer(GitHubStat)
            return Response(serializer.data)
        except GitHubStats.DoesNotExist:
            return Response({'error': 'Image Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        try:
            GitHubStat = GitHubStats.objects.get(pk=pk)
            serializer = GitHubStatsSerializer(GitHubStat, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except GitHubStats.DoesNotExist:
            return Response({'error': 'Image Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        try:
            GitHubStat = GitHubStats.objects.get(pk=pk)
            GitHubStat.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except GitHubStats.DoesNotExist:
            return Response({'error': 'Image Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        GitHubStat_s = GitHubStats.objects.all()
        serializer = GitHubStatsSerializer(GitHubStat_s, many = True)
        return Response(serializer.data)