from django.db import models
from django.contrib.auth.models import User

class JobPost(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True)
    job_role = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    experience = models.CharField(max_length=50, help_text="e.g. 0-3 years")
    ctc = models.CharField(max_length=100, blank=True, help_text="e.g. 5 LPA")
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company_name or 'N/A'}"


class Application(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.name} for {self.job.title}"
