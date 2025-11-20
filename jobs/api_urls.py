from rest_framework.routers import DefaultRouter
from .api_views import JobPostViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'jobs', JobPostViewSet, basename='jobpost')

urlpatterns = [
    path('', include(router.urls)),
]
