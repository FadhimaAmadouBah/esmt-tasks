from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import ModelForm
from django import forms
from .models import Task, PrimeEvaluation
from projects.models import Project
from users.models import CustomUser
from django.utils import timezone


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'status', 'priority', 'due_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def __init__(self, *args, project=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name not in ['assigned_to']:
                field.widget.attrs['class'] = 'form-control'

        if project and user:
            members = project.members.all()
            # Un étudiant ne peut pas assigner un professeur
            if user.is_etudiant:
                members = members.filter(role='etudiant')
            self.fields['assigned_to'].queryset = CustomUser.objects.filter(
                id__in=list(members.values_list('id', flat=True)) + [project.created_by.id]
            )
        self.fields['assigned_to'].widget.attrs['class'] = 'form-select'


@login_required
def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk, created_by=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, project=project, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.created_by = request.user
            task.save()
            messages.success(request, f'Tâche "{task.title}" créée !')
            return redirect('project_detail', pk=project_pk)
    else:
        form = TaskForm(project=project, user=request.user)

    return render(request, 'tasks/form.html', {'form': form, 'project': project, 'action': 'Créer'})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project

    # Vérification des permissions
    is_creator = request.user == project.created_by
    is_assigned = request.user == task.assigned_to

    if not is_creator and not is_assigned:
        messages.error(request, 'Vous ne pouvez modifier que vos propres tâches.')
        return redirect('project_detail', pk=project.pk)

    if request.method == 'POST':
        if is_creator:
            form = TaskForm(request.POST, instance=task, project=project, user=request.user)
        else:
            # L'assigné peut seulement changer le statut
            form = TaskForm(request.POST, instance=task, project=project, user=request.user)
            form.fields = {k: v for k, v in form.fields.items() if k == 'status'}

        if form.is_valid():
            form.save()
            messages.success(request, 'Tâche mise à jour !')
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm(instance=task, project=project, user=request.user)

    return render(request, 'tasks/form.html', {'form': form, 'project': project, 'task': task, 'action': 'Modifier'})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    project_pk = task.project.pk
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tâche supprimée.')
    return redirect('project_detail', pk=project_pk)


@login_required
def statistics_view(request):
    """Statistiques et évaluations pour les primes"""
    from django.db.models import Count, Q

    context = {}

    if request.user.is_professeur or request.user.is_staff:
        # Stats des professeurs pour les primes
        professeurs = CustomUser.objects.filter(role='professeur')
        evaluations = []

        year = timezone.now().year
        for prof in professeurs:
            total = prof.assigned_tasks.filter(due_date__year=year).count()
            on_time = sum(1 for t in prof.assigned_tasks.filter(
                due_date__year=year, status='termine'
            ) if t.completed_on_time())

            rate = round((on_time / total * 100), 1) if total > 0 else 0
            prime = 100000 if rate == 100 else (30000 if rate >= 90 else 0)

            evaluations.append({
                'user': prof,
                'total': total,
                'on_time': on_time,
                'rate': rate,
                'prime': prime,
            })

        context['evaluations'] = evaluations
        context['year'] = year

    # Stats personnelles
    my_tasks = request.user.assigned_tasks.all()
    quarterly_stats = []
    year = timezone.now().year

    for q, (start_month, end_month) in enumerate([(1, 3), (4, 6), (7, 9), (10, 12)], 1):
        q_tasks = my_tasks.filter(due_date__year=year, due_date__month__gte=start_month, due_date__month__lte=end_month)
        total = q_tasks.count()
        done = q_tasks.filter(status='termine').count()
        on_time = sum(1 for t in q_tasks.filter(status='termine') if t.completed_on_time())

        quarterly_stats.append({
            'quarter': f'T{q}',
            'total': total,
            'done': done,
            'on_time': on_time,
            'rate': round((on_time / total * 100), 1) if total > 0 else 0,
        })

    context['quarterly_stats'] = quarterly_stats
    return render(request, 'tasks/statistics.html', context)