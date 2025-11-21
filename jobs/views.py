from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.http import JsonResponse
from .models import JobPost, Application
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

def job_list_view(request):
    """
    Renders the job list page. The page will use JS to fetch /api/jobs/
    If user is authenticated, the JS will request mine=1 by default to show
    only the owner's jobs (as requested).
    """
    return render(request, "job_list.html")


@login_required
def job_create_view(request):
    return render(request, "create_job.html")


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')


def apply_view(request, job_id):
    job = get_object_or_404(JobPost, pk=job_id)
    return render(request, "apply.html", {"job": job})


def submit_application_view(request):
    """
    Handles submission of application from the apply.html form via POST (multipart/form-data).
    Returns JSON {success: true} on success.
    """
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

    job_id = request.POST.get('job_id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    cover_letter = request.POST.get('cover_letter', '')

    resume = request.FILES.get('resume')
    if not job_id or not name or not email or not mobile or not resume:
        return JsonResponse({'success': False, 'error': 'Missing fields'}, status=400)

    job = get_object_or_404(JobPost, pk=job_id)

    application = Application.objects.create(
        job=job,
        name=name,
        mobile=mobile,
        email=email,
        resume=resume,
        cover_letter=cover_letter
    )

    return JsonResponse({'success': True})


@login_required
def applicants_view(request):
    """
    Shows list of applicants for jobs owned by the logged-in user.
    """
    jobs = JobPost.objects.filter(owner=request.user).order_by('-created_at')
    # Prefetch applications
    job_applications = []
    for job in jobs:
        apps = job.applications.all().order_by('-created_at')
        job_applications.append((job, apps))
    return render(request, "applicants.html", {"job_applications": job_applications})
