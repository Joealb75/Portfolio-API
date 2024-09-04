from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from portfolioapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
# 1. URL-Prefix/PATH | 2. Class that handles request | 3. used for reverse URL matching in models / views EX "article/{pk}"

router.register(r"users", Users, "user")
router.register(r'projects', ProjectViewSet, 'project')
router.register(r'tags', LanguageTagViewSet, 'tag')
router.register(r'images', ImageViewSet, 'image')
router.register(r'githubstats', GitHubStatsViewSet, 'githubstat')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-token-auth', obtain_auth_token),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

