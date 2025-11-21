from rest_framework import viewsets, permissions
from .models import JobPost, Application
from .serializers import JobPostSerializer, ApplicationSerializer

class JobPostViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all().order_by('-created_at')
    serializer_class = JobPostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        qs = super().get_queryset()
        # If query param mine=1 and user is authenticated, show only user's jobs
        mine = self.request.query_params.get('mine')
        if mine == '1' and self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        # Search support via q param (search title, company, role, location)
        q = self.request.query_params.get('q')
        if q:
            return qs.filter(
                models.Q(title__icontains=q) |
                models.Q(company_name__icontains=q) |
                models.Q(job_role__icontains=q) |
                models.Q(location__icontains=q)
            ).order_by('-created_at')
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('-created_at')
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        # Allow anyone to create application; read restricted to authenticated owners (we'll not expose in API publicly)
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
