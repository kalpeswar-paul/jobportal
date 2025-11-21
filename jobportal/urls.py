from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from jobs.views import (
    job_list_view, job_create_view, signup_view, logout_view,
    apply_view, submit_application_view, applicants_view
)

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),

    path('jobs/list/', job_list_view, name='job_list'),
    path('jobs/create/', job_create_view, name='job_create'),

    path('jobs/apply/<int:job_id>/', apply_view, name='apply'),
    path('jobs/apply/submit/', submit_application_view, name='apply_submit'),
    path('jobs/applicants/', applicants_view, name='applicants'),

    path('api/', include('jobs.api_urls')),

    # OpenAPI schema and documentation (drf-spectacular)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc:
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
