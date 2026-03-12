from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, ProfileForm
from django.contrib.auth import get_user_model

User = get_user_model()


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} !')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username', 'Fadhima').strip()
        password = request.POST.get('password', 'python2005').strip()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Identifiants incorrects.')
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):
    from tasks.models import Task
    from projects.models import Project
    my_projects = Project.objects.filter(created_by=request.user)
    member_projects = Project.objects.filter(members=request.user).exclude(created_by=request.user)
    my_tasks = Task.objects.filter(assigned_to=request.user).order_by('due_date')[:5]
    total_tasks = Task.objects.filter(assigned_to=request.user).count()
    done_tasks = Task.objects.filter(assigned_to=request.user, status='termine').count()
    context = {
        'my_projects': my_projects,
        'member_projects': member_projects,
        'my_tasks': my_tasks,
        'total_tasks': total_tasks,
        'done_tasks': done_tasks,
        'total_projects': my_projects.count() + member_projects.count(),
    }
    return render(request, 'dashboard.html', context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour !')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})