from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, ProfileUpdateForm
from .models import CustomUser


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} ! Votre compte a été créé.')
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté.')
    return redirect('login')


@login_required
def dashboard_view(request):
    user = request.user

    # Projets de l'utilisateur
    created_projects = user.created_projects.all()[:5]
    member_projects = user.member_projects.exclude(created_by=user)[:5]

    # Tâches assignées
    my_tasks = user.assigned_tasks.select_related('project').order_by('due_date')[:10]

    # Statistiques
    total_tasks = user.assigned_tasks.count()
    done_tasks = user.assigned_tasks.filter(status='termine').count()
    in_progress = user.assigned_tasks.filter(status='en_cours').count()
    overdue_tasks = [t for t in user.assigned_tasks.filter(status__in=['a_faire', 'en_cours']) if t.is_overdue()]

    context = {
        'created_projects': created_projects,
        'member_projects': member_projects,
        'my_tasks': my_tasks,
        'total_tasks': total_tasks,
        'done_tasks': done_tasks,
        'in_progress': in_progress,
        'overdue_count': len(overdue_tasks),
        'completion_rate': round((done_tasks / total_tasks * 100), 1) if total_tasks > 0 else 0,
    }
    return render(request, 'dashboard.html', context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès !')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': form})