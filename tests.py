import pytest
from django.contrib.auth import get_user_model
from projects.models import Project
from tasks.models import Task

User = get_user_model()


# ===== TESTS UTILISATEURS =====

@pytest.mark.django_db
def test_creer_utilisateur():
    user = User.objects.create_user(
        username='testuser',
        password='Test1234!',
        role='etudiant'
    )
    assert user.username == 'testuser'
    assert user.role == 'etudiant'
    assert user.is_etudiant == True
    assert user.is_professeur == False


@pytest.mark.django_db
def test_creer_professeur():
    prof = User.objects.create_user(
        username='testprof',
        password='Test1234!',
        role='professeur'
    )
    assert prof.is_professeur == True
    assert prof.is_etudiant == False


# ===== TESTS PROJETS =====

@pytest.mark.django_db
def test_creer_projet():
    user = User.objects.create_user(
        username='creator',
        password='Test1234!',
        role='etudiant'
    )
    project = Project.objects.create(
        name='Projet Test',
        description='Description test',
        created_by=user
    )
    assert project.name == 'Projet Test'
    assert project.created_by == user
    assert project.get_completion_rate() == 0


@pytest.mark.django_db
def test_taux_completion_projet():
    user = User.objects.create_user(
        username='creator2',
        password='Test1234!',
        role='etudiant'
    )
    project = Project.objects.create(
        name='Projet Test 2',
        created_by=user
    )
    Task.objects.create(
        title='Tâche 1', project=project,
        created_by=user, status='termine'
    )
    Task.objects.create(
        title='Tâche 2', project=project,
        created_by=user, status='a_faire'
    )
    assert project.get_completion_rate() == 50


# ===== TESTS TÂCHES =====

@pytest.mark.django_db
def test_creer_tache():
    user = User.objects.create_user(
        username='creator3',
        password='Test1234!',
        role='etudiant'
    )
    project = Project.objects.create(
        name='Projet Test 3',
        created_by=user
    )
    task = Task.objects.create(
        title='Tâche Test',
        project=project,
        created_by=user,
        status='a_faire'
    )
    assert task.title == 'Tâche Test'
    assert task.status == 'a_faire'
    assert task.is_overdue() == False


@pytest.mark.django_db
def test_statut_tache():
    user = User.objects.create_user(
        username='creator4',
        password='Test1234!',
        role='etudiant'
    )
    project = Project.objects.create(
        name='Projet Test 4',
        created_by=user
    )
    task = Task.objects.create(
        title='Tâche Terminée',
        project=project,
        created_by=user,
        status='termine'
    )
    assert task.status == 'termine'
    assert task.completed_at is not None


# ===== TESTS PRIMES =====

@pytest.mark.django_db
def test_prime_100k():
    from tasks.models import PrimeEvaluation
    prof = User.objects.create_user(
        username='prof1',
        password='Test1234!',
        role='professeur'
    )
    eval = PrimeEvaluation(
        professeur=prof,
        period='T1',
        year=2026,
        total_tasks=10,
        tasks_on_time=10
    )
    prime = eval.calculate_prime()
    assert prime == 100000


@pytest.mark.django_db
def test_prime_30k():
    from tasks.models import PrimeEvaluation
    prof = User.objects.create_user(
        username='prof2',
        password='Test1234!',
        role='professeur'
    )
    eval = PrimeEvaluation(
        professeur=prof,
        period='T1',
        year=2026,
        total_tasks=10,
        tasks_on_time=9
    )
    prime = eval.calculate_prime()
    assert prime == 30000


@pytest.mark.django_db
def test_pas_de_prime():
    from tasks.models import PrimeEvaluation
    prof = User.objects.create_user(
        username='prof3',
        password='Test1234!',
        role='professeur'
    )
    eval = PrimeEvaluation(
        professeur=prof,
        period='T1',
        year=2026,
        total_tasks=10,
        tasks_on_time=5
    )
    prime = eval.calculate_prime()
    assert prime == 0