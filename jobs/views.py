from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'base.html')

def job_list_view(request):
    return render(request, "job_list.html")

@login_required
def job_create_view(request):
    return render(request, "create_job.html")
