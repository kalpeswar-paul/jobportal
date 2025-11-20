from rest_framework import viewsets, permissions
from .models import JobPost
from .serializers import JobPostSerializer

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all().order_by('-created_at')
    serializer_class = JobPostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
