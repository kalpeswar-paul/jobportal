from rest_framework import serializers
from .models import JobPost, Application

class JobPostSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    owner_id = serializers.IntegerField(source='owner.id', read_only=True)

    class Meta:
        model = JobPost
        fields = [
            'id', 'owner_id', 'owner_username', 'title', 'company_name', 'job_role',
            'description', 'experience', 'ctc', 'location', 'created_at'
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'job', 'job_title', 'name', 'mobile', 'email', 'resume', 'cover_letter', 'created_at']
        read_only_fields = ['created_at']
