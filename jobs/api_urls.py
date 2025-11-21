from rest_framework.routers import DefaultRouter
from .api_views import JobPostViewSet, ApplicationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'jobs', JobPostViewSet, basename='jobpost')
router.register(r'applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
]
