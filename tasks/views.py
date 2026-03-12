from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from projects.models import Project


@login_required
def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if project.created_by != request.user:
        messages.error(request, 'Permission refusée.')
        return redirect('project_detail', pk=project_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.created_by = request.user
            task.save()
            messages.success(request, 'Tâche créée !')
            return redirect('project_detail', pk=project_pk)
    else:
        form = TaskForm(user=request.user)
    return render(request, 'tasks/form.html', {'form': form, 'project': project, 'action': 'Créer'})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    is_creator = task.project.created_by == request.user
    is_assigned = task.assigned_to == request.user
    if not is_creator and not is_assigned:
        messages.error(request, 'Permission refusée.')
        return redirect('project_detail', pk=task.project.pk)
    if request.method == 'POST':
        if is_creator:
            form = TaskForm(request.POST, instance=task, user=request.user)
        else:
            form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            if not is_creator:
                task.status = form.cleaned_data['status']
                task.save()
            else:
                form.save()
            messages.success(request, 'Tâche mise à jour !')
            return redirect('project_detail', pk=task.project.pk)
    else:
        form = TaskForm(instance=task, user=request.user)
    return render(request, 'tasks/form.html', {'form': form, 'project': task.project, 'action': 'Modifier'})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, project__created_by=request.user)
    project_pk = task.project.pk
    task.delete()
    messages.success(request, 'Tâche supprimée.')
    return redirect('project_detail', pk=project_pk)


@login_required
def statistics_view(request):
    from django.db.models import Count
    year = timezone.now().year
    quarters = {
        'T1': (1, 3), 'T2': (4, 6), 'T3': (7, 9), 'T4': (10, 12)
    }
    quarterly_stats = []
    for q, (m_start, m_end) in quarters.items():
        tasks = Task.objects.filter(
            assigned_to=request.user,
            due_date__year=year,
            due_date__month__gte=m_start,
            due_date__month__lte=m_end
        )
        total = tasks.count()
        on_time = sum(1 for t in tasks if t.completed_on_time())
        rate = round((on_time / total * 100)) if total > 0 else 0
        quarterly_stats.append({'quarter': q, 'total': total, 'on_time': on_time, 'rate': rate})

    evaluations = []
    if request.user.is_staff:
        from users.models import CustomUser
        professors = CustomUser.objects.filter(role='professeur')
        for prof in professors:
            tasks = Task.objects.filter(assigned_to=prof)
            total = tasks.count()
            on_time = sum(1 for t in tasks if t.completed_on_time())
            rate = round((on_time / total * 100)) if total > 0 else 0
            prime = 100000 if rate == 100 else (30000 if rate >= 90 else 0)
            evaluations.append({
                'user': prof, 'total': total,
                'on_time': on_time, 'rate': rate, 'prime': prime
            })

    return render(request, 'tasks/statistics.html', {
        'quarterly_stats': quarterly_stats,
        'evaluations': evaluations,
        'year': year,
    })