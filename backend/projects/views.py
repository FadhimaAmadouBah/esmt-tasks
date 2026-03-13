from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import ModelForm
from .models import Project
from users.models import CustomUser


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'members']
        widgets = {
            'description': __import__('django').forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'members': __import__('django').forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'


@login_required
def project_list(request):
    my_projects = request.user.created_projects.prefetch_related('tasks', 'members')
    member_projects = request.user.member_projects.exclude(created_by=request.user)
    return render(request, 'projects/list.html', {
        'my_projects': my_projects,
        'member_projects': member_projects
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
            messages.success(request, f'Projet "{project.name}" créé avec succès !')
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'projects/form.html', {'form': form, 'action': 'Créer'})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.created_by and request.user not in project.members.all():
        messages.error(request, 'Vous n\'avez pas accès à ce projet.')
        return redirect('project_list')

    tasks = project.tasks.select_related('assigned_to')

    # Filtres
    status_filter = request.GET.get('status', '')
    user_filter = request.GET.get('user', '')
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if user_filter:
        tasks = tasks.filter(assigned_to__id=user_filter)

    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks,
        'members': project.members.all(),
        'status_filter': status_filter,
        'user_filter': user_filter,
        'is_creator': request.user == project.created_by,
    })


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projet modifié avec succès !')
            return redirect('project_detail', pk=pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/form.html', {'form': form, 'action': 'Modifier', 'project': project})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, created_by=request.user)
    if request.method == 'POST':
        name = project.name
        project.delete()
        messages.success(request, f'Projet "{name}" supprimé.')
        return redirect('project_list')
    return render(request, 'projects/confirm_delete.html', {'project': project})