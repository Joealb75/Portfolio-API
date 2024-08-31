from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
# 1. URL-Prefix/PATH | 2. Class that handles request | 3. used for reverse URL matching in models / views EX "article/{pk}"

# router.register(r'consultation', ConsultationViewSet, 'consultation')

urlpatterns = [
    path('', include(router.urls)),
]

