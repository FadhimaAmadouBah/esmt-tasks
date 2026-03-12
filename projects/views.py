from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from tasks.models import Task


@login_required
def project_list(request):
    my_projects = Project.objects.filter(created_by=request.user)
    member_projects = Project.objects.filter(members=request.user).exclude(created_by=request.user)
    return render(request, 'projects/list.html', {
        'my_projects': my_projects,
        'member_projects': member_projects,
    })


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            form.save_m2m()
            messages.success(request, 'Projet créé avec succès !')
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'projects/form.html', {'form': form, 'action': 'Créer'})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    is_creator = project.created_by == request.user
    tasks = project.tasks.all()
    status_filter = request.GET.get('status')
    user_filter = request.GET.get('user')
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if user_filter:
        tasks = tasks.filter(assigned_to_id=user_filter)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks,
        'is_creator': is_creator,
        'members': project.members.all(),
        'status_filter': status_filter,
        'user_filter': user_filter,
    })


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projet modifié !')
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/form.html', {'form': form, 'action': 'Modifier'})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, created_by=request.user)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Projet supprimé.')
        return redirect('project_list')
    return render(request, 'projects/confirm_delete.html', {'project': project})