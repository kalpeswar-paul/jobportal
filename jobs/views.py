from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

def landing_page(request):
    return render(request, 'base.html')

def job_list_view(request):
    return render(request, "job_list.html")

@login_required
def job_create_view(request):
    return render(request, "create_job.html")

def signup_view(request):
    """
    Employer signup view.
    After registration, user is logged in and can create jobs.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the new employer
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def logout_view(request):
    """
    Custom logout view that works with a simple GET link.
    """
    logout(request)
    return redirect('login')
