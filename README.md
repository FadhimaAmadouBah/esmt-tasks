
Cahier des Charges : Application de Gestion des Tâches Collaboratives Contexte Votre mission consiste à développer une application web pour gérer des tâches dans un environnement collaboratif je préfère dire que l’application sera orientée ESMT pour les enseignants et étudiants). Chaque utilisateur peut créer des projets, y ajouter des tâches, les assigner à d'autres membres et suivre leur progression. Mettez en place une possibilité de voir les statistiques concernant les taches trimestriel et annuel et possibilité d’évaluation afin de voir si certain utilisateur (membre d’équipe qui sont des enseignants) ont droit à une prime. NB: - La prime de 30K pour ceux qui finissent 90% de leur tâche dans les délais accordés et à hauteur de 100k ceux qui font 100%. -Il y’a deux profil, Etudiant et Professeur Objectifs 1 (en utilisant les Template Django) : 1. Gestion des utilisateurs : a. Inscription et connexion (authentification avec un système de gestion des utilisateurs). b. Gestion des profils : chaque utilisateur peut mettre à jour son profil (nom, avatar, email et le mot de passe). 2. Gestion des projets : a. Un utilisateur peut créer, modifier ou supprimer un projet. b. Chaque projet contient une liste de tâches. Objectifs 2 (frontend Angular/react) : 3. Gestion des tâches : a. Chaque tâche est associée à un projet. b. Les tâches incluent un titre, une description, une date limite, un statut (à faire, en cours, terminé) et un utilisateur assigné. c. Les utilisateurs peuvent mettre à jour le statut des tâches. d. Les étudiants ne peuvent pas associer un professeur à une tache 4. Permissions et rôles : a. Seuls les créateurs d’un projet peuvent ajouter/supprimer des tâches ou des utilisateurs au projet. b. Les utilisateurs assignés à un projet peuvent uniquement modifier les tâches qui leur sont attribuées. 5. Interface utilisateur : a. Les fonctionnalités doivent être accessibles via une interface web conviviale et moderne. b. Un tableau de bord affichera les projets et leurs tâches associés avec un système de filtres (par statut ou utilisateur). Spécifications techniques Backend • Framework : Django • Modules requis : o Django REST Framework pour créer une API RESTful. o Django ORM pour la gestion des bases de données. o Django Allauth ou équivalent pour la gestion de l’authentification. o Django CORS Headers pour permettre des connexions avec un frontend (angular ou react). Frontend • Interface minimale obligatoire avec Django Templates (HTML, CSS, JavaScript) pour le premier objectif. • Pour l’objectif 2 vous pouvez lier l’API à une application React/Angular/Vue.js. Base de données • Base relationnelle : PostgreSQL ou SQLite (pour simplifier) mais vous pouvez utiliser aussi mysql. Authentification • Utilisation du système d’authentification intégré à Django. • Gestion de tokens via djangorestframework-simplejwt (JWT) pour l'API exposée à un frontend angular ou react. Tests • Implémentez des tests unitaires pour les fonctionnalités principales avec pytest-django. Livrables 1. Code source complet de l'application sur un dépôt GitHub ou GitLab. 2. Documentation incluant : a. Instructions pour configurer et lancer le projet. b. Explication des modèles de données et des routes API disponibles. 3. Présentation d'une démo fonctionnelle. Déroulement et évaluation Durée : 3 semaines Phases : 1. Semaine 1 : a. Développement des modèles et des vues pour les utilisateurs, projets et tâches. b. Mise en place de l'authentification. 2. Semaine 2 & 3: a. Création de l’interface utilisateur de base. b. Exposition des routes API (si applicable). c. Mise en place du frontend Angular ou React d. Tests et débogage. e. Finalisation et documentation. Critères d'évaluation : • Respect des fonctionnalités demandées. • Structure et clarté du code (respect des bonnes pratiques Django). • Qualité de l’interface utilisateur. • Qualité de la documentation. Exemples de fonctionnalités bonus (optionnel) • Notifications par email pour les tâches proches de leur date limite. • Recherche avancée et filtres pour les tâches. • Intégration avec un calendrier (par exemple, Google Calendar). • Ajout d’un chat en temps réel (via Django Channels). Tu m'expliques pas a pas je suis debutante et on fait tout aujourdh'ui

Afficher plus
26 févr.
Je vais t'expliquer tout pas à pas ! C'est un grand projet, alors commençons par bien comprendre ce qu'on va construire ensemble.

🗺️ Vue d'ensemble du projet
Tu vas créer une application web pour l'ESMT (une école) où :

Les professeurs et étudiants peuvent gérer des projets et tâches
Les professeurs peuvent recevoir des primes selon leur performance
Il y a un tableau de bord avec statistiques
📋 Plan du jour (étape par étape)
Voici ce qu'on va faire aujourd'hui, dans l'ordre :

Étape 1 - Mise en place de l'environnement (installation des outils) Étape 2 - Création du projet Django (le backend) Étape 3 - Les modèles de données (la base de données) Étape 4 - L'authentification (connexion/inscription) Étape 5 - Les vues et templates (l'interface Django) Étape 6 - L'API REST (pour le frontend React plus tard) Étape 7 - Le frontend React (l'interface moderne)

🛠️ ÉTAPE 1 : Installation de l'environnement
Ce dont tu as besoin installé sur ton PC :
Python 3.10+ → https://python.org
Node.js 18+ → https://nodejs.org
VS Code → https://code.visualstudio.com
Git → https://git-scm.com
Vérifie tes installations (dans le terminal) :
bash
python --version
node --version
git --version
📁 ÉTAPE 2 : Créer la structure du projet
Ouvre ton terminal et tape ces commandes une par une :

bash
# 1. Crée un dossier pour ton projet
mkdir esmt-tasks
cd esmt-tasks

# 2. Crée un environnement virtuel Python (isolé)
python -m venv venv

# 3. Active l'environnement virtuel
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate

# 4. Installe Django et toutes les dépendances
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow pytest-django

# 5. Crée le projet Django
django-admin startproject backend
cd backend

# 6. Crée les applications Django
python manage.py startapp users
python manage.py startapp projects
python manage.py startapp tasks
```

### Structure obtenue :
```
esmt-tasks/
├── venv/
└── backend/
    ├── manage.py
    ├── backend/          ← configuration principale
    ├── users/            ← gestion des utilisateurs
    ├── projects/         ← gestion des projets
    └── tasks/            ← gestion des tâches
⚙️ ÉTAPE 3 : Configuration de Django (settings.py)
Ouvre backend/backend/settings.py et remplace tout le contenu par ceci :

python
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-esmt-secret-key-change-in-production'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps tierces
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    # Nos apps
    'users',
    'projects',
    'tasks',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ← doit être en 1er !
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ← dossier templates global
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Dakar'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Modèle utilisateur personnalisé
AUTH_USER_MODEL = 'users.CustomUser'

# Configuration de l'API REST
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Configuration JWT
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

# CORS - autoriser React à se connecter
CORS_ALLOW_ALL_ORIGINS = True  # En production, mettre les domaines précis

# Redirection après login/logout
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'
🗃️ ÉTAPE 4 : Les Modèles de données
4.1 - Modèle Utilisateur (users/models.py)
python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Utilisateur personnalisé avec rôle Etudiant ou Professeur"""
    
    ROLE_CHOICES = [
        ('etudiant', 'Étudiant'),
        ('professeur', 'Professeur'),
    ]
    
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='etudiant'
    )
    avatar = models.ImageField(
        upload_to='avatars/', 
        null=True, 
        blank=True
    )
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    @property
    def is_professeur(self):
        return self.role == 'professeur'
    
    @property
    def is_etudiant(self):
        return self.role == 'etudiant'
4.2 - Modèle Projet (projects/models.py)
python
from django.db import models
from django.conf import settings

class Project(models.Model):
    """Un projet peut contenir plusieurs tâches"""
    
    name = models.CharField(max_length=200, verbose_name="Nom du projet")
    description = models.TextField(blank=True, verbose_name="Description")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_projects',
        verbose_name="Créé par"
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='member_projects',
        blank=True,
        verbose_name="Membres"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
    
    def __str__(self):
        return self.name
    
    def get_completion_rate(self):
        """Calcule le taux de complétion du projet"""
        total = self.tasks.count()
        if total == 0:
            return 0
        done = self.tasks.filter(status='termine').count()
        return round((done / total) * 100, 1)
4.3 - Modèle Tâche (tasks/models.py)
python
from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    """Une tâche appartient à un projet"""
    
    STATUS_CHOICES = [
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
    ]
    
    PRIORITY_CHOICES = [
        ('basse', 'Basse'),
        ('normale', 'Normale'),
        ('haute', 'Haute'),
        ('urgente', 'Urgente'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(blank=True, verbose_name="Description")
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name="Projet"
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks',
        verbose_name="Assigné à"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_tasks',
        verbose_name="Créé par"
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='a_faire',
        verbose_name="Statut"
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='normale',
        verbose_name="Priorité"
    )
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="Date limite")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Terminé le")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['due_date', '-priority']
        verbose_name = "Tâche"
        verbose_name_plural = "Tâches"
    
    def __str__(self):
        return f"{self.title} - {self.project.name}"
    
    def is_overdue(self):
        """Vérifie si la tâche est en retard"""
        if self.due_date and self.status != 'termine':
            return timezone.now() > self.due_date
        return False
    
    def completed_on_time(self):
        """Vérifie si la tâche a été terminée dans les délais"""
        if self.completed_at and self.due_date:
            return self.completed_at <= self.due_date
        return False
    
    def save(self, *args, **kwargs):
        # Enregistre automatiquement la date de fin
        if self.status == 'termine' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status != 'termine':
            self.completed_at = None
        super().save(*args, **kwargs)


class PrimeEvaluation(models.Model):
    """Évaluation trimestrielle/annuelle pour les primes des professeurs"""
    
    PERIOD_CHOICES = [
        ('T1', 'Trimestre 1 (Jan-Mar)'),
        ('T2', 'Trimestre 2 (Avr-Jun)'),
        ('T3', 'Trimestre 3 (Jul-Sep)'),
        ('T4', 'Trimestre 4 (Oct-Déc)'),
        ('annuel', 'Annuel'),
    ]
    
    PRIME_CHOICES = [
        (0, 'Pas de prime'),
        (30000, 'Prime 30 000 FCFA (90%+)'),
        (100000, 'Prime 100 000 FCFA (100%)'),
    ]
    
    professeur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='evaluations'
    )
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    year = models.IntegerField(verbose_name="Année")
    total_tasks = models.IntegerField(default=0)
    tasks_on_time = models.IntegerField(default=0)
    completion_rate = models.FloatField(default=0.0)
    prime_amount = models.IntegerField(choices=PRIME_CHOICES, default=0)
    calculated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['professeur', 'period', 'year']
        verbose_name = "Évaluation Prime"
    
    def calculate_prime(self):
        """Calcule la prime selon le taux de complétion"""
        if self.total_tasks == 0:
            self.prime_amount = 0
        elif self.completion_rate == 100.0:
            self.prime_amount = 100000
        elif self.completion_rate >= 90.0:
            self.prime_amount = 30000
        else:
            self.prime_amount = 0
        return self.prime_amount
    
    def __str__(self):
        return f"{self.professeur.username} - {self.period} {self.year} - {self.prime_amount} FCFA"
🔗 ÉTAPE 5 : URLs principales (backend/urls.py)
python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs Django Templates (Objectif 1)
    path('', include('users.urls')),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    
    # URLs API REST (Objectif 2)
    path('api/', include('users.api_urls')),
    path('api/', include('projects.api_urls')),
    path('api/', include('tasks.api_urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else settings.STATIC_ROOT)
👤 ÉTAPE 6 : App Users complète
users/forms.py
python
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'avatar', 'bio')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
users/views.py
python
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
users/urls.py
python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
users/admin.py
python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations ESMT', {'fields': ('role', 'avatar', 'bio')}),
    )
📁 ÉTAPE 7 : App Projects
projects/views.py
python
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
projects/urls.py
python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
]
✅ ÉTAPE 8 : App Tasks
tasks/views.py
python
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
    
    for q, (start_month, end_month) in enumerate([(1,3),(4,6),(7,9),(10,12)], 1):
        q_tasks = my_tasks.filter(due_date__year=year, due_date__month__gte=start_month, due_date__month__lte=end_month)
        total = q_tasks.count()
        done = q_tasks.filter(status='termine').count()
        on_time = sum(1 for t in q_tasks.filter(status='termine') if t.completed_on_time())
        
        quarterly_stats.append({
            'quarter': f'T{q}',
            'total': total,
            'done': done,
            'on_time': on_time,
            'rate': round((on_time/total*100), 1) if total > 0 else 0,
        })
    
    context['quarterly_stats'] = quarterly_stats
    return render(request, 'tasks/statistics.html', context)
tasks/urls.py
python
from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:project_pk>/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('statistics/', views.statistics_view, name='statistics'),
]
🌐 ÉTAPE 9 : API REST
users/serializers.py
python
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'avatar', 'bio']
        read_only_fields = ['id']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role', 'first_name', 'last_name']
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
users/api_urls.py
python
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api_views

urlpatterns = [
    path('auth/register/', api_views.RegisterAPIView.as_view(), name='api_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='api_login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='api_refresh'),
    path('users/me/', api_views.MeAPIView.as_view(), name='api_me'),
    path('users/', api_views.UserListAPIView.as_view(), name='api_users'),
]
users/api_views.py
python
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class MeAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
projects/serializers.py
python
from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, source='members',
        queryset=__import__('users.models', fromlist=['CustomUser']).CustomUser.objects.all()
    )
    completion_rate = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_by', 'members', 'member_ids', 
                  'completion_rate', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']
    
    def get_completion_rate(self, obj):
        return obj.get_completion_rate()
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
projects/api_views.py
python
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(
            created_by=user
        ) | Project.objects.filter(members=user)

class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(created_by=user) | Project.objects.filter(members=user)
    
    def perform_update(self, serializer):
        if self.get_object().created_by != self.request.user:
            raise PermissionDenied("Seul le créateur peut modifier ce projet.")
        serializer.save()
    
    def perform_destroy(self, instance):
        if instance.created_by != self.request.user:
            raise PermissionDenied("Seul le créateur peut supprimer ce projet.")
        instance.delete()
projects/api_urls.py
python
from django.urls import path
from . import api_views

urlpatterns = [
    path('projects/', api_views.ProjectListCreateAPI.as_view(), name='api_project_list'),
    path('projects/<int:pk>/', api_views.ProjectDetailAPI.as_view(), name='api_project_detail'),
]
tasks/serializers.py
python
from rest_framework import serializers
from .models import Task, PrimeEvaluation
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_detail = UserSerializer(source='assigned_to', read_only=True)
    is_overdue = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assigned_to', 'assigned_to_detail',
                  'created_by', 'status', 'priority', 'due_date', 'completed_at',
                  'is_overdue', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'completed_at', 'created_at', 'updated_at']
    
    def get_is_overdue(self, obj):
        return obj.is_overdue()
    
    def validate(self, data):
        request = self.context.get('request')
        if request and request.user.is_etudiant:
            assigned = data.get('assigned_to')
            if assigned and assigned.is_professeur:
                raise serializers.ValidationError(
                    "Les étudiants ne peuvent pas assigner une tâche à un professeur."
                )
        return data

class PrimeEvaluationSerializer(serializers.ModelSerializer):
    professeur = UserSerializer(read_only=True)
    
    class Meta:
        model = PrimeEvaluation
        fields = '__all__'
tasks/api_views.py
python
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Task, PrimeEvaluation
from .serializers import TaskSerializer, PrimeEvaluationSerializer
from projects.models import Project
from users.models import CustomUser
from django.utils import timezone

class TaskListCreateAPI(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Task.objects.filter(project__id=project_id)
        return Task.objects.filter(assigned_to=self.request.user)
    
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = Project.objects.get(pk=project_id)
        if project.created_by != self.request.user:
            raise PermissionDenied("Seul le créateur peut ajouter des tâches.")
        serializer.save(created_by=self.request.user, project=project)

class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def perform_update(self, serializer):
        task = self.get_object()
        user = self.request.user
        is_creator = task.project.created_by == user
        is_assigned = task.assigned_to == user
        
        if not is_creator and not is_assigned:
            raise PermissionDenied("Permission refusée.")
        
        if not is_creator and is_assigned:
            # L'assigné ne peut changer que le statut
            allowed = {'status'}
            if set(serializer.validated_data.keys()) - allowed:
                raise PermissionDenied("Vous ne pouvez changer que le statut.")
        
        serializer.save()

class StatisticsAPI(APIView):
    def get(self, request):
        year = int(request.query_params.get('year', timezone.now().year))
        period = request.query_params.get('period', 'annuel')
        
        if request.user.is_staff or request.user.is_professeur:
            professeurs = CustomUser.objects.filter(role='professeur')
            evaluations = []
            for prof in professeurs:
                tasks = prof.assigned_tasks.filter(due_date__year=year)
                total = tasks.count()
                on_time = sum(1 for t in tasks.filter(status='termine') if t.completed_on_time())
                rate = round((on_time/total*100), 1) if total > 0 else 0
                prime = 100000 if rate == 100 else (30000 if rate >= 90 else 0)
                evaluations.append({
                    'id': prof.id,
                    'name': prof.get_full_name() or prof.username,
                    'total_tasks': total,
                    'on_time': on_time,
                    'completion_rate': rate,
                    'prime': prime
                })
            return Response({'evaluations': evaluations, 'year': year})
        return Response({'error': 'Permission refusée'}, status=403)
tasks/api_urls.py
python
from django.urls import path
from . import api_views

urlpatterns = [
    path('projects/<int:project_pk>/tasks/', api_views.TaskListCreateAPI.as_view(), name='api_task_list'),
    path('tasks/<int:pk>/', api_views.TaskDetailAPI.as_view(), name='api_task_detail'),
    path('tasks/my/', api_views.TaskListCreateAPI.as_view(), name='api_my_tasks'),
    path('statistics/', api_views.StatisticsAPI.as_view(), name='api_statistics'),
]
🎨 ÉTAPE 10 : Templates HTML
Crée le dossier backend/templates/ puis ces fichiers :

templates/base.html (template de base)
html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}ESMT Tasks{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        :root {
            --esmt-primary: #1a3a6e;
            --esmt-secondary: #e8a020;
        }
        body { background-color: #f8f9fa; font-family: 'Segoe UI', sans-serif; }
        .navbar { background: var(--esmt-primary) !important; }
        .navbar-brand { color: var(--esmt-secondary) !important; font-weight: bold; font-size: 1.3rem; }
        .nav-link { color: rgba(255,255,255,0.85) !important; }
        .nav-link:hover, .nav-link.active { color: var(--esmt-secondary) !important; }
        .sidebar { min-height: calc(100vh - 56px); background: white; box-shadow: 2px 0 5px rgba(0,0,0,.05); }
        .sidebar .nav-link { color: #444; padding: .6rem 1rem; border-radius: 8px; margin: 2px 0; }
        .sidebar .nav-link:hover, .sidebar .nav-link.active { background: var(--esmt-primary); color: white !important; }
        .card { border: none; border-radius: 12px; box-shadow: 0 2px 15px rgba(0,0,0,.06); }
        .card-header { background: var(--esmt-primary); color: white; border-radius: 12px 12px 0 0 !important; }
        .btn-primary { background: var(--esmt-primary); border-color: var(--esmt-primary); }
        .btn-primary:hover { background: #0f2447; }
        .btn-warning { background: var(--esmt-secondary); border-color: var(--esmt-secondary); color: white; }
        .badge-a_faire { background: #6c757d; }
        .badge-en_cours { background: #0d6efd; }
        .badge-termine { background: #198754; }
        .stat-card { border-left: 4px solid var(--esmt-primary); }
    </style>
</head>
<body>
    <!-- NAVBAR -->
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'dashboard' %}">
                <i class="bi bi-kanban"></i> ESMT Tasks
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navMenu">
                <ul class="navbar-nav ms-auto align-items-center">
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <span class="nav-link text-warning">
                            <i class="bi bi-person-circle"></i> {{ user.username }}
                            <span class="badge bg-warning text-dark ms-1">{{ user.get_role_display }}</span>
                        </span>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'profile' %}"><i class="bi bi-gear"></i> Profil</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'logout' %}"><i class="bi bi-box-arrow-right"></i> Déconnexion</a>
                    </li>
                    {% else %}
                    <li class="nav-item"><a class="nav-link" href="{% url 'login' %}">Connexion</a></li>
                    <li class="nav-item"><a class="nav-link" href="{% url 'register' %}">Inscription</a></li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <div class="container-fluid">
        <div class="row">
            {% if user.is_authenticated %}
            <!-- SIDEBAR -->
            <div class="col-md-2 sidebar py-3">
                <nav class="nav flex-column">
                    <a class="nav-link {% if request.resolver_match.url_name == 'dashboard' %}active{% endif %}" href="{% url 'dashboard' %}">
                        <i class="bi bi-house-door"></i> Tableau de bord
                    </a>
                    <a class="nav-link {% if 'project' in request.resolver_match.url_name %}active{% endif %}" href="{% url 'project_list' %}">
                        <i class="bi bi-folder2-open"></i> Projets
                    </a>
                    <a class="nav-link {% if 'statistics' in request.resolver_match.url_name %}active{% endif %}" href="{% url 'statistics' %}">
                        <i class="bi bi-bar-chart-line"></i> Statistiques
                    </a>
                    <a class="nav-link" href="{% url 'profile' %}">
                        <i class="bi bi-person"></i> Mon Profil
                    </a>
                    {% if user.is_staff %}
                    <hr>
                    <a class="nav-link" href="/admin/" target="_blank">
                        <i class="bi bi-shield-lock"></i> Administration
                    </a>
                    {% endif %}
                </nav>
            </div>
            <div class="col-md-10 py-4 px-4">
            {% else %}
            <div class="col-12 py-4 px-4">
            {% endif %}
                <!-- Messages flash -->
                {% if messages %}
                <div class="mb-3">
                    {% for message in messages %}
                    <div class="alert alert-{{ message.tags|default:'info' }} alert-dismissible fade show" role="alert">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                    {% endfor %}
                </div>
                {% endif %}
                
                {% block content %}{% endblock %}
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
templates/dashboard.html
html
{% extends 'base.html' %}
{% block title %}Tableau de bord - ESMT Tasks{% endblock %}
{% block content %}
<h2 class="mb-4"><i class="bi bi-house-door text-primary"></i> Bonjour, {{ user.first_name|default:user.username }} !</h2>

<!-- Cartes statistiques -->
<div class="row g-3 mb-4">
    <div class="col-md-3">
        <div class="card stat-card h-100">
            <div class="card-body text-center">
                <div class="fs-1 fw-bold text-primary">{{ total_tasks }}</div>
                <div class="text-muted">Tâches totales</div>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card h-100" style="border-left: 4px solid #198754;">
            <div class="card-body text-center">
                <div class="fs-1 fw-bold text-success">{{ done_tasks }}</div>
                <div class="text-muted">Terminées</div>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card h-100" style="border-left: 4px solid #0d6efd;">
            <div class="card-body text-center">
                <div class="fs-1 fw-bold text-primary">{{ in_progress }}</div>
                <div class="text-muted">En cours</div>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card h-100" style="border-left: 4px solid #e8a020;">
            <div class="card-body text-center">
                <div class="fs-1 fw-bold" style="color: var(--esmt-secondary);">{{ completion_rate }}%</div>
                <div class="text-muted">Taux complétion</div>
            </div>
        </div>
    </div>
</div>

{% if overdue_count > 0 %}
<div class="alert alert-danger">
    <i class="bi bi-exclamation-triangle"></i> Vous avez <strong>{{ overdue_count }}</strong> tâche(s) en retard !
</div>
{% endif %}

<div class="row g-4">
    <!-- Mes projets -->
    <div class="col-md-6">
        <div class="card">
            <div class="card-header d-flex justify-content-between align-items-center">
                <span><i class="bi bi-folder2"></i> Mes Projets</span>
                <a href="{% url 'project_create' %}" class="btn btn-sm btn-warning">
                    <i class="bi bi-plus"></i> Nouveau
                </a>
            </div>
            <div class="card-body p-0">
                {% if created_projects %}
                <ul class="list-group list-group-flush">
                    {% for project in created_projects %}
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                            <a href="{% url 'project_detail' project.pk %}" class="text-decoration-none fw-semibold">
                                {{ project.name }}
                            </a>
                            <small class="text-muted d-block">{{ project.tasks.count }} tâche(s)</small>
                        </div>
                        <div class="text-end">
                            <span class="badge bg-primary">{{ project.get_completion_rate }}%</span>
                        </div>
                    </li>
                    {% endfor %}
                </ul>
                {% else %}
                <p class="text-center text-muted py-3">Aucun projet créé</p>
                {% endif %}
            </div>
        </div>
    </div>
    
    <!-- Mes tâches récentes -->
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <i class="bi bi-list-check"></i> Mes Tâches
            </div>
            <div class="card-body p-0">
                {% if my_tasks %}
                <ul class="list-group list-group-flush">
                    {% for task in my_tasks %}
                    <li class="list-group-item">
                        <div class="d-flex justify-content-between">
                            <span class="fw-semibold">{{ task.title }}</span>
                            <span class="badge badge-{{ task.status }} text-white">{{ task.get_status_display }}</span>
                        </div>
                        <small class="text-muted">
                            <i class="bi bi-folder2"></i> {{ task.project.name }}
                            {% if task.due_date %}
                            | <i class="bi bi-calendar"></i> {{ task.due_date|date:"d/m/Y" }}
                            {% endif %}
                        </small>
                    </li>
                    {% endfor %}
                </ul>
                {% else %}
                <p class="text-center text-muted py-3">Aucune tâche assignée</p>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{% endblock %}
templates/users/login.html
html
{% extends 'base.html' %}
{% block title %}Connexion - ESMT Tasks{% endblock %}
{% block content %}
<div class="row justify-content-center mt-5">
    <div class="col-md-5">
        <div class="card shadow-lg">
            <div class="card-header text-center py-3">
                <h4><i class="bi bi-kanban"></i> ESMT Tasks</h4>
                <p class="mb-0 opacity-75">Connectez-vous à votre compte</p>
            </div>
            <div class="card-body p-4">
                <form method="post">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label class="form-label fw-semibold">Nom d'utilisateur</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-person"></i></span>
                            <input type="text" name="username" class="form-control" required>
                        </div>
                    </div>
                    <div class="mb-3">
                        <label class="form-label fw-semibold">Mot de passe</label>
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-lock"></i></span>
                            <input type="password" name="password" class="form-control" required>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary w-100 py-2 mt-2">
                        <i class="bi bi-box-arrow-in-right"></i> Se connecter
                    </button>
                </form>
                <hr>
                <p class="text-center mb-0">
                    Pas encore de compte ? <a href="{% url 'register' %}">S'inscrire</a>
                </p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
templates/users/register.html
html
{% extends 'base.html' %}
{% block title %}Inscription - ESMT Tasks{% endblock %}
{% block content %}
<div class="row justify-content-center mt-4">
    <div class="col-md-6">
        <div class="card shadow-lg">
            <div class="card-header text-center py-3">
                <h4><i class="bi bi-person-plus"></i> Créer un compte</h4>
            </div>
            <div class="card-body p-4">
                <form method="post">
                    {% csrf_token %}
                    {% for field in form %}
                    <div class="mb-3">
                        <label class="form-label fw-semibold">{{ field.label }}</label>
                        {{ field }}
                        {% if field.errors %}
                        <div class="text-danger small">{{ field.errors }}</div>
                        {% endif %}
                    </div>
                    {% endfor %}
                    <button type="submit" class="btn btn-primary w-100 py-2">
                        <i class="bi bi-check-circle"></i> Créer mon compte
                    </button>
                </form>
                <hr>
                <p class="text-center mb-0">
                    Déjà un compte ? <a href="{% url 'login' %}">Se connecter</a>
                </p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
templates/users/profile.html
html
{% extends 'base.html' %}
{% block title %}Mon Profil{% endblock %}
{% block content %}
<div class="row">
    <div class="col-md-4">
        <div class="card text-center">
            <div class="card-body">
                {% if user.avatar %}
                <img src="{{ user.avatar.url }}" class="rounded-circle mb-3" width="100" height="100" style="object-fit:cover;">
                {% else %}
                <div class="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center mb-3" style="width:100px;height:100px;font-size:2.5rem;">
                    {{ user.username.0|upper }}
                </div>
                {% endif %}
                <h4>{{ user.get_full_name|default:user.username }}</h4>
                <span class="badge bg-warning text-dark">{{ user.get_role_display }}</span>
                <p class="text-muted mt-2">{{ user.email }}</p>
                <hr>
                <div class="row text-center">
                    <div class="col-6">
                        <div class="fw-bold text-primary fs-4">{{ user.created_projects.count }}</div>
                        <small class="text-muted">Projets créés</small>
                    </div>
                    <div class="col-6">
                        <div class="fw-bold text-success fs-4">{{ user.assigned_tasks.count }}</div>
                        <small class="text-muted">Tâches</small>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-8">
        <div class="card">
            <div class="card-header"><i class="bi bi-pencil-square"></i> Modifier le profil</div>
            <div class="card-body">
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    {% for field in form %}
                    <div class="mb-3">
                        <label class="form-label fw-semibold">{{ field.label }}</label>
                        {{ field }}
                        {% if field.errors %}<div class="text-danger small">{{ field.errors }}</div>{% endif %}
                    </div>
                    {% endfor %}
                    <button type="submit" class="btn btn-primary">
                        <i class="bi bi-save"></i> Sauvegarder
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
templates/projects/list.html
html
{% extends 'base.html' %}
{% block title %}Mes Projets{% endblock %}
{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <h2><i class="bi bi-folder2-open text-primary"></i> Projets</h2>
    <a href="{% url 'project_create' %}" class="btn btn-primary">
        <i class="bi bi-plus-circle"></i> Nouveau projet
    </a>
</div>

{% if my_projects %}
<h5 class="text-muted mb-3">Projets que j'ai créés</h5>
<div class="row g-3 mb-4">
    {% for project in my_projects %}
    <div class="col-md-4">
        <div class="card h-100">
            <div class="card-body">
                <h5 class="card-title">
                    <a href="{% url 'project_detail' project.pk %}" class="text-decoration-none">{{ project.name }}</a>
                </h5>
                <p class="text-muted small">{{ project.description|truncatewords:15 }}</p>
                <div class="d-flex justify-content-between align-items-center mt-2">
                    <small><i class="bi bi-people"></i> {{ project.members.count }} membre(s)</small>
                    <small><i class="bi bi-list-check"></i> {{ project.tasks.count }} tâche(s)</small>
                </div>
                <!-- Barre de progression -->
                <div class="progress mt-2" style="height: 6px;">
                    <div class="progress-bar bg-success" style="width: {{ project.get_completion_rate }}%"></div>
                </div>
                <small class="text-muted">{{ project.get_completion_rate }}% complété</small>
            </div>
            <div class="card-footer d-flex gap-2">
                <a href="{% url 'project_detail' project.pk %}" class="btn btn-sm btn-outline-primary flex-fill">Voir</a>
                <a href="{% url 'project_edit' project.pk %}" class="btn btn-sm btn-outline-warning flex-fill">Modifier</a>
                <a href="{% url 'project_delete' project.pk %}" class="btn btn-sm btn-outline-danger">
                    <i class="bi bi-trash"></i>
                </a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% endif %}

{% if member_projects %}
<h5 class="text-muted mb-3">Projets auxquels je participe</h5>
<div class="row g-3">
    {% for project in member_projects %}
    <div class="col-md-4">
        <div class="card h-100 border-info">
            <div class="card-body">
                <h5 class="card-title">
                    <a href="{% url 'project_detail' project.pk %}" class="text-decoration-none">{{ project.name }}</a>
                </h5>
                <small class="text-muted">Créé par {{ project.created_by.username }}</small>
            </div>
            <div class="card-footer">
                <a href="{% url 'project_detail' project.pk %}" class="btn btn-sm btn-outline-info w-100">Voir</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% endif %}

{% if not my_projects and not member_projects %}
<div class="text-center py-5">
    <i class="bi bi-folder-plus text-muted" style="font-size: 4rem;"></i>
    <h4 class="mt-3 text-muted">Aucun projet pour le moment</h4>
    <a href="{% url 'project_create' %}" class="btn btn-primary mt-2">
        <i class="bi bi-plus"></i> Créer votre premier projet
    </a>
</div>
{% endif %}
{% endblock %}
templates/projects/detail.html
html
{% extends 'base.html' %}
{% block title %}{{ project.name }}{% endblock %}
{% block content %}
<div class="d-flex justify-content-between align-items-start mb-4">
    <div>
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="{% url 'project_list' %}">Projets</a></li>
                <li class="breadcrumb-item active">{{ project.name }}</li>
            </ol>
        </nav>
        <h2>{{ project.name }}</h2>
        <p class="text-muted">{{ project.description }}</p>
    </div>
    {% if is_creator %}
    <div class="d-flex gap-2">
        <a href="{% url 'task_create' project.pk %}" class="btn btn-primary">
            <i class="bi bi-plus"></i> Ajouter tâche
        </a>
        <a href="{% url 'project_edit' project.pk %}" class="btn btn-outline-warning">
            <i class="bi bi-pencil"></i>
        </a>
    </div>
    {% endif %}
</div>

<!-- Filtres -->
<div class="card mb-3">
    <div class="card-body py-2">
        <form method="get" class="row g-2 align-items-center">
            <div class="col-auto">
                <label class="form-label mb-0 fw-semibold">Filtrer :</label>
            </div>
            <div class="col-auto">
                <select name="status" class="form-select form-select-sm" onchange="this.form.submit()">
                    <option value="">Tous les statuts</option>
                    <option value="a_faire" {% if status_filter == 'a_faire' %}selected{% endif %}>À faire</option>
                    <option value="en_cours" {% if status_filter == 'en_cours' %}selected{% endif %}>En cours</option>
                    <option value="termine" {% if status_filter == 'termine' %}selected{% endif %}>Terminé</option>
                </select>
            </div>
            <div class="col-auto">
                <select name="user" class="form-select form-select-sm" onchange="this.form.submit()">
                    <option value="">Tous les membres</option>
                    {% for member in members %}
                    <option value="{{ member.id }}" {% if user_filter == member.id|stringformat:"s" %}selected{% endif %}>
                        {{ member.username }}
                    </option>
                    {% endfor %}
                </select>
            </div>
            {% if status_filter or user_filter %}
            <div class="col-auto">
                <a href="{% url 'project_detail' project.pk %}" class="btn btn-sm btn-outline-secondary">
                    <i class="bi bi-x"></i> Effacer
                </a>
            </div>
            {% endif %}
        </form>
    </div>
</div>

<!-- Liste des tâches -->
{% if tasks %}
<div class="row g-3">
    {% for task in tasks %}
    <div class="col-md-4">
        <div class="card h-100 {% if task.is_overdue %}border-danger{% endif %}">
            <div class="card-body">
                <div class="d-flex justify-content-between mb-2">
                    <h6 class="card-title mb-0">{{ task.title }}</h6>
                    <span class="badge badge-{{ task.status }} text-white">{{ task.get_status_display }}</span>
                </div>
                <p class="text-muted small">{{ task.description|truncatewords:10 }}</p>
                
                {% if task.assigned_to %}
                <small><i class="bi bi-person"></i> {{ task.assigned_to.username }}</small><br>
                {% endif %}
                
                {% if task.due_date %}
                <small class="{% if task.is_overdue %}text-danger{% else %}text-muted{% endif %}">
                    <i class="bi bi-calendar{% if task.is_overdue %}-x{% endif %}"></i>
                    {{ task.due_date|date:"d/m/Y H:i" }}
                    {% if task.is_overdue %} ⚠️ En retard{% endif %}
                </small>
                {% endif %}
                
                <div class="mt-2">
                    <span class="badge bg-secondary">{{ task.get_priority_display }}</span>
                </div>
            </div>
            {% if is_creator or task.assigned_to == request.user %}
            <div class="card-footer d-flex gap-1">
                <a href="{% url 'task_update' task.pk %}" class="btn btn-sm btn-outline-primary flex-fill">
                    <i class="bi bi-pencil"></i> Modifier
                </a>
                {% if is_creator %}
                <a href="{% url 'task_delete' task.pk %}" class="btn btn-sm btn-outline-danger"
                   onclick="return confirm('Supprimer cette tâche ?')">
                    <i class="bi bi-trash"></i>
                </a>
                {% endif %}
            </div>
            {% endif %}
        </div>
    </div>
    {% endfor %}
</div>
{% else %}
<div class="text-center py-4">
    <i class="bi bi-clipboard text-muted" style="font-size: 3rem;"></i>
    <p class="text-muted mt-2">Aucune tâche pour le moment</p>
    {% if is_creator %}
    <a href="{% url 'task_create' project.pk %}" class="btn btn-primary">Créer une tâche</a>
    {% endif %}
</div>
{% endif %}
{% endblock %}
templates/projects/form.html
html
{% extends 'base.html' %}
{% block title %}{{ action }} un projet{% endblock %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-md-7">
        <div class="card">
            <div class="card-header">
                <i class="bi bi-folder-plus"></i> {{ action }} un projet
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    {% for field in form %}
                    <div class="mb-3">
                        <label class="form-label fw-semibold">{{ field.label }}</label>
                        {{ field }}
                        {% if field.errors %}<div class="text-danger small">{{ field.errors }}</div>{% endif %}
                        {% if field.help_text %}<div class="form-text">{{ field.help_text }}</div>{% endif %}
                    </div>
                    {% endfor %}
                    <div class="d-flex gap-2">
                        <button type="submit" class="btn btn-primary">
                            <i class="bi bi-save"></i> {{ action }}
                        </button>
                        <a href="{% url 'project_list' %}" class="btn btn-outline-secondary">Annuler</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
templates/projects/confirm_delete.html
html
{% extends 'base.html' %}
{% block title %}Supprimer le projet{% endblock %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-md-5">
        <div class="card border-danger">
            <div class="card-header bg-danger text-white">
                <i class="bi bi-exclamation-triangle"></i> Confirmer la suppression
            </div>
            <div class="card-body text-center">
                <p class="fs-5">Voulez-vous vraiment supprimer le projet <strong>{{ project.name }}</strong> ?</p>
                <p class="text-danger">Cette action supprimera aussi toutes les tâches associées !</p>
                <form method="post" class="d-flex gap-2 justify-content-center">
                    {% csrf_token %}
                    <button type="submit" class="btn btn-danger">
                        <i class="bi bi-trash"></i> Oui, supprimer
                    </button>
                    <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline-secondary">Annuler</a>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
templates/tasks/form.html
html
{% extends 'base.html' %}
{% block title %}{{ action }} une tâche{% endblock %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-md-7">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="{% url 'project_list' %}">Projets</a></li>
                <li class="breadcrumb-item"><a href="{% url 'project_detail' project.pk %}">{{ project.name }}</a></li>
                <li class="breadcrumb-item active">{{ action }} tâche</li>
            </ol>
        </nav>
        <div class="card">
            <div class="card-header">
                <i class="bi bi-clipboard-plus"></i> {{ action }} une tâche
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    {% for field in form %}
                    <div class="mb-3">
                        <label class="form-label fw-semibold">{{ field.label }}</label>
                        {{ field }}
                        {% if field.errors %}<div class="text-danger small">{{ field.errors }}</div>{% endif %}
                    </div>
                    {% endfor %}
                    <div class="d-flex gap-2">
                        <button type="submit" class="btn btn-primary">
                            <i class="bi bi-save"></i> {{ action }}
                        </button>
                        <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline-secondary">Annuler</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
templates/tasks/statistics.html
html
{% extends 'base.html' %}
{% block title %}Statistiques{% endblock %}
{% block content %}
<h2 class="mb-4"><i class="bi bi-bar-chart-line text-primary"></i> Statistiques & Évaluations</h2>

<!-- Statistiques personnelles trimestrielles -->
<div class="card mb-4">
    <div class="card-header">
        <i class="bi bi-calendar3"></i> Mes statistiques trimestrielles {{ year }}
    </div>
    <div class="card-body">
        <div class="row g-3">
            {% for q in quarterly_stats %}
            <div class="col-md-3">
                <div class="card text-center {% if q.rate >= 100 %}border-success{% elif q.rate >= 90 %}border-warning{% else %}border-secondary{% endif %}">
                    <div class="card-body">
                        <h5>{{ q.quarter }}</h5>
                        <div class="fs-2 fw-bold {% if q.rate >= 100 %}text-success{% elif q.rate >= 90 %}text-warning{% else %}text-secondary{% endif %}">
                            {{ q.rate }}%
                        </div>
                        <p class="mb-1 small">{{ q.on_time }}/{{ q.total }} dans les délais</p>
                        {% if q.rate == 100 %}
                        <span class="badge bg-success">Prime 100 000 FCFA 🎉</span>
                        {% elif q.rate >= 90 %}
                        <span class="badge bg-warning text-dark">Prime 30 000 FCFA ✨</span>
                        {% else %}
                        <span class="badge bg-secondary">Pas de prime</span>
                        {% endif %}
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</div>

<!-- Tableau des évaluations professeurs (si admin ou professeur) -->
{% if evaluations %}
<div class="card">
    <div class="card-header">
        <i class="bi bi-award"></i> Évaluations des Professeurs - {{ year }}
        <span class="badge bg-warning text-dark ms-2">Annuel</span>
    </div>
    <div class="card-body p-0">
        <table class="table table-hover mb-0">
            <thead class="table-dark">
                <tr>
                    <th>Professeur</th>
                    <th class="text-center">Tâches totales</th>
                    <th class="text-center">Dans les délais</th>
                    <th class="text-center">Taux</th>
                    <th class="text-center">Prime</th>
                </tr>
            </thead>
            <tbody>
                {% for eval in evaluations %}
                <tr class="{% if eval.rate == 100 %}table-success{% elif eval.rate >= 90 %}table-warning{% endif %}">
                    <td>
                        <strong>{{ eval.user.get_full_name|default:eval.user.username }}</strong>
                        <small class="text-muted d-block">{{ eval.user.email }}</small>
                    </td>
                    <td class="text-center">{{ eval.total }}</td>
                    <td class="text-center">{{ eval.on_time }}</td>
                    <td class="text-center">
                        <div class="progress" style="height: 20px;">
                            <div class="progress-bar {% if eval.rate == 100 %}bg-success{% elif eval.rate >= 90 %}bg-warning{% else %}bg-danger{% endif %}"
                                style="width: {{ eval.rate }}%">
                                {{ eval.rate }}%
                            </div>
                        </div>
                    </td>
                    <td class="text-center">
                        {% if eval.prime == 100000 %}
                        <span class="badge bg-success fs-6">100 000 FCFA 🏆</span>
                        {% elif eval.prime == 30000 %}
                        <span class="badge bg-warning text-dark fs-6">30 000 FCFA ⭐</span>
                        {% else %}
                        <span class="badge bg-secondary">-</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endif %}
{% endblock %}
🚀 ÉTAPE 11 : Migrations et lancement
bash
# Dans le dossier backend/
python manage.py makemigrations users
python manage.py makemigrations projects
python manage.py makemigrations tasks
python manage.py migrate

# Créer les dossiers nécessaires
mkdir -p static templates/users templates/projects templates/tasks media

# Créer un superutilisateur (admin)
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
Ouvre http://127.0.0.1:8000 dans ton navigateur !

🧪 ÉTAPE 12 : Tests unitaires
Crée backend/tests/test_tasks.py :

python
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from users.models import CustomUser
from projects.models import Project
from tasks.models import Task
from django.utils import timezone
import datetime

@pytest.mark.django_db
class TestModels(TestCase):
    def setUp(self):
        self.prof = CustomUser.objects.create_user(
            username='prof1', password='test1234', role='professeur'
        )
        self.student = CustomUser.objects.create_user(
            username='student1', password='test1234', role='etudiant'
        )
        self.project = Project.objects.create(
            name='Projet Test', created_by=self.prof
        )
        self.project.members.add(self.student)

    def test_user_roles(self):
        assert self.prof.is_professeur == True
        assert self.student.is_etudiant == True

    def test_task_on_time(self):
        future = timezone.now() + datetime.timedelta(days=5)
        task = Task.objects.create(
            title='Test', project=self.project,
            created_by=self.prof, assigned_to=self.prof,
            due_date=future, status='termine'
        )
        assert task.completed_on_time() == True

    def test_task_overdue(self):
        past = timezone.now() - datetime.timedelta(days=2)
        task = Task.objects.create(
            title='Late task', project=self.project,
            created_by=self.prof, assigned_to=self.prof,
            due_date=past, status='a_faire'
        )
        assert task.is_overdue() == True

    def test_prime_calculation(self):
        from tasks.models import PrimeEvaluation
        eval = PrimeEvaluation(
            professeur=self.prof,
            total_tasks=10,
            tasks_on_time=10,
            completion_rate=100.0,
            period='T1',
            year=2025
        )
        assert eval.calculate_prime() == 100000
        
        eval.completion_rate = 90.0
        assert eval.calculate_prime() == 30000
        
        eval.completion_rate = 80.0
        assert eval.calculate_prime() == 0
bash
# Installer et lancer les tests
pip install pytest-django
# Créer pytest.ini
echo "[pytest]
DJANGO_SETTINGS_MODULE = backend.settings
python_files = tests/*.py" > pytest.ini

pytest tests/ -v
```

---

## 📂 Structure finale du projet
```
esmt-tasks/
├── venv/
└── backend/
    ├── manage.py
    ├── pytest.ini
    ├── db.sqlite3
    ├── backend/
    │   ├── settings.py
    │   └── urls.py
    ├── users/
    │   ├── models.py       ← CustomUser
    │   ├── views.py        ← login, register, profile
    │   ├── forms.py
    │   ├── urls.py         ← routes Django
    │   ├── api_urls.py     ← routes API
    │   ├── api_views.py
    │   └── serializers.py
    ├── projects/
    │   ├── models.py       ← Project
    │   ├── views.py
    │   ├── urls.py
    │   ├── api_urls.py
    │   ├── api_views.py
    │   └── serializers.py
    ├── tasks/
    │   ├── models.py       ← Task, PrimeEvaluation
    │   ├── views.py
    │   ├── urls.py
    │   ├── api_urls.py
    │   ├── api_views.py
    │   └── serializers.py
    ├── templates/
    │   ├── base.html
    │   ├── dashboard.html
    │   ├── users/
    │   │   ├── login.html
    │   │   ├── register.html
    │   │   └── profile.html
    │   ├── projects/
    │   │   ├── list.html, detail.html, form.html...
    │   └── tasks/
    │       ├── form.html, statistics.html
    ├── static/
    └── media/
📝 Résumé des routes disponibles
URL	Fonction
/	Tableau de bord
/login/	Connexion
/register/	Inscription
/profile/	Mon profil
/projects/	Liste des projets
/projects/create/	Créer un projet
/projects/<id>/	Détail d'un projet
/tasks/create/<project_id>/	Créer une tâche
/tasks/statistics/	Statistiques & primes
API	
/api/auth/register/	Inscription API
/api/auth/login/	Connexion JWT
/api/projects/	CRUD Projets
/api/projects/<id>/tasks/	Tâches d'un projet
/api/statistics/	Stats & primes
🎯 Par où commencer maintenant ?
Ordre recommandé pour toi aujourd'hui :

✅ Installe Python, Node.js, VS Code
✅ Crée le dossier et l'environnement virtuel
✅ Copie chaque fichier dans le bon dossier
✅ Lance les migrations
✅ Crée un superuser et teste sur le navigateur
Tu veux qu'on commence par une étape en particulier ? Je peux t'aider à déboguer ou à avancer sur le frontend React si tu le souhaites ! 🚀

je travail avec pycharm

26 févr.
Parfait ! PyCharm est excellent pour Django. Voici comment configurer tout ça dans PyCharm :

🖥️ Configuration dans PyCharm
Étape 1 : Ouvrir PyCharm et créer le projet
Ouvre PyCharm
Clique sur "New Project"
Configure comme ceci :
📁 Location: C:\Users\TonNom\esmt-tasks\backend
   (ou /home/tonnom/esmt-tasks/backend sur Linux/Mac)

🐍 Python Interpreter: New environment using Virtualenv
   Base interpreter: Python 3.10+ (celui installé sur ton PC)
   
✅ Coche "Create a main.py welcome script" → NON, décoche-le
Clique "Create"
Étape 2 : Ouvrir le Terminal dans PyCharm
En bas de PyCharm, clique sur l'onglet "Terminal" (ou Alt+F12)

Tu verras quelque chose comme :

(venv) C:\Users\TonNom\esmt-tasks\backend>
Le (venv) confirme que l'environnement virtuel est activé ✅

Étape 3 : Installer les dépendances
Dans le terminal PyCharm :

bash
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow pytest-django
Attends que tout s'installe (ça prend 1-2 minutes) ✅

Étape 4 : Créer le projet Django
bash
django-admin startproject backend .
⚠️ Le point . à la fin est important — il crée le projet dans le dossier actuel

bash
python manage.py startapp users
python manage.py startapp projects
python manage.py startapp tasks
```

---

### Étape 5 : Configurer l'interpréteur Python dans PyCharm

1. Va dans **File → Settings** (ou `Ctrl+Alt+S`)
2. **Project → Python Interpreter**
3. Vérifie que tu vois le venv avec Django installé
4. Si ce n'est pas le cas, clique sur l'engrenage ⚙️ → **Add** → **Existing environment** → sélectionne `venv\Scripts\python.exe`

---

### Étape 6 : Créer la configuration de lancement Django

1. En haut à droite, clique sur **"Add Configuration"** (ou **"Edit Configurations"**)
2. Clique sur **"+"** → **"Django server"**
3. Configure :
```
Name: ESMT Tasks
Host: 127.0.0.1
Port: 8000
```
4. Dans **"Environment variables"**, ajoute :
```
DJANGO_SETTINGS_MODULE=backend.settings
```
5. Clique **OK**

Maintenant tu peux lancer le serveur avec le bouton ▶️ vert !

---

### Étape 7 : Structure des dossiers dans PyCharm

Dans le panneau **Project** à gauche, crée ces dossiers manuellement :

Fais **clic droit sur le dossier racine → New → Directory** :
```
📁 templates/
    📁 users/
    📁 projects/
    📁 tasks/
📁 static/
📁 media/
📁 tests/
Étape 8 : Créer les fichiers
Pour chaque fichier du guide précédent, dans PyCharm :

Clic droit sur le bon dossier → New → Python File (pour les .py)
Clic droit sur le bon dossier → New → File (pour les .html)
Astuce PyCharm 💡 : Activer le support Django
File → Settings → Languages & Frameworks → Django
Coche "Enable Django Support"
Django project root : sélectionne ton dossier backend
Settings : sélectionne backend/settings.py
Manage script : sélectionne manage.py
✅ Maintenant PyCharm comprend Django et t'aide avec l'autocomplétion !

Lancer les migrations depuis PyCharm
Dans le terminal intégré :

bash
python manage.py makemigrations users
python manage.py makemigrations projects
python manage.py makemigrations tasks
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ou utilise **Tools → Run manage.py Task** (raccourci `Ctrl+Alt+R`) et tape directement :
```
migrate
createsuperuser
runserver
Tu es prête à copier les fichiers ? Dis-moi où tu en es et je t'aide à avancer ! 😊

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py startapp users
C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Scripts\python.exe: can't open file 'C:\\Users\\HP\\Desktop\\Cours-Semestre1-DAR\\python\\ProjetPy\\manage.py': [Errno 2] No such file or directory

3 mars
L'erreur dit que manage.py n'existe pas encore — tu dois d'abord créer le projet Django ! Voici ce qu'il faut faire :

🔧 Correction
Dans ton terminal PyCharm, tape ces commandes dans l'ordre :

Étape 1 : Crée le projet Django d'abord
bash
django-admin startproject backend .
```
⚠️ Le **point `.`** à la fin est obligatoire !

Tu devrais voir apparaître dans PyCharm à gauche :
```
📁 ProjetPy/
  📄 manage.py        ← ce fichier doit apparaître !
  📁 backend/
      📄 settings.py
      📄 urls.py
      📄 wsgi.py
Étape 2 : Maintenant crée les apps
bash
python manage.py startapp users
python manage.py startapp projects
python manage.py startapp tasks
Étape 3 : Vérifie que tout est bien là
bash
dir
Tu dois voir manage.py dans la liste ✅

❓ Si django-admin ne fonctionne pas
Cela voudrait dire que Django n'est pas encore installé. Tape d'abord :

bash
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow pytest-django
Puis relance l'étape 1.

Dis-moi ce que tu vois après avoir tapé dir ou ls dans le terminal 😊

3 mars
Je vois le problème ! Le manage.py est dans le dossier backend/ mais ton terminal est dans ProjetPy/. Il faut naviguer dans le bon dossier.

🔧 Solution
Dans le terminal PyCharm, tape :

bash
cd backend
Puis vérifie :

bash
dir
Tu dois voir manage.py dans la liste. Ensuite tape :

bash
python manage.py startapp users
python manage.py startapp projects
python manage.py startapp tasks
```

---

## 📌 Explication de ta structure actuelle
```
📁 ProjetPy/          ← tu es ici (terminal)
  📁 .venv/
  📁 backend/         ← il faut aller ici !
      📁 backend/
          📄 settings.py
          📄 urls.py
      📄 manage.py    ← manage.py est ici
  📁 venv/
  📄 main.py
Donc toujours travailler depuis ProjetPy/backend/ pour les commandes Django. Dis-moi ce que tu vois après le cd backend ! 😊

je ne comprends pas l'etape6

3 mars
Bien sûr ! L'étape 6 c'est pour configurer le bouton ▶️ "Run" de PyCharm pour lancer ton serveur Django facilement. Voici en images :

🎯 Étape 6 en détail
1️⃣ Clique ici en haut à droite de PyCharm
PyCharm: The Python-Specific Integrated Development Environment

pythonguis.com
Python - Developers Portal

docs.openobd.com
FastAPI | PyCharm Documentation

jetbrains.com
Résultats du Web
En haut à droite de PyCharm tu vois une barre comme ça :

[  Current File  ▼]  ▶️  🐛
Clique sur "Current File" (ou ce qui est écrit là) → puis "Edit Configurations..."

2️⃣ Dans la fenêtre qui s'ouvre
Clique sur  +  (en haut à gauche de la fenêtre)
     ↓
Cherche "Django server"
     ↓
Clique dessus
3️⃣ Remplis les champs
Name:  ESMT Tasks
Host:  127.0.0.1  
Port:  8000
4️⃣ En bas, dans "Environment variables"
Clique sur l'icône 📋 à droite du champ et ajoute :

Name:   DJANGO_SETTINGS_MODULE
Value:  backend.settings
5️⃣ Clique OK ✅
⚡ Méthode plus simple pour toi
En fait, tu n'as pas besoin de faire l'étape 6 si tu utilises le terminal ! Tu peux juste taper dans le terminal :

bash
cd backend
python manage.py runserver
Et ouvrir http://127.0.0.1:8000 dans ton navigateur.

L'étape 6 c'est juste pour utiliser le bouton ▶️ au lieu du terminal. Continue avec le terminal, c'est plus simple ! 😊

Tu en es où maintenant ? Les 3 apps (users, projects, tasks) sont créées ?

👤 ÉTAPE 6 : App Users complète
users/forms.py
python

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'avatar', 'bio')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
Afficher plus
3 mars
Je vois que tu es à l'étape de créer users/forms.py ! Voici comment faire dans PyCharm :

📝 Comment créer le fichier forms.py dans PyCharm
1️⃣ Dans le panneau gauche, trouve le dossier users
📁 backend/
  📁 users/        ← clic droit ici
      📄 admin.py
      📄 apps.py
      📄 models.py
      📄 views.py
      ...
2️⃣ Clic droit sur le dossier users → New → Python File
Nom du fichier : forms
(PyCharm ajoute .py automatiquement)
3️⃣ Copie-colle le code dedans
⚠️ Attention - Ordre important !
Avant de créer forms.py, tu dois d'abord avoir créé users/models.py avec le CustomUser. Car forms.py importe depuis models.py.

Vérifie que ton users/models.py contient déjà ce code :

python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    ROLE_CHOICES = [
        ('etudiant', 'Étudiant'),
        ('professeur', 'Professeur'),
    ]
    
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='etudiant'
    )
    avatar = models.ImageField(
        upload_to='avatars/', 
        null=True, 
        blank=True
    )
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    @property
    def is_professeur(self):
        return self.role == 'professeur'
    
    @property
    def is_etudiant(self):
        return self.role == 'etudiant'
```

---

## ✅ Ordre de création des fichiers

Suis cet ordre pour éviter les erreurs :
```
1. users/models.py        ← déjà fait ?
2. settings.py            ← ajouter AUTH_USER_MODEL
3. users/forms.py         ← tu es ici
4. users/views.py
5. users/urls.py
6. users/admin.py
🔴 Très important dans settings.py
Assure-toi d'avoir cette ligne dans backend/settings.py avant de faire les migrations :

python
AUTH_USER_MODEL = 'users.CustomUser'
Sans cette ligne, Django utilisera son utilisateur par défaut et forms.py ne fonctionnera pas !

Tu as déjà créé models.py ? Montre-moi une capture de ta structure de fichiers actuelle pour qu'on avance ensemble ! 😊

3 mars
Parfait ! Tu avances très bien ! 🎉 Je vois que tu as créé tous les fichiers dans users/. Maintenant vérifions que tout est complet.

✅ Ce que tu as déjà
📁 users/
  ✅ migrations/
  ✅ admin.py
  ✅ api_urls.py
  ✅ api_views.py
  ✅ apps.py
  ✅ forms.py
  ✅ models.py
  ✅ serializers.py
  ✅ tests.py
  ✅ urls.py
  ✅ views.py
❓ Ce qu'il faut vérifier maintenant
1️⃣ Clique sur projects et tasks — ont-ils leurs fichiers ?
Il leur manque probablement ces fichiers à créer :

📁 projects/
  📄 models.py      ← à remplir
  📄 views.py       ← à remplir
  📄 urls.py        ← à remplir
  📄 api_views.py   ← à créer
  📄 api_urls.py    ← à créer
  📄 serializers.py ← à créer

📁 tasks/
  📄 models.py      ← à remplir
  📄 views.py       ← à remplir
  📄 urls.py        ← à remplir
  📄 api_views.py   ← à créer
  📄 api_urls.py    ← à créer
  📄 serializers.py ← à créer
🚦 Prochaines étapes dans l'ordre
Dis-moi simplement "oui c'est fait" ou "pas encore" pour chaque point :

settings.py est configuré avec tout le contenu donné ?
users/models.py a le code CustomUser ?
projects/models.py a le code Project ?
tasks/models.py a le code Task et PrimeEvaluation ?
On va vérifier fichier par fichier pour éviter les erreurs ! 😊

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\backend> python manage.py makemigrations users
Migrations for 'users':
  users\migrations\0001_initial.py
    + Create model CustomUser

3 mars
🎉 Excellent ! La migration users fonctionne parfaitement !

Maintenant continue dans l'ordre :

▶️ Tape ces commandes une par une
2️⃣ Migration projects
bash
python manage.py makemigrations projects
3️⃣ Migration tasks
bash
python manage.py makemigrations tasks
4️⃣ Appliquer toutes les migrations
bash
python manage.py migrate
5️⃣ Créer le compte administrateur
bash
python manage.py createsuperuser
```
Il va te demander :
```
Username: admin (ou ton prénom)
Email: ton@email.com
Password: ******** (min 8 caractères)
Password (again): ********
6️⃣ Lancer le serveur
bash
python manage.py runserver
🌐 Ensuite ouvre ton navigateur
Va sur http://127.0.0.1:8000

Et aussi http://127.0.0.1:8000/admin pour tester avec ton superuser !

Dis-moi ce qui s'affiche après chaque commande 😊

ckend> mkdir -p static templates/users templates/projects templates/tasks media                                                      
mkdir : Impossible de trouver un paramètre positionnel acceptant 
l'argument «templates/users».
Au caractère Ligne:1 : 1
+ mkdir -p static templates/users templates/projects 
templates/tasks me ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~
    + CategoryInfo          : InvalidArgument : (:) [mkdir], Para 
   meterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,mkdir

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\backend>

Afficher plus
3 mars
C'est normal ! Tu es sur Windows PowerShell qui n'accepte pas la commande Linux. Voici la version Windows :

🪟 Commandes Windows PowerShell
Tape une par une :

bash
mkdir static
bash
mkdir media
bash
mkdir templates
bash
mkdir templates\users
bash
mkdir templates\projects
bash
mkdir templates\tasks
✅ Vérifie que les dossiers sont créés
bash
dir
```

Tu dois voir dans la liste :
```
📁 static
📁 media
📁 templates
📁 backend
📁 users
📁 projects
📁 tasks
📄 manage.py
💡 Astuce PyCharm
Tu peux aussi créer les dossiers directement dans PyCharm sans le terminal :

Clic droit sur le dossier backend dans le panneau gauche
New → Directory
Tape le nom : static → OK
Répète pour media, templates
Clic droit sur templates → New → Directory → users
Répète pour projects et tasks
C'est plus simple avec PyCharm ! 😊 Dis-moi quand c'est fait !

File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\core\servers\basehttp.py", line 49, in get_internal_wsgi_application                                       
    return import_string(app_path)
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\utils\module_loading.py", line 30, in import_string                                                        
    return cached_import(module_path, class_name)
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\utils\module_loading.py", line 15, in cached_import                                                        
    module = import_module(module_path)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python313\Lib\importlib\__init__.py", line 88, in import_module                     
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load                                                                  
  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked                                                         
ModuleNotFoundError: No module named 'backend.wsgi'
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python313\Lib\threading.py", line 1041, in _bootstrap_inner                         
    self.run()
    ~~~~~~~~^^
  File "C:\Users\HP\AppData\Local\Programs\Python\Python313\Lib\threading.py", line 992, in run                                       
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper                                                                  
    fn(*args, **kwargs)
    ~~^^^^^^^^^^^^^^^^^
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\core\management\commands\runserver.py", line 143, in inner_run
    handler = self.get_handler(*args, **options)
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\contrib\staticfiles\management\commands\runserver.py", line 31, in get_handler                             
    handler = super().get_handler(*args, **options)
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\core\management\commands\runserver.py", line 73, in get_handler
    return get_internal_wsgi_application()
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\core\servers\basehttp.py", line 51, in get_internal_wsgi_application                                       
    raise ImproperlyConfigured(
    ...<2 lines>...
    ) from err
django.core.exceptions.ImproperlyConfigured: WSGI application 'backend.wsgi.application' could not be loaded; Error importing module.

Afficher plus
3 mars
L'erreur dit que Django cherche backend.wsgi mais ne le trouve pas. C'est un problème de structure de dossiers. Voyons ça !

🔍 Diagnostic
Tape dans le terminal :

bash
dir
Et aussi :

bash
dir backend
```

Montre-moi ce que tu vois. 

---

## 🤔 Le problème probable

Ta structure ressemble probablement à ça :
```
📁 backend/          ← tu es ici (terminal)
  📁 backend/        ← dossier config Django
      📄 settings.py
      📄 urls.py
      ❌ wsgi.py      ← manquant ou mal placé ?
  📄 manage.py
✅ Solution rapide
Vérifie si wsgi.py existe :
bash
dir backend
```

Tu dois voir :
```
__init__.py
asgi.py
settings.py
urls.py
wsgi.py   ← doit être là !
Si wsgi.py est absent, crée-le :
Dans PyCharm, clic droit sur le dossier backend/backend/ → New → Python File → nomme-le wsgi

Colle ce contenu :

python
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
Vérifie aussi settings.py — cette ligne doit être présente :
python
WSGI_APPLICATION = 'backend.wsgi.application'
Montre-moi le résultat de dir backend 😊

le role du super useur

3 mars
👑 Le rôle du Superuser dans Django
Le superuser c'est le compte administrateur qui a tous les droits sur l'application.

🔑 Ce qu'il peut faire
Sur /admin/ (interface d'administration Django)
✅ Voir tous les utilisateurs
✅ Créer/modifier/supprimer des utilisateurs
✅ Changer le rôle de quelqu'un (Étudiant → Professeur)
✅ Voir tous les projets
✅ Voir toutes les tâches
✅ Voir toutes les évaluations et primes
✅ Accéder à TOUT sans restriction
👥 Différence entre les 3 types d'utilisateurs
Étudiant	Professeur	Superuser/Admin
Créer des projets	✅	✅	✅
Assigner un prof à une tâche	❌	✅	✅
Voir les primes	❌	✅ (les siennes)	✅ (tous)
Accès /admin/	❌	❌	✅
Gérer les utilisateurs	❌	❌	✅
🏫 Dans le contexte ESMT
👑 Superuser = Directeur / Responsable RH
      → Gère tout, voit les primes de tous les profs

👨‍🏫 Professeur
      → Crée des projets, assigne des tâches
      → Peut voir ses propres statistiques et primes

👨‍🎓 Étudiant  
      → Crée des projets, fait ses tâches
      → Ne peut pas assigner un professeur
      → Pas accès aux primes
🚀 Comment créer le superuser
Dans ton terminal :

bash
python manage.py createsuperuser
```
```
Username: admin
Email: admin@esmt.sn
Password: Admin1234!
Password (again): Admin1234!
Ensuite va sur http://127.0.0.1:8000/admin et connecte-toi avec ces identifiants.

⚙️ Comment donner le rôle "Professeur" à quelqu'un via admin
Va sur http://127.0.0.1:8000/admin
Clique sur Users
Clique sur l'utilisateur
Change le champ Role → Professeur
Sauvegarde ✅
Tu as réussi à résoudre l'erreur wsgi ? 😊

Je veux un css plus jolie

3 mars
Voyons d'abord le skill frontend pour faire quelque chose de vraiment beau !


Reading frontend design skill
Reading frontend design skill
Je vais créer un CSS magnifique et moderne spécialement pour ESMT Tasks ! Voici le nouveau base.html complet avec un design raffiné :


Exécuté 4 commandes, fichier créé
Exécuté 4 commandes, fichier créé
Le bash semble indisponible. Je vais te donner directement les fichiers à copier-coller dans PyCharm. Voici le nouveau base.html magnifique :

🎨 Nouveau templates/base.html
Dans PyCharm, ouvre templates/base.html et remplace tout par ce code :

html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}ESMT Tasks{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        :root {
            --navy: #0d1f3c;       --navy-light: #162d56;
            --gold: #c9972c;       --gold-light: #f0b94a;
            --cream: #fdf8f2;      --white: #ffffff;
            --gray-50: #f9fafb;    --gray-100: #f3f4f6;
            --gray-200: #e5e7eb;   --gray-400: #9ca3af;
            --gray-600: #4b5563;   --gray-800: #1f2937;
            --green: #059669;      --blue: #2563eb;
            --red: #dc2626;
            --sidebar-w: 260px;    --navbar-h: 64px;
            --radius: 14px;        --radius-sm: 8px;
            --shadow: 0 4px 24px rgba(13,31,60,.08);
            --shadow-lg: 0 8px 40px rgba(13,31,60,.14);
            --transition: all .22s cubic-bezier(.4,0,.2,1);
        }
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'DM Sans', sans-serif; background: var(--cream); color: var(--gray-800); min-height: 100vh; }

        /* ── NAVBAR ── */
        .navbar { position: fixed; top: 0; left: 0; right: 0; height: var(--navbar-h); background: var(--navy); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; z-index: 1000; box-shadow: 0 2px 20px rgba(0,0,0,.25); }
        .navbar-brand { display: flex; align-items: center; gap: .6rem; text-decoration: none; }
        .logo-icon { width: 36px; height: 36px; background: linear-gradient(135deg, var(--gold), var(--gold-light)); border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; color: var(--navy); font-weight: 700; }
        .brand-text { font-family: 'Playfair Display', serif; color: var(--white); font-size: 1.25rem; }
        .brand-text span { color: var(--gold-light); }
        .navbar-right { display: flex; align-items: center; gap: 1rem; }
        .user-chip { display: flex; align-items: center; gap: .5rem; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.12); border-radius: 50px; padding: .35rem .75rem .35rem .35rem; text-decoration: none; transition: var(--transition); }
        .user-chip:hover { background: rgba(255,255,255,.14); }
        .user-avatar { width: 30px; height: 30px; border-radius: 50%; background: linear-gradient(135deg, var(--gold), var(--gold-light)); display: flex; align-items: center; justify-content: center; font-size: .8rem; font-weight: 700; color: var(--navy); }
        .user-name { color: var(--white); font-size: .85rem; font-weight: 500; }
        .role-badge { font-size: .68rem; font-weight: 600; padding: .15rem .5rem; border-radius: 20px; text-transform: uppercase; letter-spacing: .04em; }
        .role-badge.professeur { background: rgba(201,151,44,.2); color: var(--gold-light); border: 1px solid rgba(201,151,44,.3); }
        .role-badge.etudiant { background: rgba(37,99,235,.2); color: #93c5fd; border: 1px solid rgba(37,99,235,.3); }
        .nav-btn { display: flex; align-items: center; gap: .4rem; color: rgba(255,255,255,.7); text-decoration: none; padding: .4rem .7rem; border-radius: var(--radius-sm); transition: var(--transition); }
        .nav-btn:hover { color: var(--white); background: rgba(255,255,255,.08); }

        /* ── LAYOUT ── */
        .app-layout { display: flex; padding-top: var(--navbar-h); min-height: 100vh; }

        /* ── SIDEBAR ── */
        .sidebar { width: var(--sidebar-w); background: var(--white); border-right: 1px solid var(--gray-200); position: fixed; top: var(--navbar-h); bottom: 0; left: 0; overflow-y: auto; padding: 1.5rem 1rem; display: flex; flex-direction: column; gap: .25rem; }
        .sidebar-section { font-size: .7rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: var(--gray-400); padding: 1rem .75rem .4rem; }
        .sidebar-link { display: flex; align-items: center; gap: .75rem; padding: .65rem .75rem; border-radius: var(--radius-sm); color: var(--gray-600); text-decoration: none; font-size: .9rem; font-weight: 500; transition: var(--transition); position: relative; }
        .sidebar-link i { font-size: 1.05rem; width: 20px; text-align: center; }
        .sidebar-link:hover { background: var(--gray-50); color: var(--navy); }
        .sidebar-link.active { background: linear-gradient(135deg, #e8eef8, #dce6f5); color: var(--navy); font-weight: 600; }
        .sidebar-link.active::before { content: ''; position: absolute; left: 0; top: 20%; bottom: 20%; width: 3px; background: var(--gold); border-radius: 0 3px 3px 0; }
        .sidebar-divider { height: 1px; background: var(--gray-200); margin: .75rem .5rem; }

        /* ── MAIN ── */
        .main-content { margin-left: var(--sidebar-w); flex: 1; padding: 2rem 2.5rem; }

        /* ── CARDS ── */
        .card { background: var(--white); border-radius: var(--radius); box-shadow: var(--shadow); border: 1px solid var(--gray-200); overflow: hidden; }
        .card-header { padding: 1.25rem 1.5rem; border-bottom: 1px solid var(--gray-100); display: flex; align-items: center; justify-content: space-between; }
        .card-title { font-family: 'Playfair Display', serif; font-size: 1.05rem; color: var(--navy); display: flex; align-items: center; gap: .5rem; }
        .card-body { padding: 1.5rem; }

        /* ── STAT CARDS ── */
        .stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 2rem; }
        .stat-card { background: var(--white); border-radius: var(--radius); padding: 1.5rem; box-shadow: var(--shadow); border: 1px solid var(--gray-200); position: relative; overflow: hidden; transition: var(--transition); }
        .stat-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }
        .stat-card::after { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; }
        .stat-card.navy::after { background: var(--navy); }
        .stat-card.gold::after { background: var(--gold); }
        .stat-card.green::after { background: var(--green); }
        .stat-card.blue::after { background: var(--blue); }
        .stat-icon { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin-bottom: 1rem; }
        .stat-icon.navy { background: #e8eef8; color: var(--navy); }
        .stat-icon.gold { background: #fef3d0; color: var(--gold); }
        .stat-icon.green { background: #d1fae5; color: var(--green); }
        .stat-icon.blue { background: #dbeafe; color: var(--blue); }
        .stat-value { font-size: 2rem; font-weight: 700; color: var(--navy); line-height: 1; margin-bottom: .3rem; }
        .stat-label { font-size: .82rem; color: var(--gray-400); }

        /* ── BUTTONS ── */
        .btn { display: inline-flex; align-items: center; gap: .4rem; padding: .55rem 1.1rem; border-radius: var(--radius-sm); font-size: .875rem; font-weight: 600; border: none; cursor: pointer; text-decoration: none; transition: var(--transition); }
        .btn-primary { background: var(--navy); color: var(--white); }
        .btn-primary:hover { background: var(--navy-light); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(13,31,60,.25); }
        .btn-gold { background: linear-gradient(135deg, var(--gold), var(--gold-light)); color: var(--navy); }
        .btn-gold:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(201,151,44,.35); }
        .btn-outline { background: transparent; border: 1.5px solid var(--gray-200); color: var(--gray-600); }
        .btn-outline:hover { border-color: var(--navy); color: var(--navy); }
        .btn-danger { background: #fee2e2; color: var(--red); border: 1.5px solid #fecaca; }
        .btn-danger:hover { background: var(--red); color: white; }
        .btn-sm { padding: .35rem .75rem; font-size: .8rem; }

        /* ── FORMS ── */
        .form-group { margin-bottom: 1.25rem; }
        .form-label { display: block; font-size: .85rem; font-weight: 600; color: var(--gray-800); margin-bottom: .4rem; }
        .form-control, .form-select, select, input[type=text], input[type=email], input[type=password], input[type=datetime-local], textarea {
            width: 100%; padding: .65rem .9rem; border: 1.5px solid var(--gray-200); border-radius: var(--radius-sm); font-size: .9rem; font-family: 'DM Sans', sans-serif; color: var(--gray-800); background: var(--white); transition: var(--transition); outline: none; }
        .form-control:focus, select:focus, input:focus, textarea:focus { border-color: var(--navy); box-shadow: 0 0 0 3px rgba(13,31,60,.08); }
        textarea { resize: vertical; min-height: 90px; }
        .errorlist { color: var(--red); font-size: .78rem; list-style: none; margin-top: .3rem; }

        /* ── BADGES ── */
        .badge { display: inline-flex; align-items: center; gap: .3rem; padding: .25rem .65rem; border-radius: 20px; font-size: .75rem; font-weight: 600; }
        .badge-a_faire { background: #f3f4f6; color: #6b7280; }
        .badge-en_cours { background: #dbeafe; color: #1d4ed8; }
        .badge-termine { background: #d1fae5; color: #065f46; }

        /* ── PROJECT CARDS ── */
        .project-card { background: var(--white); border-radius: var(--radius); border: 1.5px solid var(--gray-200); overflow: hidden; transition: var(--transition); }
        .project-card:hover { box-shadow: var(--shadow-lg); transform: translateY(-3px); border-color: #bfcde8; }
        .project-name { font-family: 'Playfair Display', serif; font-size: 1.05rem; color: var(--navy); text-decoration: none; display: block; margin-bottom: .3rem; }
        .project-name:hover { color: var(--gold); }
        .progress-bar-wrap { height: 5px; background: var(--gray-100); border-radius: 10px; overflow: hidden; margin: .5rem 1.25rem; }
        .progress-fill { height: 100%; border-radius: 10px; background: linear-gradient(90deg, var(--navy), #2d5fa8); }
        .progress-fill.high { background: linear-gradient(90deg, var(--green), #34d399); }

        /* ── TASK CARDS ── */
        .task-card { background: var(--white); border: 1.5px solid var(--gray-200); border-radius: var(--radius); padding: 1.1rem 1.25rem; transition: var(--transition); margin-bottom: .75rem; }
        .task-card:hover { border-color: #bfcde8; box-shadow: 0 4px 16px rgba(13,31,60,.08); transform: translateY(-2px); }
        .task-card.overdue { border-left: 3px solid var(--red); }
        .task-title { font-weight: 600; color: var(--navy); font-size: .95rem; }
        .task-meta { display: flex; align-items: center; gap: .75rem; flex-wrap: wrap; font-size: .78rem; color: var(--gray-400); margin-top: .5rem; }

        /* ── ALERTS ── */
        .alert { padding: .9rem 1.1rem; border-radius: var(--radius-sm); font-size: .875rem; display: flex; align-items: center; gap: .6rem; margin-bottom: 1rem; animation: slideDown .3s ease; }
        @keyframes slideDown { from { opacity:0; transform:translateY(-8px); } to { opacity:1; transform:translateY(0); } }
        .alert-success { background: #d1fae5; color: #065f46; border: 1px solid #a7f3d0; }
        .alert-error, .alert-danger { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
        .alert-info { background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }
        .alert-warning { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
        .alert-close { margin-left: auto; background: none; border: none; cursor: pointer; color: inherit; opacity: .6; }

        /* ── TABLES ── */
        .table-container { overflow-x: auto; border-radius: var(--radius); border: 1px solid var(--gray-200); }
        table { width: 100%; border-collapse: collapse; font-size: .875rem; }
        thead th { background: var(--navy); color: rgba(255,255,255,.85); font-weight: 600; padding: .9rem 1.1rem; text-align: left; font-size: .8rem; text-transform: uppercase; letter-spacing: .04em; }
        tbody tr { border-bottom: 1px solid var(--gray-100); transition: var(--transition); }
        tbody tr:hover { background: var(--gray-50); }
        tbody td { padding: .9rem 1.1rem; }

        /* ── PAGE HEADER ── */
        .page-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 2rem; gap: 1rem; }
        .page-title { font-family: 'Playfair Display', serif; font-size: 1.75rem; color: var(--navy); }
        .page-subtitle { font-size: .875rem; color: var(--gray-400); margin-bottom: .25rem; }
        .breadcrumb { display: flex; align-items: center; gap: .4rem; font-size: .8rem; color: var(--gray-400); margin-bottom: .5rem; list-style: none; }
        .breadcrumb a { color: var(--gray-400); text-decoration: none; }
        .breadcrumb a:hover { color: var(--navy); }

        /* ── EMPTY STATE ── */
        .empty-state { text-align: center; padding: 4rem 2rem; color: var(--gray-400); }
        .empty-state i { font-size: 3rem; display: block; margin-bottom: 1rem; opacity: .4; }
        .empty-state h4 { color: var(--gray-600); margin-bottom: .5rem; }
        .empty-state p { font-size: .875rem; margin-bottom: 1.5rem; }

        /* ── FILTER BAR ── */
        .filter-bar { display: flex; align-items: center; gap: .75rem; padding: .9rem 1.25rem; background: var(--white); border-radius: var(--radius); border: 1px solid var(--gray-200); margin-bottom: 1.5rem; flex-wrap: wrap; }
        .filter-bar label { font-size: .8rem; font-weight: 600; color: var(--gray-400); text-transform: uppercase; letter-spacing: .06em; }
        .filter-select { padding: .4rem .75rem; border: 1.5px solid var(--gray-200); border-radius: 6px; font-size: .85rem; font-family: 'DM Sans', sans-serif; background: var(--gray-50); outline: none; width: auto; }

        /* ── AUTH PAGES ── */
        .auth-wrapper { min-height: 100vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, var(--navy) 0%, #1e4080 60%, #2d5fa8 100%); position: relative; overflow: hidden; padding: 2rem; }
        .auth-wrapper::before { content: ''; position: absolute; width: 500px; height: 500px; border-radius: 50%; background: rgba(201,151,44,.08); top: -100px; right: -100px; }
        .auth-card { background: var(--white); border-radius: 20px; width: 100%; max-width: 440px; box-shadow: 0 25px 60px rgba(0,0,0,.3); overflow: hidden; position: relative; z-index: 1; }
        .auth-card-header { background: linear-gradient(135deg, var(--navy), #1e4080); padding: 2rem; text-align: center; }
        .auth-logo { width: 56px; height: 56px; background: linear-gradient(135deg, var(--gold), var(--gold-light)); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: var(--navy); margin: 0 auto 1rem; }
        .auth-card-header h2 { font-family: 'Playfair Display', serif; color: var(--white); font-size: 1.5rem; margin-bottom: .25rem; }
        .auth-card-header p { color: rgba(255,255,255,.6); font-size: .875rem; }
        .auth-card-body { padding: 2rem; }
        .auth-link { color: var(--navy); font-weight: 600; text-decoration: none; }
        .auth-link:hover { color: var(--gold); }

        /* ── SCROLLBAR ── */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: var(--gray-50); }
        ::-webkit-scrollbar-thumb { background: var(--gray-200); border-radius: 3px; }

        /* ── RESPONSIVE ── */
        @media (max-width: 768px) {
            .sidebar { display: none; }
            .main-content { margin-left: 0; padding: 1.25rem; }
            .stat-grid { grid-template-columns: repeat(2, 1fr); }
            .page-header { flex-direction: column; }
        }
    </style>
</head>
<body>

{% if user.is_authenticated %}
<nav class="navbar">
    <a href="{% url 'dashboard' %}" class="navbar-brand">
        <div class="logo-icon">E</div>
        <span class="brand-text">ESMT <span>Tasks</span></span>
    </a>
    <div class="navbar-right">
        <a href="{% url 'profile' %}" class="user-chip">
            <div class="user-avatar">{{ user.username.0|upper }}</div>
            <span class="user-name">{{ user.username }}</span>
            <span class="role-badge {{ user.role }}">{{ user.get_role_display }}</span>
        </a>
        <a href="{% url 'logout' %}" class="nav-btn">
            <i class="bi bi-box-arrow-right"></i>
        </a>
    </div>
</nav>

<div class="app-layout">
    <aside class="sidebar">
        <span class="sidebar-section">Menu</span>
        <a href="{% url 'dashboard' %}" class="sidebar-link {% if request.resolver_match.url_name == 'dashboard' %}active{% endif %}">
            <i class="bi bi-house-door"></i> Tableau de bord
        </a>
        <a href="{% url 'project_list' %}" class="sidebar-link {% if 'project' in request.resolver_match.url_name %}active{% endif %}">
            <i class="bi bi-folder2-open"></i> Projets
        </a>
        <a href="{% url 'statistics' %}" class="sidebar-link {% if 'statistics' in request.resolver_match.url_name %}active{% endif %}">
            <i class="bi bi-bar-chart-line"></i> Statistiques
        </a>
        <div class="sidebar-divider"></div>
        <span class="sidebar-section">Compte</span>
        <a href="{% url 'profile' %}" class="sidebar-link {% if request.resolver_match.url_name == 'profile' %}active{% endif %}">
            <i class="bi bi-person-circle"></i> Mon Profil
        </a>
        {% if user.is_staff %}
        <a href="/admin/" class="sidebar-link" target="_blank">
            <i class="bi bi-shield-lock"></i> Administration
        </a>
        {% endif %}
        <div class="sidebar-divider"></div>
        <a href="{% url 'logout' %}" class="sidebar-link" style="color:var(--red);">
            <i class="bi bi-box-arrow-right"></i> Déconnexion
        </a>
    </aside>

    <main class="main-content">
        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i>
                {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}
        {% block content %}{% endblock %}
    </main>
</div>

{% else %}
{% block content %}{% endblock %}
{% endif %}

</body>
</html>
🖼️ Aperçu du nouveau design
Le nouveau style apporte :

Avant	Après
Bootstrap générique	Design sur mesure ESMT
Bleu/gris basique	Marine + Or (couleurs officielles)
Sidebar Bootstrap	Sidebar élégante avec indicateur doré
Boutons plats	Boutons avec hover animé
Fonts système	Playfair Display + DM Sans
Cards simples	Cards avec ombre et bande colorée
🔄 Met aussi à jour templates/users/login.html
html
{% extends 'base.html' %}
{% block title %}Connexion{% endblock %}
{% block content %}
<div class="auth-wrapper">
    <div class="auth-card">
        <div class="auth-card-header">
            <div class="auth-logo"><i class="bi bi-kanban-fill"></i></div>
            <h2>ESMT Tasks</h2>
            <p>Connectez-vous à votre espace</p>
        </div>
        <div class="auth-card-body">
            <form method="post">
                {% csrf_token %}
                <div class="form-group">
                    <label class="form-label">Nom d'utilisateur</label>
                    <input type="text" name="username" placeholder="Votre identifiant" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Mot de passe</label>
                    <input type="password" name="password" placeholder="••••••••" required>
                </div>
                <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;padding:.75rem;">
                    <i class="bi bi-box-arrow-in-right"></i> Se connecter
                </button>
            </form>
            <p style="text-align:center;margin-top:1.5rem;font-size:.875rem;color:var(--gray-400);">
                Pas encore de compte ? <a href="{% url 'register' %}" class="auth-link">S'inscrire</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
Remplace ces deux fichiers dans PyCharm et recharge la page ! Tu verras un design professionnel et moderne 🎨✨

avec du blanc et du beige et marron clair

3 mars
D'accord, palette blanc, beige et marron clair — très élégant ! Voici le nouveau base.html complet :

🎨 Nouveau templates/base.html — Thème Beige & Marron
html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}ESMT Tasks{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        :root {
            --brown-dark:   #5c3d2e;
            --brown:        #7d5a4f;
            --brown-light:  #a67c6d;
            --brown-pale:   #c8a99a;
            --beige-dark:   #e8d5c4;
            --beige:        #f2e8dc;
            --beige-light:  #f8f2eb;
            --cream:        #fdf9f5;
            --white:        #ffffff;
            --gray-400:     #a8998f;
            --gray-600:     #6b5c54;
            --gray-800:     #3d2c26;
            --green:        #5a8a6a;
            --red:          #b85c5c;
            --blue:         #5c7aa8;

            --sidebar-w:    265px;
            --navbar-h:     64px;
            --radius:       16px;
            --radius-sm:    10px;
            --shadow:       0 4px 24px rgba(92,61,46,.07);
            --shadow-lg:    0 8px 40px rgba(92,61,46,.13);
            --transition:   all .22s cubic-bezier(.4,0,.2,1);
        }

        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'DM Sans', sans-serif; background: var(--cream); color: var(--gray-800); min-height: 100vh; }

        /* ══ NAVBAR ══ */
        .navbar {
            position: fixed; top: 0; left: 0; right: 0;
            height: var(--navbar-h);
            background: var(--brown-dark);
            display: flex; align-items: center; justify-content: space-between;
            padding: 0 2rem;
            z-index: 1000;
            box-shadow: 0 2px 20px rgba(92,61,46,.25);
        }
        .navbar-brand { display: flex; align-items: center; gap: .65rem; text-decoration: none; }
        .logo-icon {
            width: 38px; height: 38px;
            background: linear-gradient(135deg, var(--beige-dark), var(--beige));
            border-radius: 11px;
            display: flex; align-items: center; justify-content: center;
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.3rem; font-weight: 700;
            color: var(--brown-dark);
            box-shadow: 0 2px 8px rgba(0,0,0,.15);
        }
        .brand-text { font-family: 'Cormorant Garamond', serif; color: var(--beige-light); font-size: 1.35rem; font-weight: 600; letter-spacing: .02em; }
        .brand-text span { color: var(--beige-dark); }
        .navbar-right { display: flex; align-items: center; gap: .75rem; }
        .user-chip {
            display: flex; align-items: center; gap: .5rem;
            background: rgba(255,255,255,.08);
            border: 1px solid rgba(255,255,255,.15);
            border-radius: 50px;
            padding: .3rem .75rem .3rem .3rem;
            text-decoration: none; transition: var(--transition);
        }
        .user-chip:hover { background: rgba(255,255,255,.14); }
        .user-avatar {
            width: 32px; height: 32px; border-radius: 50%;
            background: linear-gradient(135deg, var(--beige-dark), var(--brown-pale));
            display: flex; align-items: center; justify-content: center;
            font-size: .85rem; font-weight: 700; color: var(--brown-dark);
        }
        .user-name { color: var(--beige-light); font-size: .85rem; font-weight: 500; }
        .role-badge { font-size: .67rem; font-weight: 600; padding: .15rem .5rem; border-radius: 20px; text-transform: uppercase; letter-spacing: .05em; }
        .role-badge.professeur { background: rgba(200,169,154,.2); color: var(--beige-dark); border: 1px solid rgba(200,169,154,.3); }
        .role-badge.etudiant   { background: rgba(92,122,168,.2); color: #a8c0e8; border: 1px solid rgba(92,122,168,.3); }
        .nav-btn { color: rgba(255,255,255,.6); text-decoration: none; padding: .4rem .65rem; border-radius: var(--radius-sm); transition: var(--transition); font-size: .95rem; }
        .nav-btn:hover { color: var(--beige-light); background: rgba(255,255,255,.08); }

        /* ══ LAYOUT ══ */
        .app-layout { display: flex; padding-top: var(--navbar-h); min-height: 100vh; }

        /* ══ SIDEBAR ══ */
        .sidebar {
            width: var(--sidebar-w);
            background: var(--white);
            border-right: 1px solid var(--beige-dark);
            position: fixed; top: var(--navbar-h); bottom: 0; left: 0;
            overflow-y: auto;
            padding: 1.5rem .9rem;
            display: flex; flex-direction: column; gap: .2rem;
        }
        .sidebar-section { font-size: .68rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--brown-pale); padding: 1rem .75rem .35rem; }
        .sidebar-link {
            display: flex; align-items: center; gap: .7rem;
            padding: .65rem .85rem;
            border-radius: var(--radius-sm);
            color: var(--gray-600); text-decoration: none;
            font-size: .88rem; font-weight: 500;
            transition: var(--transition); position: relative;
        }
        .sidebar-link i { font-size: 1rem; width: 20px; text-align: center; color: var(--brown-pale); transition: var(--transition); }
        .sidebar-link:hover { background: var(--beige-light); color: var(--brown-dark); }
        .sidebar-link:hover i { color: var(--brown); }
        .sidebar-link.active { background: var(--beige); color: var(--brown-dark); font-weight: 600; }
        .sidebar-link.active i { color: var(--brown); }
        .sidebar-link.active::before { content: ''; position: absolute; left: 0; top: 18%; bottom: 18%; width: 3px; background: var(--brown); border-radius: 0 3px 3px 0; }
        .sidebar-divider { height: 1px; background: var(--beige-dark); margin: .6rem .5rem; }

        /* ══ MAIN ══ */
        .main-content { margin-left: var(--sidebar-w); flex: 1; padding: 2.25rem 2.5rem; }

        /* ══ PAGE HEADER ══ */
        .page-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 2rem; gap: 1rem; flex-wrap: wrap; }
        .page-subtitle { font-size: .82rem; color: var(--brown-pale); margin-bottom: .2rem; text-transform: uppercase; letter-spacing: .08em; font-weight: 600; }
        .page-title { font-family: 'Cormorant Garamond', serif; font-size: 2rem; color: var(--brown-dark); line-height: 1.15; font-weight: 700; }
        .breadcrumb { display: flex; align-items: center; gap: .4rem; font-size: .78rem; color: var(--brown-pale); list-style: none; margin-bottom: .5rem; }
        .breadcrumb a { color: var(--brown-pale); text-decoration: none; }
        .breadcrumb a:hover { color: var(--brown-dark); }

        /* ══ CARDS ══ */
        .card { background: var(--white); border-radius: var(--radius); box-shadow: var(--shadow); border: 1px solid var(--beige-dark); overflow: hidden; }
        .card-header { padding: 1.2rem 1.5rem; border-bottom: 1px solid var(--beige); display: flex; align-items: center; justify-content: space-between; background: var(--white); }
        .card-title { font-family: 'Cormorant Garamond', serif; font-size: 1.15rem; color: var(--brown-dark); display: flex; align-items: center; gap: .5rem; font-weight: 600; }
        .card-body { padding: 1.5rem; }

        /* ══ STAT CARDS ══ */
        .stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 2rem; }
        .stat-card {
            background: var(--white); border-radius: var(--radius);
            padding: 1.5rem; border: 1px solid var(--beige-dark);
            box-shadow: var(--shadow); position: relative; overflow: hidden;
            transition: var(--transition);
        }
        .stat-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }
        .stat-card::after { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; border-radius: 3px 3px 0 0; }
        .stat-card.c1::after { background: var(--brown-dark); }
        .stat-card.c2::after { background: var(--green); }
        .stat-card.c3::after { background: var(--blue); }
        .stat-card.c4::after { background: var(--brown-light); }
        .stat-icon { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin-bottom: .9rem; }
        .stat-icon.c1 { background: #ede0d4; color: var(--brown-dark); }
        .stat-icon.c2 { background: #d4ede0; color: var(--green); }
        .stat-icon.c3 { background: #d4dff0; color: var(--blue); }
        .stat-icon.c4 { background: #f0e4de; color: var(--brown-light); }
        .stat-value { font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700; color: var(--brown-dark); line-height: 1; margin-bottom: .25rem; }
        .stat-label { font-size: .8rem; color: var(--brown-pale); font-weight: 500; }

        /* ══ BUTTONS ══ */
        .btn { display: inline-flex; align-items: center; gap: .45rem; padding: .55rem 1.15rem; border-radius: var(--radius-sm); font-size: .875rem; font-weight: 600; border: none; cursor: pointer; text-decoration: none; transition: var(--transition); font-family: 'DM Sans', sans-serif; }
        .btn-primary { background: var(--brown-dark); color: var(--beige-light); }
        .btn-primary:hover { background: var(--brown); transform: translateY(-1px); box-shadow: 0 4px 14px rgba(92,61,46,.3); }
        .btn-beige { background: var(--beige); color: var(--brown-dark); border: 1.5px solid var(--beige-dark); }
        .btn-beige:hover { background: var(--beige-dark); transform: translateY(-1px); }
        .btn-outline { background: transparent; border: 1.5px solid var(--beige-dark); color: var(--gray-600); }
        .btn-outline:hover { border-color: var(--brown); color: var(--brown-dark); background: var(--beige-light); }
        .btn-danger { background: #f5e8e8; color: var(--red); border: 1.5px solid #e8c8c8; }
        .btn-danger:hover { background: var(--red); color: white; }
        .btn-sm { padding: .35rem .8rem; font-size: .8rem; }

        /* ══ FORMS ══ */
        .form-group { margin-bottom: 1.25rem; }
        .form-label { display: block; font-size: .83rem; font-weight: 600; color: var(--brown-dark); margin-bottom: .4rem; letter-spacing: .01em; }
        input[type=text], input[type=email], input[type=password], input[type=datetime-local],
        select, textarea, .form-control, .form-select {
            width: 100%; padding: .65rem .95rem;
            border: 1.5px solid var(--beige-dark);
            border-radius: var(--radius-sm);
            font-size: .9rem; font-family: 'DM Sans', sans-serif;
            color: var(--gray-800); background: var(--beige-light);
            transition: var(--transition); outline: none;
        }
        input:focus, select:focus, textarea:focus, .form-control:focus {
            border-color: var(--brown);
            background: var(--white);
            box-shadow: 0 0 0 3px rgba(92,61,46,.08);
        }
        textarea { resize: vertical; min-height: 90px; }
        .errorlist { color: var(--red); font-size: .78rem; list-style: none; margin-top: .3rem; }

        /* ══ BADGES ══ */
        .badge { display: inline-flex; align-items: center; gap: .3rem; padding: .25rem .7rem; border-radius: 20px; font-size: .73rem; font-weight: 600; }
        .badge-a_faire  { background: #f0ebe5; color: #7d6557; }
        .badge-en_cours { background: #dde8f5; color: #3a5f8a; }
        .badge-termine  { background: #d8eddf; color: #2f6b45; }
        .badge-urgente  { background: #f5dede; color: #8a3030; }
        .badge-haute    { background: #f5ead8; color: #7a5020; }
        .badge-normale  { background: #e8f0f5; color: #3a5a70; }
        .badge-basse    { background: #e8f5ea; color: #2f6040; }

        /* ══ PROJECT CARDS ══ */
        .project-card { background: var(--white); border-radius: var(--radius); border: 1.5px solid var(--beige-dark); overflow: hidden; transition: var(--transition); }
        .project-card:hover { box-shadow: var(--shadow-lg); transform: translateY(-3px); border-color: var(--brown-pale); }
        .project-header { padding: 1.25rem 1.25rem .75rem; }
        .project-name { font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; font-weight: 600; color: var(--brown-dark); text-decoration: none; display: block; margin-bottom: .25rem; }
        .project-name:hover { color: var(--brown-light); }
        .project-desc { font-size: .82rem; color: var(--brown-pale); line-height: 1.5; }
        .project-stats { display: flex; gap: 1rem; padding: .7rem 1.25rem; border-top: 1px solid var(--beige); font-size: .79rem; color: var(--gray-600); }
        .project-footer { padding: .75rem 1.25rem; border-top: 1px solid var(--beige); display: flex; gap: .5rem; background: var(--beige-light); }
        .progress-wrap { height: 5px; background: var(--beige); border-radius: 10px; overflow: hidden; margin: .4rem 1.25rem .6rem; }
        .progress-fill { height: 100%; border-radius: 10px; background: linear-gradient(90deg, var(--brown-dark), var(--brown-light)); }
        .progress-fill.high { background: linear-gradient(90deg, var(--green), #8ac4a0); }

        /* ══ TASK CARDS ══ */
        .task-card { background: var(--white); border: 1.5px solid var(--beige-dark); border-radius: var(--radius); padding: 1.1rem 1.3rem; transition: var(--transition); margin-bottom: .75rem; }
        .task-card:hover { border-color: var(--brown-pale); box-shadow: 0 4px 16px rgba(92,61,46,.09); transform: translateY(-2px); }
        .task-card.overdue { border-left: 3px solid var(--red); }
        .task-title { font-weight: 600; color: var(--brown-dark); font-size: .93rem; margin-bottom: .35rem; }
        .task-meta { display: flex; align-items: center; gap: .75rem; flex-wrap: wrap; font-size: .77rem; color: var(--brown-pale); margin-top: .45rem; }

        /* ══ ALERTS ══ */
        .alert { padding: .85rem 1.1rem; border-radius: var(--radius-sm); font-size: .875rem; display: flex; align-items: center; gap: .6rem; margin-bottom: 1rem; animation: slideDown .3s ease; }
        @keyframes slideDown { from { opacity:0; transform:translateY(-8px); } to { opacity:1; transform:translateY(0); } }
        .alert-success { background: #e0f0e6; color: #2f6040; border: 1px solid #b8dcca; }
        .alert-error, .alert-danger { background: #f5e0e0; color: #8a2020; border: 1px solid #e0b8b8; }
        .alert-info { background: #e0eaf5; color: #2a4a78; border: 1px solid #b8cce0; }
        .alert-warning { background: #f5ecd8; color: #7a5010; border: 1px solid #e0cca8; }
        .alert-close { margin-left: auto; background: none; border: none; cursor: pointer; color: inherit; opacity: .6; font-size: 1rem; }
        .alert-close:hover { opacity: 1; }

        /* ══ TABLES ══ */
        .table-container { overflow-x: auto; border-radius: var(--radius); border: 1px solid var(--beige-dark); }
        table { width: 100%; border-collapse: collapse; font-size: .875rem; }
        thead th { background: var(--brown-dark); color: rgba(255,255,255,.85); font-weight: 600; padding: .9rem 1.1rem; text-align: left; font-size: .78rem; text-transform: uppercase; letter-spacing: .05em; }
        tbody tr { border-bottom: 1px solid var(--beige); transition: var(--transition); }
        tbody tr:hover { background: var(--beige-light); }
        tbody tr:last-child { border-bottom: none; }
        tbody td { padding: .9rem 1.1rem; color: var(--gray-800); }

        /* ══ FILTER BAR ══ */
        .filter-bar { display: flex; align-items: center; gap: .75rem; padding: .9rem 1.25rem; background: var(--white); border-radius: var(--radius); border: 1px solid var(--beige-dark); margin-bottom: 1.5rem; flex-wrap: wrap; }
        .filter-label { font-size: .75rem; font-weight: 700; color: var(--brown-pale); text-transform: uppercase; letter-spacing: .08em; }
        .filter-select { padding: .4rem .8rem; border: 1.5px solid var(--beige-dark); border-radius: 8px; font-size: .84rem; font-family: 'DM Sans', sans-serif; color: var(--brown-dark); background: var(--beige-light); outline: none; cursor: pointer; width: auto; }
        .filter-select:focus { border-color: var(--brown); }

        /* ══ EMPTY STATE ══ */
        .empty-state { text-align: center; padding: 4rem 2rem; color: var(--brown-pale); }
        .empty-state i { font-size: 3rem; display: block; margin-bottom: 1rem; opacity: .35; }
        .empty-state h4 { color: var(--brown); margin-bottom: .5rem; font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; }
        .empty-state p { font-size: .875rem; margin-bottom: 1.5rem; }

        /* ══ AUTH ══ */
        .auth-wrapper {
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
            background: linear-gradient(150deg, var(--brown-dark) 0%, var(--brown) 50%, var(--brown-light) 100%);
            position: relative; overflow: hidden; padding: 2rem;
        }
        .auth-wrapper::before { content: ''; position: absolute; width: 600px; height: 600px; border-radius: 50%; background: rgba(248,242,235,.05); top: -200px; right: -150px; }
        .auth-wrapper::after  { content: ''; position: absolute; width: 350px; height: 350px; border-radius: 50%; background: rgba(255,255,255,.04); bottom: -100px; left: -80px; }
        .auth-card { background: var(--white); border-radius: 22px; width: 100%; max-width: 440px; box-shadow: 0 30px 70px rgba(0,0,0,.25); overflow: hidden; position: relative; z-index: 1; }
        .auth-card-header { background: linear-gradient(135deg, var(--brown-dark), var(--brown)); padding: 2.25rem 2rem; text-align: center; }
        .auth-logo { width: 58px; height: 58px; background: linear-gradient(135deg, var(--beige-dark), var(--beige-light)); border-radius: 18px; display: flex; align-items: center; justify-content: center; font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; font-weight: 700; color: var(--brown-dark); margin: 0 auto 1rem; box-shadow: 0 4px 16px rgba(0,0,0,.15); }
        .auth-card-header h2 { font-family: 'Cormorant Garamond', serif; color: var(--beige-light); font-size: 1.65rem; margin-bottom: .3rem; font-weight: 600; }
        .auth-card-header p { color: rgba(255,255,255,.55); font-size: .85rem; }
        .auth-card-body { padding: 2rem; }
        .auth-link { color: var(--brown-dark); font-weight: 600; text-decoration: none; }
        .auth-link:hover { color: var(--brown-light); }

        /* ══ SCROLLBAR ══ */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: var(--beige-light); }
        ::-webkit-scrollbar-thumb { background: var(--beige-dark); border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--brown-pale); }

        /* ══ RESPONSIVE ══ */
        @media (max-width: 768px) {
            .sidebar { display: none; }
            .main-content { margin-left: 0; padding: 1.25rem; }
            .stat-grid { grid-template-columns: repeat(2, 1fr); }
            .page-header { flex-direction: column; }
        }
    </style>
</head>
<body>

{% if user.is_authenticated %}

<!-- NAVBAR -->
<nav class="navbar">
    <a href="{% url 'dashboard' %}" class="navbar-brand">
        <div class="logo-icon">E</div>
        <span class="brand-text">ESMT <span>Tasks</span></span>
    </a>
    <div class="navbar-right">
        <a href="{% url 'profile' %}" class="user-chip">
            <div class="user-avatar">{{ user.username.0|upper }}</div>
            <span class="user-name">{{ user.username }}</span>
            <span class="role-badge {{ user.role }}">{{ user.get_role_display }}</span>
        </a>
        <a href="{% url 'logout' %}" class="nav-btn" title="Déconnexion">
            <i class="bi bi-box-arrow-right"></i>
        </a>
    </div>
</nav>

<div class="app-layout">

    <!-- SIDEBAR -->
    <aside class="sidebar">
        <span class="sidebar-section">Navigation</span>
        <a href="{% url 'dashboard' %}" class="sidebar-link {% if request.resolver_match.url_name == 'dashboard' %}active{% endif %}">
            <i class="bi bi-house-door"></i> Tableau de bord
        </a>
        <a href="{% url 'project_list' %}" class="sidebar-link {% if 'project' in request.resolver_match.url_name %}active{% endif %}">
            <i class="bi bi-folder2-open"></i> Projets
        </a>
        <a href="{% url 'statistics' %}" class="sidebar-link {% if 'statistics' in request.resolver_match.url_name %}active{% endif %}">
            <i class="bi bi-bar-chart-line"></i> Statistiques
        </a>

        <div class="sidebar-divider"></div>
        <span class="sidebar-section">Compte</span>

        <a href="{% url 'profile' %}" class="sidebar-link {% if request.resolver_match.url_name == 'profile' %}active{% endif %}">
            <i class="bi bi-person-circle"></i> Mon Profil
        </a>
        {% if user.is_staff %}
        <a href="/admin/" class="sidebar-link" target="_blank">
            <i class="bi bi-shield-lock"></i> Administration
        </a>
        {% endif %}

        <div class="sidebar-divider"></div>
        <a href="{% url 'logout' %}" class="sidebar-link" style="color:var(--red);">
            <i class="bi bi-box-arrow-right"></i> Déconnexion
        </a>
    </aside>

    <!-- CONTENU PRINCIPAL -->
    <main class="main-content">
        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i>
                {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        {% block content %}{% endblock %}
    </main>
</div>

{% else %}
{% block content %}{% endblock %}
{% endif %}

</body>
</html>
🔄 Mets aussi à jour le dashboard.html
html
{% extends 'base.html' %}
{% block title %}Tableau de bord{% endblock %}
{% block content %}

<div class="page-header">
    <div>
        <p class="page-subtitle">Bienvenue de retour</p>
        <h1 class="page-title">{{ user.first_name|default:user.username }} 👋</h1>
    </div>
    <a href="{% url 'project_create' %}" class="btn btn-primary">
        <i class="bi bi-plus-lg"></i> Nouveau projet
    </a>
</div>

<!-- Statistiques -->
<div class="stat-grid">
    <div class="stat-card c1">
        <div class="stat-icon c1"><i class="bi bi-list-check"></i></div>
        <div class="stat-value">{{ total_tasks }}</div>
        <div class="stat-label">Tâches totales</div>
    </div>
    <div class="stat-card c2">
        <div class="stat-icon c2"><i class="bi bi-check-circle"></i></div>
        <div class="stat-value">{{ done_tasks }}</div>
        <div class="stat-label">Terminées</div>
    </div>
    <div class="stat-card c3">
        <div class="stat-icon c3"><i class="bi bi-arrow-repeat"></i></div>
        <div class="stat-value">{{ in_progress }}</div>
        <div class="stat-label">En cours</div>
    </div>
    <div class="stat-card c4">
        <div class="stat-icon c4"><i class="bi bi-graph-up"></i></div>
        <div class="stat-value">{{ completion_rate }}%</div>
        <div class="stat-label">Taux de complétion</div>
    </div>
</div>

{% if overdue_count > 0 %}
<div class="alert alert-danger">
    <i class="bi bi-exclamation-triangle-fill"></i>
    <strong>{{ overdue_count }} tâche(s) en retard !</strong> Pensez à les traiter rapidement.
</div>
{% endif %}

<div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">

    <!-- Mes Projets -->
    <div class="card">
        <div class="card-header">
            <span class="card-title"><i class="bi bi-folder2-open"></i> Mes Projets</span>
            <a href="{% url 'project_list' %}" class="btn btn-outline btn-sm">Voir tout</a>
        </div>
        <div class="card-body" style="padding:0;">
            {% if created_projects %}
                {% for project in created_projects %}
                <div style="padding:.9rem 1.4rem; border-bottom:1px solid var(--beige); display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <a href="{% url 'project_detail' project.pk %}" class="project-name" style="font-size:.9rem;">{{ project.name }}</a>
                        <div style="font-size:.77rem; color:var(--brown-pale); margin-top:.1rem;">{{ project.tasks.count }} tâche(s)</div>
                    </div>
                    <span style="font-size:.82rem; font-weight:700; color:var(--brown-dark);">{{ project.get_completion_rate }}%</span>
                </div>
                {% endfor %}
            {% else %}
            <div class="empty-state" style="padding:2.5rem;">
                <i class="bi bi-folder-plus"></i>
                <h4>Aucun projet</h4>
                <p>Créez votre premier projet</p>
                <a href="{% url 'project_create' %}" class="btn btn-primary btn-sm">Commencer</a>
            </div>
            {% endif %}
        </div>
    </div>

    <!-- Mes Tâches -->
    <div class="card">
        <div class="card-header">
            <span class="card-title"><i class="bi bi-clipboard-check"></i> Mes Tâches</span>
        </div>
        <div class="card-body" style="padding:0;">
            {% if my_tasks %}
                {% for task in my_tasks %}
                <div style="padding:.9rem 1.4rem; border-bottom:1px solid var(--beige);">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:.5rem;">
                        <span class="task-title" style="font-size:.88rem;">{{ task.title }}</span>
                        <span class="badge badge-{{ task.status }}">{{ task.get_status_display }}</span>
                    </div>
                    <div class="task-meta">
                        <span><i class="bi bi-folder2"></i> {{ task.project.name }}</span>
                        {% if task.due_date %}<span><i class="bi bi-calendar3"></i> {{ task.due_date|date:"d/m/Y" }}</span>{% endif %}
                    </div>
                </div>
                {% endfor %}
            {% else %}
            <div class="empty-state" style="padding:2.5rem;">
                <i class="bi bi-clipboard"></i>
                <h4>Aucune tâche</h4>
                <p>Aucune tâche assignée pour l'instant</p>
            </div>
            {% endif %}
        </div>
    </div>

</div>
{% endblock %}
🔄 Nouveau login.html
html
{% extends 'base.html' %}
{% block title %}Connexion{% endblock %}
{% block content %}
<div class="auth-wrapper">
    <div class="auth-card">
        <div class="auth-card-header">
            <div class="auth-logo">E</div>
            <h2>ESMT Tasks</h2>
            <p>Connectez-vous à votre espace</p>
        </div>
        <div class="auth-card-body">
            <form method="post">
                {% csrf_token %}
                <div class="form-group">
                    <label class="form-label">Nom d'utilisateur</label>
                    <input type="text" name="username" placeholder="Votre identifiant" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Mot de passe</label>
                    <input type="password" name="password" placeholder="••••••••" required>
                </div>
                <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;padding:.75rem;margin-top:.5rem;">
                    <i class="bi bi-box-arrow-in-right"></i> Se connecter
                </button>
            </form>
            <p style="text-align:center;margin-top:1.5rem;font-size:.875rem;color:var(--brown-pale);">
                Pas encore de compte ? <a href="{% url 'register' %}" class="auth-link">S'inscrire</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
🎨 Résumé de la palette
Élément	Couleur
Navbar & bouton principal	
#5c3d2e Marron foncé
Sidebar active	
#f2e8dc Beige
Fond de page	
#fdf9f5 Crème
Cartes	Blanc + bordure beige
Texte titres	Marron foncé + police Cormorant Garamond
Badges	Tons pastels chauds
Remplace tes 3 fichiers et rafraîchis le navigateur ! 🍂✨


TemplateSyntaxError à / 'block' tag with name 'content' appears more than once Méthode de demande : ALLEZ URL de demande : http://127.0.0.1:8000/ Version Django : 6.0.2 Type d’exception : TemplateSyntaxError Valeur d’exception : 'block' tag with name 'content' appears more than once Emplace

pasted

3 mars
L'erreur est claire ! Le problème est dans base.html — le tag {% block content %} apparaît deux fois. Voici comment corriger :

🔧 Le problème
Dans ton base.html, tu as ceci à la fin :

html
{% block content %}{% endblock %}  ← ligne 246 (dans le main)
...
{% else %}
{% block content %}{% endblock %}  ← ligne 251 (répété !)
{% endif %}
Django n'accepte pas deux fois le même nom de block.

✅ La correction
Remplace la fin de ton base.html (à partir du {% else %}) par ceci :

html
        {% block content %}{% endblock %}
    </main>
</div>

{% else %}
{% block auth_content %}{% endblock %}
{% endif %}

</body>
</html>
Et dans login.html et register.html, remplace :

html
{% block content %}
par :

html
{% block auth_content %}
🔄 Solution plus simple — Restructure la fin du base.html
En fait la meilleure solution est de supprimer complètement le {% if user.is_authenticated %} dans base.html et de tout mettre dans un seul block :

Remplace toute la partie finale de base.html par :

html
    <!-- CONTENU PRINCIPAL -->
    <main class="main-content">
        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i>
                {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        {% block content %}{% endblock %}
    </main>
</div>

</body>
</html>
Et dans login.html et register.html, enveloppe le contenu de la page avec la auth-wrapper directement dans {% block content %} — ce qui est déjà le cas ! ✅

📝 Version corrigée complète de la fin du base.html
Voici exactement ce que doit contenir la fin de ton fichier, à partir de la navbar :

html
{% if user.is_authenticated %}
<nav class="navbar">
    <a href="{% url 'dashboard' %}" class="navbar-brand">
        <div class="logo-icon">E</div>
        <span class="brand-text">ESMT <span>Tasks</span></span>
    </a>
    <div class="navbar-right">
        <a href="{% url 'profile' %}" class="user-chip">
            <div class="user-avatar">{{ user.username.0|upper }}</div>
            <span class="user-name">{{ user.username }}</span>
            <span class="role-badge {{ user.role }}">{{ user.get_role_display }}</span>
        </a>
        <a href="{% url 'logout' %}" class="nav-btn">
            <i class="bi bi-box-arrow-right"></i>
        </a>
    </div>
</nav>

<div class="app-layout">
    <aside class="sidebar">
        <span class="sidebar-section">Navigation</span>
        <a href="{% url 'dashboard' %}" class="sidebar-link {% if request.resolver_match.url_name == 'dashboard' %}active{% endif %}">
            <i class="bi bi-house-door"></i> Tableau de bord
        </a>
        <a href="{% url 'project_list' %}" class="sidebar-link {% if 'project' in request.resolver_match.url_name %}active{% endif %}">
            <i class="bi bi-folder2-open"></i> Projets
        </a>
        <a href="{% url 'statistics' %}" class="sidebar-link {% if 'statistics' in request.resolver_match.url_name %}active{% endif %}">
            <i class="bi bi-bar-chart-line"></i> Statistiques
        </a>
        <div class="sidebar-divider"></div>
        <span class="sidebar-section">Compte</span>
        <a href="{% url 'profile' %}" class="sidebar-link {% if request.resolver_match.url_name == 'profile' %}active{% endif %}">
            <i class="bi bi-person-circle"></i> Mon Profil
        </a>
        {% if user.is_staff %}
        <a href="/admin/" class="sidebar-link" target="_blank">
            <i class="bi bi-shield-lock"></i> Administration
        </a>
        {% endif %}
        <div class="sidebar-divider"></div>
        <a href="{% url 'logout' %}" class="sidebar-link" style="color:var(--red);">
            <i class="bi bi-box-arrow-right"></i> Déconnexion
        </a>
    </aside>

    <main class="main-content">
        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i>
                {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}
        {% block content %}{% endblock %}
    </main>
</div>

{% else %}
    {% block content %}{% endblock %}   ← ⚠️ PROBLÈME ICI
{% endif %}
Le {% block content %} est répété ! Voici la vraie correction — utilise {% block auth_content %} pour la partie non connectée :

html
{% else %}
    {% block auth_content %}{% endblock %}
{% endif %}

</body>
</html>
Et dans login.html et register.html :

html
{% block auth_content %}   ← remplace "content" par "auth_content"
...
{% endblock %}
Fais ce changement dans PyCharm et rafraîchis ! 😊


TemplateSyntaxError à / 'block' tag with name 'content' appears more than once Méthode de demande : ALLEZ URL de demande : http://127.0.0.1:8000/ Version Django : 6.0.2 Type d’exception : TemplateSyntaxError Valeur d’exception : 'block' tag with name 'content' appears more than once Emplace

pasted

3 mars
Le problème persiste ! C'est parce que tu as encore le double {% block content %}. Voici la solution définitive — remplace TOUT le contenu de base.html par exactement ce code, sans rien ajouter :

✅ base.html — Version finale corrigée
html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}ESMT Tasks{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        :root {
            --brown-dark: #5c3d2e; --brown: #7d5a4f; --brown-light: #a67c6d;
            --brown-pale: #c8a99a; --beige-dark: #e8d5c4; --beige: #f2e8dc;
            --beige-light: #f8f2eb; --cream: #fdf9f5; --white: #ffffff;
            --gray-400: #a8998f; --gray-600: #6b5c54; --gray-800: #3d2c26;
            --green: #5a8a6a; --red: #b85c5c; --blue: #5c7aa8;
            --sidebar-w: 265px; --navbar-h: 64px;
            --radius: 16px; --radius-sm: 10px;
            --shadow: 0 4px 24px rgba(92,61,46,.07);
            --shadow-lg: 0 8px 40px rgba(92,61,46,.13);
            --transition: all .22s cubic-bezier(.4,0,.2,1);
        }
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'DM Sans', sans-serif; background: var(--cream); color: var(--gray-800); min-height: 100vh; }

        .navbar { position: fixed; top: 0; left: 0; right: 0; height: var(--navbar-h); background: var(--brown-dark); display: flex; align-items: center; justify-content: space-between; padding: 0 2rem; z-index: 1000; box-shadow: 0 2px 20px rgba(92,61,46,.25); }
        .navbar-brand { display: flex; align-items: center; gap: .65rem; text-decoration: none; }
        .logo-icon { width: 38px; height: 38px; background: linear-gradient(135deg, var(--beige-dark), var(--beige)); border-radius: 11px; display: flex; align-items: center; justify-content: center; font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; font-weight: 700; color: var(--brown-dark); }
        .brand-text { font-family: 'Cormorant Garamond', serif; color: var(--beige-light); font-size: 1.35rem; font-weight: 600; }
        .brand-text span { color: var(--beige-dark); }
        .navbar-right { display: flex; align-items: center; gap: .75rem; }
        .user-chip { display: flex; align-items: center; gap: .5rem; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.15); border-radius: 50px; padding: .3rem .75rem .3rem .3rem; text-decoration: none; transition: var(--transition); }
        .user-chip:hover { background: rgba(255,255,255,.14); }
        .user-avatar { width: 32px; height: 32px; border-radius: 50%; background: linear-gradient(135deg, var(--beige-dark), var(--brown-pale)); display: flex; align-items: center; justify-content: center; font-size: .85rem; font-weight: 700; color: var(--brown-dark); }
        .user-name { color: var(--beige-light); font-size: .85rem; font-weight: 500; }
        .role-badge { font-size: .67rem; font-weight: 600; padding: .15rem .5rem; border-radius: 20px; text-transform: uppercase; letter-spacing: .05em; }
        .role-badge.professeur { background: rgba(200,169,154,.2); color: var(--beige-dark); border: 1px solid rgba(200,169,154,.3); }
        .role-badge.etudiant { background: rgba(92,122,168,.2); color: #a8c0e8; border: 1px solid rgba(92,122,168,.3); }
        .nav-btn { color: rgba(255,255,255,.6); text-decoration: none; padding: .4rem .65rem; border-radius: var(--radius-sm); transition: var(--transition); font-size: .95rem; }
        .nav-btn:hover { color: var(--beige-light); background: rgba(255,255,255,.08); }

        .app-layout { display: flex; padding-top: var(--navbar-h); min-height: 100vh; }

        .sidebar { width: var(--sidebar-w); background: var(--white); border-right: 1px solid var(--beige-dark); position: fixed; top: var(--navbar-h); bottom: 0; left: 0; overflow-y: auto; padding: 1.5rem .9rem; display: flex; flex-direction: column; gap: .2rem; }
        .sidebar-section { font-size: .68rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--brown-pale); padding: 1rem .75rem .35rem; }
        .sidebar-link { display: flex; align-items: center; gap: .7rem; padding: .65rem .85rem; border-radius: var(--radius-sm); color: var(--gray-600); text-decoration: none; font-size: .88rem; font-weight: 500; transition: var(--transition); position: relative; }
        .sidebar-link i { font-size: 1rem; width: 20px; text-align: center; color: var(--brown-pale); }
        .sidebar-link:hover { background: var(--beige-light); color: var(--brown-dark); }
        .sidebar-link.active { background: var(--beige); color: var(--brown-dark); font-weight: 600; }
        .sidebar-link.active::before { content: ''; position: absolute; left: 0; top: 18%; bottom: 18%; width: 3px; background: var(--brown); border-radius: 0 3px 3px 0; }
        .sidebar-divider { height: 1px; background: var(--beige-dark); margin: .6rem .5rem; }

        .main-content { margin-left: var(--sidebar-w); flex: 1; padding: 2.25rem 2.5rem; }

        .page-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 2rem; gap: 1rem; flex-wrap: wrap; }
        .page-subtitle { font-size: .82rem; color: var(--brown-pale); margin-bottom: .2rem; text-transform: uppercase; letter-spacing: .08em; font-weight: 600; }
        .page-title { font-family: 'Cormorant Garamond', serif; font-size: 2rem; color: var(--brown-dark); font-weight: 700; }
        .breadcrumb { display: flex; align-items: center; gap: .4rem; font-size: .78rem; color: var(--brown-pale); list-style: none; margin-bottom: .5rem; }
        .breadcrumb a { color: var(--brown-pale); text-decoration: none; }
        .breadcrumb a:hover { color: var(--brown-dark); }

        .card { background: var(--white); border-radius: var(--radius); box-shadow: var(--shadow); border: 1px solid var(--beige-dark); overflow: hidden; }
        .card-header { padding: 1.2rem 1.5rem; border-bottom: 1px solid var(--beige); display: flex; align-items: center; justify-content: space-between; }
        .card-title { font-family: 'Cormorant Garamond', serif; font-size: 1.15rem; color: var(--brown-dark); display: flex; align-items: center; gap: .5rem; font-weight: 600; }
        .card-body { padding: 1.5rem; }

        .stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-bottom: 2rem; }
        .stat-card { background: var(--white); border-radius: var(--radius); padding: 1.5rem; border: 1px solid var(--beige-dark); box-shadow: var(--shadow); position: relative; overflow: hidden; transition: var(--transition); }
        .stat-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }
        .stat-card::after { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; }
        .stat-card.c1::after { background: var(--brown-dark); }
        .stat-card.c2::after { background: var(--green); }
        .stat-card.c3::after { background: var(--blue); }
        .stat-card.c4::after { background: var(--brown-light); }
        .stat-icon { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin-bottom: .9rem; }
        .stat-icon.c1 { background: #ede0d4; color: var(--brown-dark); }
        .stat-icon.c2 { background: #d4ede0; color: var(--green); }
        .stat-icon.c3 { background: #d4dff0; color: var(--blue); }
        .stat-icon.c4 { background: #f0e4de; color: var(--brown-light); }
        .stat-value { font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700; color: var(--brown-dark); line-height: 1; margin-bottom: .25rem; }
        .stat-label { font-size: .8rem; color: var(--brown-pale); font-weight: 500; }

        .btn { display: inline-flex; align-items: center; gap: .45rem; padding: .55rem 1.15rem; border-radius: var(--radius-sm); font-size: .875rem; font-weight: 600; border: none; cursor: pointer; text-decoration: none; transition: var(--transition); font-family: 'DM Sans', sans-serif; }
        .btn-primary { background: var(--brown-dark); color: var(--beige-light); }
        .btn-primary:hover { background: var(--brown); transform: translateY(-1px); box-shadow: 0 4px 14px rgba(92,61,46,.3); }
        .btn-beige { background: var(--beige); color: var(--brown-dark); border: 1.5px solid var(--beige-dark); }
        .btn-beige:hover { background: var(--beige-dark); }
        .btn-outline { background: transparent; border: 1.5px solid var(--beige-dark); color: var(--gray-600); }
        .btn-outline:hover { border-color: var(--brown); color: var(--brown-dark); background: var(--beige-light); }
        .btn-danger { background: #f5e8e8; color: var(--red); border: 1.5px solid #e8c8c8; }
        .btn-danger:hover { background: var(--red); color: white; }
        .btn-sm { padding: .35rem .8rem; font-size: .8rem; }

        .form-group { margin-bottom: 1.25rem; }
        .form-label { display: block; font-size: .83rem; font-weight: 600; color: var(--brown-dark); margin-bottom: .4rem; }
        input[type=text], input[type=email], input[type=password], input[type=datetime-local], select, textarea, .form-control, .form-select { width: 100%; padding: .65rem .95rem; border: 1.5px solid var(--beige-dark); border-radius: var(--radius-sm); font-size: .9rem; font-family: 'DM Sans', sans-serif; color: var(--gray-800); background: var(--beige-light); transition: var(--transition); outline: none; }
        input:focus, select:focus, textarea:focus, .form-control:focus { border-color: var(--brown); background: var(--white); box-shadow: 0 0 0 3px rgba(92,61,46,.08); }
        textarea { resize: vertical; min-height: 90px; }
        .errorlist { color: var(--red); font-size: .78rem; list-style: none; margin-top: .3rem; }

        .badge { display: inline-flex; align-items: center; gap: .3rem; padding: .25rem .7rem; border-radius: 20px; font-size: .73rem; font-weight: 600; }
        .badge-a_faire { background: #f0ebe5; color: #7d6557; }
        .badge-en_cours { background: #dde8f5; color: #3a5f8a; }
        .badge-termine { background: #d8eddf; color: #2f6b45; }

        .project-card { background: var(--white); border-radius: var(--radius); border: 1.5px solid var(--beige-dark); overflow: hidden; transition: var(--transition); }
        .project-card:hover { box-shadow: var(--shadow-lg); transform: translateY(-3px); border-color: var(--brown-pale); }
        .project-name { font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; font-weight: 600; color: var(--brown-dark); text-decoration: none; display: block; margin-bottom: .25rem; }
        .project-name:hover { color: var(--brown-light); }
        .progress-wrap { height: 5px; background: var(--beige); border-radius: 10px; overflow: hidden; margin: .4rem 1.25rem .6rem; }
        .progress-fill { height: 100%; border-radius: 10px; background: linear-gradient(90deg, var(--brown-dark), var(--brown-light)); }
        .progress-fill.high { background: linear-gradient(90deg, var(--green), #8ac4a0); }

        .task-card { background: var(--white); border: 1.5px solid var(--beige-dark); border-radius: var(--radius); padding: 1.1rem 1.3rem; transition: var(--transition); margin-bottom: .75rem; }
        .task-card:hover { border-color: var(--brown-pale); box-shadow: 0 4px 16px rgba(92,61,46,.09); transform: translateY(-2px); }
        .task-card.overdue { border-left: 3px solid var(--red); }
        .task-title { font-weight: 600; color: var(--brown-dark); font-size: .93rem; margin-bottom: .35rem; }
        .task-meta { display: flex; align-items: center; gap: .75rem; flex-wrap: wrap; font-size: .77rem; color: var(--brown-pale); margin-top: .45rem; }

        .alert { padding: .85rem 1.1rem; border-radius: var(--radius-sm); font-size: .875rem; display: flex; align-items: center; gap: .6rem; margin-bottom: 1rem; animation: slideDown .3s ease; }
        @keyframes slideDown { from { opacity:0; transform:translateY(-8px); } to { opacity:1; transform:translateY(0); } }
        .alert-success { background: #e0f0e6; color: #2f6040; border: 1px solid #b8dcca; }
        .alert-error, .alert-danger { background: #f5e0e0; color: #8a2020; border: 1px solid #e0b8b8; }
        .alert-info { background: #e0eaf5; color: #2a4a78; border: 1px solid #b8cce0; }
        .alert-warning { background: #f5ecd8; color: #7a5010; border: 1px solid #e0cca8; }
        .alert-close { margin-left: auto; background: none; border: none; cursor: pointer; color: inherit; opacity: .6; font-size: 1rem; }

        .table-container { overflow-x: auto; border-radius: var(--radius); border: 1px solid var(--beige-dark); }
        table { width: 100%; border-collapse: collapse; font-size: .875rem; }
        thead th { background: var(--brown-dark); color: rgba(255,255,255,.85); font-weight: 600; padding: .9rem 1.1rem; text-align: left; font-size: .78rem; text-transform: uppercase; letter-spacing: .05em; }
        tbody tr { border-bottom: 1px solid var(--beige); transition: var(--transition); }
        tbody tr:hover { background: var(--beige-light); }
        tbody td { padding: .9rem 1.1rem; }

        .filter-bar { display: flex; align-items: center; gap: .75rem; padding: .9rem 1.25rem; background: var(--white); border-radius: var(--radius); border: 1px solid var(--beige-dark); margin-bottom: 1.5rem; flex-wrap: wrap; }
        .filter-label { font-size: .75rem; font-weight: 700; color: var(--brown-pale); text-transform: uppercase; letter-spacing: .08em; }
        .filter-select { padding: .4rem .8rem; border: 1.5px solid var(--beige-dark); border-radius: 8px; font-size: .84rem; font-family: 'DM Sans', sans-serif; color: var(--brown-dark); background: var(--beige-light); outline: none; width: auto; }

        .empty-state { text-align: center; padding: 4rem 2rem; color: var(--brown-pale); }
        .empty-state i { font-size: 3rem; display: block; margin-bottom: 1rem; opacity: .35; }
        .empty-state h4 { color: var(--brown); margin-bottom: .5rem; font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; }
        .empty-state p { font-size: .875rem; margin-bottom: 1.5rem; }

        .auth-wrapper { min-height: 100vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(150deg, var(--brown-dark) 0%, var(--brown) 50%, var(--brown-light) 100%); position: relative; overflow: hidden; padding: 2rem; }
        .auth-wrapper::before { content: ''; position: absolute; width: 600px; height: 600px; border-radius: 50%; background: rgba(248,242,235,.05); top: -200px; right: -150px; }
        .auth-card { background: var(--white); border-radius: 22px; width: 100%; max-width: 440px; box-shadow: 0 30px 70px rgba(0,0,0,.25); overflow: hidden; position: relative; z-index: 1; }
        .auth-card-header { background: linear-gradient(135deg, var(--brown-dark), var(--brown)); padding: 2.25rem 2rem; text-align: center; }
        .auth-logo { width: 58px; height: 58px; background: linear-gradient(135deg, var(--beige-dark), var(--beige-light)); border-radius: 18px; display: flex; align-items: center; justify-content: center; font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; font-weight: 700; color: var(--brown-dark); margin: 0 auto 1rem; }
        .auth-card-header h2 { font-family: 'Cormorant Garamond', serif; color: var(--beige-light); font-size: 1.65rem; margin-bottom: .3rem; font-weight: 600; }
        .auth-card-header p { color: rgba(255,255,255,.55); font-size: .85rem; }
        .auth-card-body { padding: 2rem; }
        .auth-link { color: var(--brown-dark); font-weight: 600; text-decoration: none; }
        .auth-link:hover { color: var(--brown-light); }

        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: var(--beige-light); }
        ::-webkit-scrollbar-thumb { background: var(--beige-dark); border-radius: 3px; }

        @media (max-width: 768px) {
            .sidebar { display: none; }
            .main-content { margin-left: 0; padding: 1.25rem; }
            .stat-grid { grid-template-columns: repeat(2, 1fr); }
            .page-header { flex-direction: column; }
        }
    </style>
</head>
<body>

{% block content %}{% endblock %}

</body>
</html>
⚠️ Changement important dans dashboard.html
Maintenant que base.html n'a plus la navbar/sidebar intégrée, tu dois les mettre dans dashboard.html. Voici le nouveau dashboard.html complet :

html
{% extends 'base.html' %}
{% block title %}Tableau de bord{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">

        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i> {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        <div class="page-header">
            <div>
                <p class="page-subtitle">Bienvenue de retour</p>
                <h1 class="page-title">{{ user.first_name|default:user.username }} 👋</h1>
            </div>
            <a href="{% url 'project_create' %}" class="btn btn-primary">
                <i class="bi bi-plus-lg"></i> Nouveau projet
            </a>
        </div>

        <div class="stat-grid">
            <div class="stat-card c1">
                <div class="stat-icon c1"><i class="bi bi-list-check"></i></div>
                <div class="stat-value">{{ total_tasks }}</div>
                <div class="stat-label">Tâches totales</div>
            </div>
            <div class="stat-card c2">
                <div class="stat-icon c2"><i class="bi bi-check-circle"></i></div>
                <div class="stat-value">{{ done_tasks }}</div>
                <div class="stat-label">Terminées</div>
            </div>
            <div class="stat-card c3">
                <div class="stat-icon c3"><i class="bi bi-arrow-repeat"></i></div>
                <div class="stat-value">{{ in_progress }}</div>
                <div class="stat-label">En cours</div>
            </div>
            <div class="stat-card c4">
                <div class="stat-icon c4"><i class="bi bi-graph-up"></i></div>
                <div class="stat-value">{{ completion_rate }}%</div>
                <div class="stat-label">Taux de complétion</div>
            </div>
        </div>

        {% if overdue_count > 0 %}
        <div class="alert alert-danger">
            <i class="bi bi-exclamation-triangle-fill"></i>
            <strong>{{ overdue_count }} tâche(s) en retard !</strong>
        </div>
        {% endif %}

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
            <div class="card">
                <div class="card-header">
                    <span class="card-title"><i class="bi bi-folder2-open"></i> Mes Projets</span>
                    <a href="{% url 'project_list' %}" class="btn btn-outline btn-sm">Voir tout</a>
                </div>
                <div class="card-body" style="padding:0;">
                    {% if created_projects %}
                        {% for project in created_projects %}
                        <div style="padding:.9rem 1.4rem; border-bottom:1px solid var(--beige); display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <a href="{% url 'project_detail' project.pk %}" class="project-name" style="font-size:.9rem;">{{ project.name }}</a>
                                <div style="font-size:.77rem; color:var(--brown-pale);">{{ project.tasks.count }} tâche(s)</div>
                            </div>
                            <span style="font-size:.82rem; font-weight:700; color:var(--brown-dark);">{{ project.get_completion_rate }}%</span>
                        </div>
                        {% endfor %}
                    {% else %}
                    <div class="empty-state" style="padding:2.5rem;">
                        <i class="bi bi-folder-plus"></i>
                        <h4>Aucun projet</h4>
                        <p>Créez votre premier projet</p>
                        <a href="{% url 'project_create' %}" class="btn btn-primary btn-sm">Commencer</a>
                    </div>
                    {% endif %}
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <span class="card-title"><i class="bi bi-clipboard-check"></i> Mes Tâches</span>
                </div>
                <div class="card-body" style="padding:0;">
                    {% if my_tasks %}
                        {% for task in my_tasks %}
                        <div style="padding:.9rem 1.4rem; border-bottom:1px solid var(--beige);">
                            <div style="display:flex; justify-content:space-between; gap:.5rem;">
                                <span class="task-title" style="font-size:.88rem;">{{ task.title }}</span>
                                <span class="badge badge-{{ task.status }}">{{ task.get_status_display }}</span>
                            </div>
                            <div class="task-meta">
                                <span><i class="bi bi-folder2"></i> {{ task.project.name }}</span>
                                {% if task.due_date %}<span><i class="bi bi-calendar3"></i> {{ task.due_date|date:"d/m/Y" }}</span>{% endif %}
                            </div>
                        </div>
                        {% endfor %}
                    {% else %}
                    <div class="empty-state" style="padding:2.5rem;">
                        <i class="bi bi-clipboard"></i>
                        <h4>Aucune tâche</h4>
                        <p>Aucune tâche assignée pour l'instant</p>
                    </div>
                    {% endif %}
                </div>
            </div>
        </div>

    </main>
</div>

{% endblock %}
📁 Crée aussi templates/partials/navbar.html
Dans PyCharm, crée le dossier templates/partials/ puis le fichier navbar.html :

html
<nav class="navbar">
    <a href="{% url 'dashboard' %}" class="navbar-brand">
        <div class="logo-icon">E</div>
        <span class="brand-text">ESMT <span>Tasks</span></span>
    </a>
    <div class="navbar-right">
        <a href="{% url 'profile' %}" class="user-chip">
            <div class="user-avatar">{{ user.username.0|upper }}</div>
            <span class="user-name">{{ user.username }}</span>
            <span class="role-badge {{ user.role }}">{{ user.get_role_display }}</span>
        </a>
        <a href="{% url 'logout' %}" class="nav-btn"><i class="bi bi-box-arrow-right"></i></a>
    </div>
</nav>
📁 Crée templates/partials/sidebar.html
html
<aside class="sidebar">
    <span class="sidebar-section">Navigation</span>
    <a href="{% url 'dashboard' %}" class="sidebar-link {% if request.resolver_match.url_name == 'dashboard' %}active{% endif %}">
        <i class="bi bi-house-door"></i> Tableau de bord
    </a>
    <a href="{% url 'project_list' %}" class="sidebar-link {% if 'project' in request.resolver_match.url_name %}active{% endif %}">
        <i class="bi bi-folder2-open"></i> Projets
    </a>
    <a href="{% url 'statistics' %}" class="sidebar-link {% if 'statistics' in request.resolver_match.url_name %}active{% endif %}">
        <i class="bi bi-bar-chart-line"></i> Statistiques
    </a>
    <div class="sidebar-divider"></div>
    <span class="sidebar-section">Compte</span>
    <a href="{% url 'profile' %}" class="sidebar-link {% if request.resolver_match.url_name == 'profile' %}active{% endif %}">
        <i class="bi bi-person-circle"></i> Mon Profil
    </a>
    {% if user.is_staff %}
    <a href="/admin/" class="sidebar-link" target="_blank">
        <i class="bi bi-shield-lock"></i> Administration
    </a>
    {% endif %}
    <div class="sidebar-divider"></div>
    <a href="{% url 'logout' %}" class="sidebar-link" style="color:var(--red);">
        <i class="bi bi-box-arrow-right"></i> Déconnexion
    </a>
</aside>
```

---

## 📋 Résumé des fichiers à modifier/créer
```
templates/
  base.html              ← remplacer tout le contenu
  dashboard.html         ← remplacer tout le contenu
  partials/
    navbar.html          ← nouveau fichier à créer
    sidebar.html         ← nouveau fichier à créer
Chaque page (projets, profil, etc.) devra aussi inclure {% include 'partials/navbar.html' %} et {% include 'partials/sidebar.html' %} dans son {% block content %}. Dis-moi quand c'est fait ! 😊

Chaque page (projets, profil, etc.) devra aussi inclure {% include 'partials/navbar.html' %} et {% include 'partials/sidebar.html' %} dans son {% block content %}. Dis-moi quand c'est fait ! 😊 comment

3 mars
Voici exactement comment faire pour chaque page ! C'est simple, tu ajoutes juste 3 lignes au début de chaque fichier.

📌 La structure à suivre pour CHAQUE page
html
{% extends 'base.html' %}
{% block title %}Titre de la page{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}    ← ligne 1 à ajouter

<div class="app-layout">
    {% include 'partials/sidebar.html' %}    ← ligne 2 à ajouter
    <main class="main-content">

        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i> {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        <!-- LE CONTENU DE LA PAGE ICI -->

    </main>
</div>

{% endblock %}
📄 Voici TOUS les fichiers corrigés
templates/users/profile.html
html
{% extends 'base.html' %}
{% block title %}Mon Profil{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">

        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i> {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        <div class="page-header">
            <div>
                <p class="page-subtitle">Paramètres</p>
                <h1 class="page-title">Mon Profil</h1>
            </div>
        </div>

        <div style="display:grid; grid-template-columns:300px 1fr; gap:1.5rem;">

            <!-- Carte profil gauche -->
            <div class="card" style="align-self:start;">
                <div class="card-body" style="text-align:center; padding:2rem;">
                    {% if user.avatar %}
                    <img src="{{ user.avatar.url }}" style="width:90px;height:90px;border-radius:50%;object-fit:cover;border:3px solid var(--beige-dark);">
                    {% else %}
                    <div style="width:90px;height:90px;border-radius:50%;background:linear-gradient(135deg,var(--beige-dark),var(--brown-pale));display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:2.5rem;font-weight:700;color:var(--brown-dark);margin:0 auto;">
                        {{ user.username.0|upper }}
                    </div>
                    {% endif %}
                    <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:var(--brown-dark);margin-top:1rem;">
                        {{ user.get_full_name|default:user.username }}
                    </h4>
                    <span class="role-badge {{ user.role }}" style="margin-top:.3rem;display:inline-block;">
                        {{ user.get_role_display }}
                    </span>
                    <p style="font-size:.85rem;color:var(--brown-pale);margin-top:.5rem;">{{ user.email }}</p>
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.5rem;padding-top:1.5rem;border-top:1px solid var(--beige);">
                        <div>
                            <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;font-weight:700;color:var(--brown-dark);">{{ user.created_projects.count }}</div>
                            <div style="font-size:.75rem;color:var(--brown-pale);">Projets</div>
                        </div>
                        <div>
                            <div style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;font-weight:700;color:var(--brown-dark);">{{ user.assigned_tasks.count }}</div>
                            <div style="font-size:.75rem;color:var(--brown-pale);">Tâches</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Formulaire droite -->
            <div class="card">
                <div class="card-header">
                    <span class="card-title"><i class="bi bi-pencil-square"></i> Modifier mes informations</span>
                </div>
                <div class="card-body">
                    <form method="post" enctype="multipart/form-data">
                        {% csrf_token %}
                        {% for field in form %}
                        <div class="form-group">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}
                            <div class="errorlist">{{ field.errors|join:", " }}</div>
                            {% endif %}
                        </div>
                        {% endfor %}
                        <button type="submit" class="btn btn-primary">
                            <i class="bi bi-save"></i> Sauvegarder
                        </button>
                    </form>
                </div>
            </div>

        </div>
    </main>
</div>

{% endblock %}
templates/projects/list.html
html
{% extends 'base.html' %}
{% block title %}Projets{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">

        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i> {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        <div class="page-header">
            <div>
                <p class="page-subtitle">Gestion</p>
                <h1 class="page-title">Mes Projets</h1>
            </div>
            <a href="{% url 'project_create' %}" class="btn btn-primary">
                <i class="bi bi-plus-lg"></i> Nouveau projet
            </a>
        </div>

        {% if my_projects %}
        <p style="font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--brown-pale);margin-bottom:1rem;">
            Projets créés par moi
        </p>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.25rem;margin-bottom:2rem;">
            {% for project in my_projects %}
            <div class="project-card">
                <div style="padding:1.25rem 1.25rem .75rem;">
                    <a href="{% url 'project_detail' project.pk %}" class="project-name">{{ project.name }}</a>
                    <p style="font-size:.82rem;color:var(--brown-pale);line-height:1.5;">{{ project.description|truncatewords:12 }}</p>
                </div>
                <div class="progress-wrap">
                    <div class="progress-fill {% if project.get_completion_rate >= 80 %}high{% endif %}" style="width:{{ project.get_completion_rate }}%"></div>
                </div>
                <div style="display:flex;gap:1rem;padding:.7rem 1.25rem;border-top:1px solid var(--beige);font-size:.79rem;color:var(--gray-600);">
                    <span><i class="bi bi-people"></i> {{ project.members.count }} membre(s)</span>
                    <span><i class="bi bi-list-check"></i> {{ project.tasks.count }} tâche(s)</span>
                    <span style="margin-left:auto;font-weight:700;color:var(--brown-dark);">{{ project.get_completion_rate }}%</span>
                </div>
                <div style="padding:.75rem 1.25rem;border-top:1px solid var(--beige);display:flex;gap:.5rem;background:var(--beige-light);">
                    <a href="{% url 'project_detail' project.pk %}" class="btn btn-primary btn-sm">Voir</a>
                    <a href="{% url 'project_edit' project.pk %}" class="btn btn-outline btn-sm">Modifier</a>
                    <a href="{% url 'project_delete' project.pk %}" class="btn btn-danger btn-sm">
                        <i class="bi bi-trash"></i>
                    </a>
                </div>
            </div>
            {% endfor %}
        </div>
        {% endif %}

        {% if member_projects %}
        <p style="font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--brown-pale);margin-bottom:1rem;">
            Projets auxquels je participe
        </p>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.25rem;">
            {% for project in member_projects %}
            <div class="project-card" style="border-color:var(--blue);border-top:3px solid var(--blue);">
                <div style="padding:1.25rem;">
                    <a href="{% url 'project_detail' project.pk %}" class="project-name">{{ project.name }}</a>
                    <p style="font-size:.8rem;color:var(--brown-pale);margin-top:.25rem;">
                        <i class="bi bi-person"></i> {{ project.created_by.username }}
                    </p>
                </div>
                <div style="padding:.75rem 1.25rem;border-top:1px solid var(--beige);background:var(--beige-light);">
                    <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline btn-sm" style="width:100%;justify-content:center;">Voir le projet</a>
                </div>
            </div>
            {% endfor %}
        </div>
        {% endif %}

        {% if not my_projects and not member_projects %}
        <div class="empty-state">
            <i class="bi bi-folder-plus"></i>
            <h4>Aucun projet pour le moment</h4>
            <p>Créez votre premier projet pour commencer</p>
            <a href="{% url 'project_create' %}" class="btn btn-primary">
                <i class="bi bi-plus"></i> Créer un projet
            </a>
        </div>
        {% endif %}

    </main>
</div>

{% endblock %}
templates/projects/form.html
html
{% extends 'base.html' %}
{% block title %}{{ action }} un projet{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">

        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i> {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        <div class="breadcrumb">
            <a href="{% url 'project_list' %}">Projets</a>
            <span>›</span>
            <span>{{ action }}</span>
        </div>

        <div style="max-width:600px;">
            <div class="page-header">
                <div>
                    <p class="page-subtitle">Formulaire</p>
                    <h1 class="page-title">{{ action }} un projet</h1>
                </div>
            </div>

            <div class="card">
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        {% for field in form %}
                        <div class="form-group">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}
                            <div class="errorlist">{{ field.errors|join:", " }}</div>
                            {% endif %}
                        </div>
                        {% endfor %}
                        <div style="display:flex;gap:.75rem;margin-top:1.5rem;">
                            <button type="submit" class="btn btn-primary">
                                <i class="bi bi-save"></i> {{ action }}
                            </button>
                            <a href="{% url 'project_list' %}" class="btn btn-outline">Annuler</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>

    </main>
</div>

{% endblock %}
templates/projects/detail.html
html
{% extends 'base.html' %}
{% block title %}{{ project.name }}{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">

        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i> {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        <div class="breadcrumb">
            <a href="{% url 'project_list' %}">Projets</a>
            <span>›</span>
            <span>{{ project.name }}</span>
        </div>

        <div class="page-header">
            <div>
                <p class="page-subtitle">Projet</p>
                <h1 class="page-title">{{ project.name }}</h1>
                {% if project.description %}
                <p style="color:var(--brown-pale);margin-top:.3rem;">{{ project.description }}</p>
                {% endif %}
            </div>
            {% if is_creator %}
            <div style="display:flex;gap:.5rem;">
                <a href="{% url 'task_create' project.pk %}" class="btn btn-primary">
                    <i class="bi bi-plus"></i> Ajouter tâche
                </a>
                <a href="{% url 'project_edit' project.pk %}" class="btn btn-outline">
                    <i class="bi bi-pencil"></i>
                </a>
            </div>
            {% endif %}
        </div>

        <!-- Filtres -->
        <div class="filter-bar">
            <span class="filter-label">Filtrer :</span>
            <form method="get" style="display:flex;gap:.75rem;align-items:center;">
                <select name="status" class="filter-select" onchange="this.form.submit()">
                    <option value="">Tous les statuts</option>
                    <option value="a_faire" {% if status_filter == 'a_faire' %}selected{% endif %}>À faire</option>
                    <option value="en_cours" {% if status_filter == 'en_cours' %}selected{% endif %}>En cours</option>
                    <option value="termine" {% if status_filter == 'termine' %}selected{% endif %}>Terminé</option>
                </select>
                <select name="user" class="filter-select" onchange="this.form.submit()">
                    <option value="">Tous les membres</option>
                    {% for member in members %}
                    <option value="{{ member.id }}" {% if user_filter == member.id|stringformat:"s" %}selected{% endif %}>
                        {{ member.username }}
                    </option>
                    {% endfor %}
                </select>
                {% if status_filter or user_filter %}
                <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline btn-sm">✕ Effacer</a>
                {% endif %}
            </form>
        </div>

        <!-- Tâches -->
        {% if tasks %}
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;">
            {% for task in tasks %}
            <div class="task-card {% if task.is_overdue %}overdue{% endif %}">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem;">
                    <span class="task-title">{{ task.title }}</span>
                    <span class="badge badge-{{ task.status }}">{{ task.get_status_display }}</span>
                </div>
                {% if task.description %}
                <p style="font-size:.82rem;color:var(--brown-pale);margin:.3rem 0;line-height:1.4;">{{ task.description|truncatewords:10 }}</p>
                {% endif %}
                <div class="task-meta">
                    {% if task.assigned_to %}
                    <span><i class="bi bi-person"></i> {{ task.assigned_to.username }}</span>
                    {% endif %}
                    {% if task.due_date %}
                    <span class="{% if task.is_overdue %}text-danger{% endif %}">
                        <i class="bi bi-calendar3"></i> {{ task.due_date|date:"d/m/Y" }}
                        {% if task.is_overdue %} ⚠️{% endif %}
                    </span>
                    {% endif %}
                </div>
                {% if is_creator or task.assigned_to == request.user %}
                <div style="display:flex;gap:.5rem;margin-top:.75rem;padding-top:.75rem;border-top:1px solid var(--beige);">
                    <a href="{% url 'task_update' task.pk %}" class="btn btn-outline btn-sm">
                        <i class="bi bi-pencil"></i> Modifier
                    </a>
                    {% if is_creator %}
                    <a href="{% url 'task_delete' task.pk %}" class="btn btn-danger btn-sm"
                       onclick="return confirm('Supprimer cette tâche ?')">
                        <i class="bi bi-trash"></i>
                    </a>
                    {% endif %}
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty-state">
            <i class="bi bi-clipboard"></i>
            <h4>Aucune tâche</h4>
            <p>Ce projet n'a pas encore de tâches</p>
            {% if is_creator %}
            <a href="{% url 'task_create' project.pk %}" class="btn btn-primary">
                <i class="bi bi-plus"></i> Créer une tâche
            </a>
            {% endif %}
        </div>
        {% endif %}

    </main>
</div>

{% endblock %}
templates/projects/confirm_delete.html
html
{% extends 'base.html' %}
{% block title %}Supprimer{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">
        <div style="max-width:480px;margin:3rem auto;">
            <div class="card" style="border-top:3px solid var(--red);">
                <div class="card-body" style="text-align:center;padding:2.5rem;">
                    <i class="bi bi-exclamation-triangle" style="font-size:3rem;color:var(--red);opacity:.7;display:block;margin-bottom:1rem;"></i>
                    <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;color:var(--brown-dark);margin-bottom:.75rem;">
                        Supprimer ce projet ?
                    </h3>
                    <p style="color:var(--brown-pale);margin-bottom:.5rem;">
                        Vous allez supprimer <strong style="color:var(--brown-dark);">{{ project.name }}</strong>
                    </p>
                    <p style="color:var(--red);font-size:.85rem;margin-bottom:2rem;">
                        ⚠️ Cette action supprimera aussi toutes les tâches associées !
                    </p>
                    <form method="post" style="display:flex;gap:.75rem;justify-content:center;">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-danger">
                            <i class="bi bi-trash"></i> Oui, supprimer
                        </button>
                        <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline">Annuler</a>
                    </form>
                </div>
            </div>
        </div>
    </main>
</div>

{% endblock %}
templates/tasks/form.html
html
{% extends 'base.html' %}
{% block title %}{{ action }} une tâche{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">

        <div class="breadcrumb">
            <a href="{% url 'project_list' %}">Projets</a>
            <span>›</span>
            <a href="{% url 'project_detail' project.pk %}">{{ project.name }}</a>
            <span>›</span>
            <span>{{ action }} tâche</span>
        </div>

        <div style="max-width:600px;">
            <div class="page-header">
                <div>
                    <p class="page-subtitle">Formulaire</p>
                    <h1 class="page-title">{{ action }} une tâche</h1>
                </div>
            </div>

            <div class="card">
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        {% for field in form %}
                        <div class="form-group">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}
                            <div class="errorlist">{{ field.errors|join:", " }}</div>
                            {% endif %}
                        </div>
                        {% endfor %}
                        <div style="display:flex;gap:.75rem;margin-top:1.5rem;">
                            <button type="submit" class="btn btn-primary">
                                <i class="bi bi-save"></i> {{ action }}
                            </button>
                            <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline">Annuler</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>

    </main>
</div>

{% endblock %}
templates/tasks/statistics.html
html
{% extends 'base.html' %}
{% block title %}Statistiques{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">

        <div class="page-header">
            <div>
                <p class="page-subtitle">Analyse</p>
                <h1 class="page-title">Statistiques & Primes</h1>
            </div>
        </div>

        <!-- Stats trimestrielles -->
        <div class="card" style="margin-bottom:1.5rem;">
            <div class="card-header">
                <span class="card-title"><i class="bi bi-calendar3"></i> Mes statistiques {{ year }}</span>
            </div>
            <div class="card-body">
                <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;">
                    {% for q in quarterly_stats %}
                    <div style="text-align:center;padding:1.25rem;border-radius:var(--radius);border:1.5px solid {% if q.rate == 100 %}var(--green){% elif q.rate >= 90 %}var(--brown-light){% else %}var(--beige-dark){% endif %};">
                        <div style="font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--brown-pale);margin-bottom:.5rem;">{{ q.quarter }}</div>
                        <div style="font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:700;color:{% if q.rate == 100 %}var(--green){% elif q.rate >= 90 %}var(--brown){% else %}var(--brown-pale){% endif %};">{{ q.rate }}%</div>
                        <div style="font-size:.78rem;color:var(--brown-pale);margin:.3rem 0;">{{ q.on_time }}/{{ q.total }} dans les délais</div>
                        {% if q.rate == 100 %}
                        <span style="display:inline-block;background:#d8eddf;color:#2f6b45;padding:.2rem .6rem;border-radius:20px;font-size:.72rem;font-weight:600;">🏆 100 000 FCFA</span>
                        {% elif q.rate >= 90 %}
                        <span style="display:inline-block;background:#f5ecd8;color:#7a5010;padding:.2rem .6rem;border-radius:20px;font-size:.72rem;font-weight:600;">⭐ 30 000 FCFA</span>
                        {% else %}
                        <span style="display:inline-block;background:var(--beige);color:var(--brown-pale);padding:.2rem .6rem;border-radius:20px;font-size:.72rem;font-weight:600;">Pas de prime</span>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>

        <!-- Tableau des primes professeurs -->
        {% if evaluations %}
        <div class="card">
            <div class="card-header">
                <span class="card-title"><i class="bi bi-award"></i> Évaluations Professeurs — {{ year }}</span>
            </div>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Professeur</th>
                            <th>Tâches</th>
                            <th>Dans les délais</th>
                            <th>Taux</th>
                            <th>Prime</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for eval in evaluations %}
                        <tr>
                            <td>
                                <strong>{{ eval.user.get_full_name|default:eval.user.username }}</strong>
                                <div style="font-size:.78rem;color:var(--brown-pale);">{{ eval.user.email }}</div>
                            </td>
                            <td>{{ eval.total }}</td>
                            <td>{{ eval.on_time }}</td>
                            <td>
                                <div style="height:8px;background:var(--beige);border-radius:10px;overflow:hidden;min-width:80px;">
                                    <div style="height:100%;border-radius:10px;width:{{ eval.rate }}%;background:{% if eval.rate == 100 %}var(--green){% elif eval.rate >= 90 %}var(--brown-light){% else %}var(--red){% endif %};"></div>
                                </div>
                                <span style="font-size:.8rem;font-weight:600;color:var(--brown-dark);">{{ eval.rate }}%</span>
                            </td>
                            <td>
                                {% if eval.prime == 100000 %}
                                <span style="background:#d8eddf;color:#2f6b45;padding:.3rem .75rem;border-radius:20px;font-size:.8rem;font-weight:700;">🏆 100 000 FCFA</span>
                                {% elif eval.prime == 30000 %}
                                <span style="background:#f5ecd8;color:#7a5010;padding:.3rem .75rem;border-radius:20px;font-size:.8rem;font-weight:700;">⭐ 30 000 FCFA</span>
                                {% else %}
                                <span style="background:var(--beige);color:var(--brown-pale);padding:.3rem .75rem;border-radius:20px;font-size:.8rem;">—</span>
                                {% endif %}
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        {% endif %}

    </main>
</div>

{% endblock %}
templates/users/login.html
html
{% extends 'base.html' %}
{% block title %}Connexion{% endblock %}
{% block content %}

<div class="auth-wrapper">
    <div class="auth-card">
        <div class="auth-card-header">
            <div class="auth-logo">E</div>
            <h2>ESMT Tasks</h2>
            <p>Connectez-vous à votre espace</p>
        </div>
        <div class="auth-card-body">
            {% if messages %}
                {% for message in messages %}
                <div class="alert alert-{{ message.tags|default:'info' }}" style="margin-bottom:1rem;">
                    {{ message }}
                </div>
                {% endfor %}
            {% endif %}
            <form method="post">
                {% csrf_token %}
                <div class="form-group">
                    <label class="form-label">Nom d'utilisateur</label>
                    <input type="text" name="username" placeholder="Votre identifiant" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Mot de passe</label>
                    <input type="password" name="password" placeholder="••••••••" required>
                </div>
                <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;padding:.75rem;margin-top:.5rem;">
                    <i class="bi bi-box-arrow-in-right"></i> Se connecter
                </button>
            </form>
            <p style="text-align:center;margin-top:1.5rem;font-size:.875rem;color:var(--brown-pale);">
                Pas encore de compte ? <a href="{% url 'register' %}" class="auth-link">S'inscrire</a>
            </p>
        </div>
    </div>
</div>

{% endblock %}
templates/users/register.html
html
{% extends 'base.html' %}
{% block title %}Inscription{% endblock %}
{% block content %}

<div class="auth-wrapper">
    <div class="auth-card">
        <div class="auth-card-header">
            <div class="auth-logo">E</div>
            <h2>Créer un compte</h2>
            <p>Rejoignez la plateforme ESMT</p>
        </div>
        <div class="auth-card-body">
            <form method="post">
                {% csrf_token %}
                {% for field in form %}
                <div class="form-group">
                    <label class="form-label">{{ field.label }}</label>
                    {{ field }}
                    {% if field.errors %}
                    <div class="errorlist">{{ field.errors|join:", " }}</div>
                    {% endif %}
                </div>
                {% endfor %}
                <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;padding:.75rem;margin-top:.5rem;">
                    <i class="bi bi-check-circle"></i> Créer mon compte
                </button>
            </form>
            <p style="text-align:center;margin-top:1.5rem;font-size:.875rem;color:var(--brown-pale);">
                Déjà un compte ? <a href="{% url 'login' %}" class="auth-link">Se connecter</a>
            </p>
        </div>
    </div>
</div>

{% endblock %}
```

---

## 📋 Résumé — fichiers à modifier
```
templates/
  base.html                     ✅ déjà fait
  dashboard.html                ✅ déjà fait
  partials/
    navbar.html                 ✅ déjà fait
    sidebar.html                ✅ déjà fait
  users/
    login.html                  ← copier-coller
    register.html               ← copier-coller
    profile.html                ← copier-coller
  projects/
    list.html                   ← copier-coller
    detail.html                 ← copier-coller
    form.html                   ← copier-coller
    confirm_delete.html         ← copier-coller
  tasks/
    form.html                   ← copier-coller
    statistics.html             ← copier-coller
Copie chaque fichier dans PyCharm et dis-moi quand c'est fait ! 😊


TemplateDoesNotExist at / base.html Request Method: GET Request URL: http://127.0.0.1:8000/ Django Version: 6.0.2 Exception Type: TemplateDoesNotExist Exception Value: base.html Exception Location: C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\templat

pasted

3 mars
Je vois le problème ! L'erreur dit "Skipped to avoid recursion" — c'est parce que base.html contient lui-même {% extends 'base.html' %} !

🔍 Le problème
Regarde cette ligne dans l'erreur :

django.template.loaders.filesystem.Loader: 
...templates\base.html (Skipped to avoid recursion)
Ton base.html commence par {% extends 'base.html' %} — c'est impossible, un fichier ne peut pas s'étendre lui-même !

✅ Solution
Ouvre templates/base.html dans PyCharm et vérifie la toute première ligne.

Elle doit commencer par <!DOCTYPE html> et PAS par {% extends 'base.html' %}.

Si tu vois {% extends 'base.html' %} en ligne 1 → supprime cette ligne immédiatement.

🔄 Le bon contenu de base.html — première ligne
html
<!DOCTYPE html>       ← doit commencer par ça
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}ESMT Tasks{% endblock %}</title>
    ...
```

---

## 💡 Ce qui s'est passé

Tu as probablement copié le contenu de `dashboard.html` dans `base.html` par erreur. Le fichier `dashboard.html` commence par `{% extends 'base.html' %}` mais `base.html` lui ne doit pas avoir cette ligne.

---

## 📋 Rappel des rôles
```
base.html       → PAS de {% extends %}, commence par <!DOCTYPE html>
dashboard.html  → commence par {% extends 'base.html' %}
login.html      → commence par {% extends 'base.html' %}
etc.
Ouvre base.html, supprime la première ligne si elle contient {% extends %}, sauvegarde et rafraîchis ! 😊


TemplateSyntaxError at / Invalid block tag on line 119: 'endblock'. Did you forget to register or load this tag? Request Method: GET Request URL: http://127.0.0.1:8000/ Django Version: 6.0.2 Exception Type: TemplateSyntaxError Exception Value: Invalid block tag on line 119: 'endblock'. Did y

pasted

3 mars
L'erreur dit que base.html a un {% endblock %} sans {% block %} correspondant. Le problème est que le contenu de dashboard.html a été collé dans base.html !

🔧 Solution simple et définitive
Voici exactement ce que tu dois faire :

1️⃣ Ouvre base.html dans PyCharm
Fais Ctrl+A pour tout sélectionner puis Delete pour tout effacer.

2️⃣ Colle EXACTEMENT ce contenu :
html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}ESMT Tasks{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        :root {
            --brown-dark:#5c3d2e; --brown:#7d5a4f; --brown-light:#a67c6d;
            --brown-pale:#c8a99a; --beige-dark:#e8d5c4; --beige:#f2e8dc;
            --beige-light:#f8f2eb; --cream:#fdf9f5; --white:#ffffff;
            --gray-400:#a8998f; --gray-600:#6b5c54; --gray-800:#3d2c26;
            --green:#5a8a6a; --red:#b85c5c; --blue:#5c7aa8;
            --sidebar-w:265px; --navbar-h:64px;
            --radius:16px; --radius-sm:10px;
            --shadow:0 4px 24px rgba(92,61,46,.07);
            --shadow-lg:0 8px 40px rgba(92,61,46,.13);
            --transition:all .22s cubic-bezier(.4,0,.2,1);
        }
        *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
        body{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--gray-800);min-height:100vh;}
        .navbar{position:fixed;top:0;left:0;right:0;height:var(--navbar-h);background:var(--brown-dark);display:flex;align-items:center;justify-content:space-between;padding:0 2rem;z-index:1000;box-shadow:0 2px 20px rgba(92,61,46,.25);}
        .navbar-brand{display:flex;align-items:center;gap:.65rem;text-decoration:none;}
        .logo-icon{width:38px;height:38px;background:linear-gradient(135deg,var(--beige-dark),var(--beige));border-radius:11px;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:700;color:var(--brown-dark);}
        .brand-text{font-family:'Cormorant Garamond',serif;color:var(--beige-light);font-size:1.35rem;font-weight:600;}
        .brand-text span{color:var(--beige-dark);}
        .navbar-right{display:flex;align-items:center;gap:.75rem;}
        .user-chip{display:flex;align-items:center;gap:.5rem;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:50px;padding:.3rem .75rem .3rem .3rem;text-decoration:none;transition:var(--transition);}
        .user-chip:hover{background:rgba(255,255,255,.14);}
        .user-avatar{width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--beige-dark),var(--brown-pale));display:flex;align-items:center;justify-content:center;font-size:.85rem;font-weight:700;color:var(--brown-dark);}
        .user-name{color:var(--beige-light);font-size:.85rem;font-weight:500;}
        .role-badge{font-size:.67rem;font-weight:600;padding:.15rem .5rem;border-radius:20px;text-transform:uppercase;letter-spacing:.05em;}
        .role-badge.professeur{background:rgba(200,169,154,.2);color:var(--beige-dark);border:1px solid rgba(200,169,154,.3);}
        .role-badge.etudiant{background:rgba(92,122,168,.2);color:#a8c0e8;border:1px solid rgba(92,122,168,.3);}
        .nav-btn{color:rgba(255,255,255,.6);text-decoration:none;padding:.4rem .65rem;border-radius:var(--radius-sm);transition:var(--transition);font-size:.95rem;}
        .nav-btn:hover{color:var(--beige-light);background:rgba(255,255,255,.08);}
        .app-layout{display:flex;padding-top:var(--navbar-h);min-height:100vh;}
        .sidebar{width:var(--sidebar-w);background:var(--white);border-right:1px solid var(--beige-dark);position:fixed;top:var(--navbar-h);bottom:0;left:0;overflow-y:auto;padding:1.5rem .9rem;display:flex;flex-direction:column;gap:.2rem;}
        .sidebar-section{font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--brown-pale);padding:1rem .75rem .35rem;}
        .sidebar-link{display:flex;align-items:center;gap:.7rem;padding:.65rem .85rem;border-radius:var(--radius-sm);color:var(--gray-600);text-decoration:none;font-size:.88rem;font-weight:500;transition:var(--transition);position:relative;}
        .sidebar-link i{font-size:1rem;width:20px;text-align:center;color:var(--brown-pale);}
        .sidebar-link:hover{background:var(--beige-light);color:var(--brown-dark);}
        .sidebar-link.active{background:var(--beige);color:var(--brown-dark);font-weight:600;}
        .sidebar-link.active::before{content:'';position:absolute;left:0;top:18%;bottom:18%;width:3px;background:var(--brown);border-radius:0 3px 3px 0;}
        .sidebar-divider{height:1px;background:var(--beige-dark);margin:.6rem .5rem;}
        .main-content{margin-left:var(--sidebar-w);flex:1;padding:2.25rem 2.5rem;}
        .page-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:2rem;gap:1rem;flex-wrap:wrap;}
        .page-subtitle{font-size:.82rem;color:var(--brown-pale);margin-bottom:.2rem;text-transform:uppercase;letter-spacing:.08em;font-weight:600;}
        .page-title{font-family:'Cormorant Garamond',serif;font-size:2rem;color:var(--brown-dark);font-weight:700;}
        .breadcrumb{display:flex;align-items:center;gap:.4rem;font-size:.78rem;color:var(--brown-pale);list-style:none;margin-bottom:.5rem;}
        .breadcrumb a{color:var(--brown-pale);text-decoration:none;}
        .breadcrumb a:hover{color:var(--brown-dark);}
        .card{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow);border:1px solid var(--beige-dark);overflow:hidden;}
        .card-header{padding:1.2rem 1.5rem;border-bottom:1px solid var(--beige);display:flex;align-items:center;justify-content:space-between;}
        .card-title{font-family:'Cormorant Garamond',serif;font-size:1.15rem;color:var(--brown-dark);display:flex;align-items:center;gap:.5rem;font-weight:600;}
        .card-body{padding:1.5rem;}
        .stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1.25rem;margin-bottom:2rem;}
        .stat-card{background:var(--white);border-radius:var(--radius);padding:1.5rem;border:1px solid var(--beige-dark);box-shadow:var(--shadow);position:relative;overflow:hidden;transition:var(--transition);}
        .stat-card:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg);}
        .stat-card::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;}
        .stat-card.c1::after{background:var(--brown-dark);}
        .stat-card.c2::after{background:var(--green);}
        .stat-card.c3::after{background:var(--blue);}
        .stat-card.c4::after{background:var(--brown-light);}
        .stat-icon{width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;margin-bottom:.9rem;}
        .stat-icon.c1{background:#ede0d4;color:var(--brown-dark);}
        .stat-icon.c2{background:#d4ede0;color:var(--green);}
        .stat-icon.c3{background:#d4dff0;color:var(--blue);}
        .stat-icon.c4{background:#f0e4de;color:var(--brown-light);}
        .stat-value{font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:700;color:var(--brown-dark);line-height:1;margin-bottom:.25rem;}
        .stat-label{font-size:.8rem;color:var(--brown-pale);font-weight:500;}
        .btn{display:inline-flex;align-items:center;gap:.45rem;padding:.55rem 1.15rem;border-radius:var(--radius-sm);font-size:.875rem;font-weight:600;border:none;cursor:pointer;text-decoration:none;transition:var(--transition);font-family:'DM Sans',sans-serif;}
        .btn-primary{background:var(--brown-dark);color:var(--beige-light);}
        .btn-primary:hover{background:var(--brown);transform:translateY(-1px);box-shadow:0 4px 14px rgba(92,61,46,.3);}
        .btn-outline{background:transparent;border:1.5px solid var(--beige-dark);color:var(--gray-600);}
        .btn-outline:hover{border-color:var(--brown);color:var(--brown-dark);background:var(--beige-light);}
        .btn-danger{background:#f5e8e8;color:var(--red);border:1.5px solid #e8c8c8;}
        .btn-danger:hover{background:var(--red);color:white;}
        .btn-sm{padding:.35rem .8rem;font-size:.8rem;}
        .form-group{margin-bottom:1.25rem;}
        .form-label{display:block;font-size:.83rem;font-weight:600;color:var(--brown-dark);margin-bottom:.4rem;}
        input[type=text],input[type=email],input[type=password],input[type=datetime-local],select,textarea,.form-control,.form-select{width:100%;padding:.65rem .95rem;border:1.5px solid var(--beige-dark);border-radius:var(--radius-sm);font-size:.9rem;font-family:'DM Sans',sans-serif;color:var(--gray-800);background:var(--beige-light);transition:var(--transition);outline:none;}
        input:focus,select:focus,textarea:focus{border-color:var(--brown);background:var(--white);box-shadow:0 0 0 3px rgba(92,61,46,.08);}
        textarea{resize:vertical;min-height:90px;}
        .errorlist{color:var(--red);font-size:.78rem;list-style:none;margin-top:.3rem;}
        .badge{display:inline-flex;align-items:center;gap:.3rem;padding:.25rem .7rem;border-radius:20px;font-size:.73rem;font-weight:600;}
        .badge-a_faire{background:#f0ebe5;color:#7d6557;}
        .badge-en_cours{background:#dde8f5;color:#3a5f8a;}
        .badge-termine{background:#d8eddf;color:#2f6b45;}
        .project-card{background:var(--white);border-radius:var(--radius);border:1.5px solid var(--beige-dark);overflow:hidden;transition:var(--transition);}
        .project-card:hover{box-shadow:var(--shadow-lg);transform:translateY(-3px);border-color:var(--brown-pale);}
        .project-name{font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;color:var(--brown-dark);text-decoration:none;display:block;margin-bottom:.25rem;}
        .project-name:hover{color:var(--brown-light);}
        .progress-wrap{height:5px;background:var(--beige);border-radius:10px;overflow:hidden;margin:.4rem 1.25rem .6rem;}
        .progress-fill{height:100%;border-radius:10px;background:linear-gradient(90deg,var(--brown-dark),var(--brown-light));}
        .progress-fill.high{background:linear-gradient(90deg,var(--green),#8ac4a0);}
        .task-card{background:var(--white);border:1.5px solid var(--beige-dark);border-radius:var(--radius);padding:1.1rem 1.3rem;transition:var(--transition);margin-bottom:.75rem;}
        .task-card:hover{border-color:var(--brown-pale);box-shadow:0 4px 16px rgba(92,61,46,.09);transform:translateY(-2px);}
        .task-card.overdue{border-left:3px solid var(--red);}
        .task-title{font-weight:600;color:var(--brown-dark);font-size:.93rem;margin-bottom:.35rem;}
        .task-meta{display:flex;align-items:center;gap:.75rem;flex-wrap:wrap;font-size:.77rem;color:var(--brown-pale);margin-top:.45rem;}
        .alert{padding:.85rem 1.1rem;border-radius:var(--radius-sm);font-size:.875rem;display:flex;align-items:center;gap:.6rem;margin-bottom:1rem;animation:slideDown .3s ease;}
        @keyframes slideDown{from{opacity:0;transform:translateY(-8px);}to{opacity:1;transform:translateY(0);}}
        .alert-success{background:#e0f0e6;color:#2f6040;border:1px solid #b8dcca;}
        .alert-error,.alert-danger{background:#f5e0e0;color:#8a2020;border:1px solid #e0b8b8;}
        .alert-info{background:#e0eaf5;color:#2a4a78;border:1px solid #b8cce0;}
        .alert-warning{background:#f5ecd8;color:#7a5010;border:1px solid #e0cca8;}
        .alert-close{margin-left:auto;background:none;border:none;cursor:pointer;color:inherit;opacity:.6;font-size:1rem;}
        .table-container{overflow-x:auto;border-radius:var(--radius);border:1px solid var(--beige-dark);}
        table{width:100%;border-collapse:collapse;font-size:.875rem;}
        thead th{background:var(--brown-dark);color:rgba(255,255,255,.85);font-weight:600;padding:.9rem 1.1rem;text-align:left;font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;}
        tbody tr{border-bottom:1px solid var(--beige);transition:var(--transition);}
        tbody tr:hover{background:var(--beige-light);}
        tbody td{padding:.9rem 1.1rem;}
        .filter-bar{display:flex;align-items:center;gap:.75rem;padding:.9rem 1.25rem;background:var(--white);border-radius:var(--radius);border:1px solid var(--beige-dark);margin-bottom:1.5rem;flex-wrap:wrap;}
        .filter-label{font-size:.75rem;font-weight:700;color:var(--brown-pale);text-transform:uppercase;letter-spacing:.08em;}
        .filter-select{padding:.4rem .8rem;border:1.5px solid var(--beige-dark);border-radius:8px;font-size:.84rem;font-family:'DM Sans',sans-serif;color:var(--brown-dark);background:var(--beige-light);outline:none;width:auto;}
        .empty-state{text-align:center;padding:4rem 2rem;color:var(--brown-pale);}
        .empty-state i{font-size:3rem;display:block;margin-bottom:1rem;opacity:.35;}
        .empty-state h4{color:var(--brown);margin-bottom:.5rem;font-family:'Cormorant Garamond',serif;font-size:1.2rem;}
        .empty-state p{font-size:.875rem;margin-bottom:1.5rem;}
        .auth-wrapper{min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(150deg,var(--brown-dark) 0%,var(--brown) 50%,var(--brown-light) 100%);position:relative;overflow:hidden;padding:2rem;}
        .auth-card{background:var(--white);border-radius:22px;width:100%;max-width:440px;box-shadow:0 30px 70px rgba(0,0,0,.25);overflow:hidden;position:relative;z-index:1;}
        .auth-card-header{background:linear-gradient(135deg,var(--brown-dark),var(--brown));padding:2.25rem 2rem;text-align:center;}
        .auth-logo{width:58px;height:58px;background:linear-gradient(135deg,var(--beige-dark),var(--beige-light));border-radius:18px;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:1.6rem;font-weight:700;color:var(--brown-dark);margin:0 auto 1rem;}
        .auth-card-header h2{font-family:'Cormorant Garamond',serif;color:var(--beige-light);font-size:1.65rem;margin-bottom:.3rem;font-weight:600;}
        .auth-card-header p{color:rgba(255,255,255,.55);font-size:.85rem;}
        .auth-card-body{padding:2rem;}
        .auth-link{color:var(--brown-dark);font-weight:600;text-decoration:none;}
        .auth-link:hover{color:var(--brown-light);}
        ::-webkit-scrollbar{width:6px;}
        ::-webkit-scrollbar-track{background:var(--beige-light);}
        ::-webkit-scrollbar-thumb{background:var(--beige-dark);border-radius:3px;}
        @media(max-width:768px){.sidebar{display:none;}.main-content{margin-left:0;padding:1.25rem;}.stat-grid{grid-template-columns:repeat(2,1fr);}.page-header{flex-direction:column;}}
    </style>
</head>
<body>
{% block content %}{% endblock %}
</body>
</html>
```

---

## ✅ Vérifie que `base.html` ne contient que ça

Le fichier doit avoir **exactement** :
- Commence par `<!DOCTYPE html>`
- Finit par `</html>`
- Contient **UNE SEULE fois** `{% block content %}{% endblock %}`
- **AUCUN** `{% extends %}` 
- **AUCUN** `{% include %}`

## 3️⃣ Vérifie `dashboard.html`

La première ligne doit être :
```
{% extends 'base.html' %}
et le fichier doit avoir {% block content %} ... {% endblock %} une seule fois.

Sauvegarde et rafraîchis ! 😊

merciii sa a marhé bebe

3 mars
🎉 Félicitations !!! Tu as réussi !

C'était beaucoup de débogage mais tu as tenu bon — bravo ! 💪

Ce que tu as accompli aujourd'hui
✅ Projet Django créé
✅ 3 apps (users, projects, tasks)
✅ Modèles de données (CustomUser, Project, Task, PrimeEvaluation)
✅ Authentification (login, register, logout)
✅ API REST avec JWT
✅ Templates HTML avec beau design beige/marron
✅ Tableau de bord avec statistiques
✅ Système de primes pour les professeurs
✅ Sidebar + Navbar fonctionnels
🚀 Prochaines étapes quand tu es prête
Tester toutes les pages — crée des projets, des tâches, teste les filtres
Créer des utilisateurs test — un professeur, un étudiant via /admin/
Frontend React — connecter l'API à une interface React moderne
Tests unitaires — lancer pytest
Documentation — README pour GitHub
N'hésite pas à revenir quand tu veux continuer ! 😊🍂

Livrables
1. Code source complet de l'application sur un dépôt GitHub ou GitLab.
2. Documentation incluant :
a. Instructions pour configurer et lancer le projet.
b. Explication des modèles de données et des routes API disponibles.
3. Présentation d'une démo fonctionnelle.

3 mars
Faisons tout ça ensemble ! Commençons par GitHub puis la documentation.

📤 PARTIE 1 : Mettre le code sur GitHub
Étape 1 — Créer un compte GitHub
Va sur https://github.com et crée un compte si tu n'en as pas.

Étape 2 — Créer un nouveau dépôt
Clique sur "New repository" (bouton vert)
Remplis :
Repository name : esmt-tasks
Description : Application de gestion des tâches collaboratives - ESMT
Visibility : Public
NE PAS cocher "Add README"
Clique "Create repository"
Étape 3 — Dans le terminal PyCharm
bash
# Assure-toi d'être dans le bon dossier
cd C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\backend

# Créer le fichier .gitignore
```

Crée un fichier `.gitignore` dans le dossier `backend/` avec ce contenu :
```
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# Django
*.log
local_settings.py
db.sqlite3
media/

# IDE
.idea/
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db
Étape 4 — Initialiser Git et pousser
bash
git init
git add .
git commit -m "Initial commit - ESMT Tasks App"
git branch -M main
git remote add origin https://github.com/TON_USERNAME/esmt-tasks.git
git push -u origin main
⚠️ Remplace TON_USERNAME par ton vrai nom GitHub !

📄 PARTIE 2 : Documentation (README.md)
Crée un fichier README.md dans le dossier backend/ :

markdown
# 📋 ESMT Tasks — Application de Gestion des Tâches Collaboratives

Application web développée pour l'ESMT permettant aux enseignants et étudiants 
de gérer des projets et tâches collaboratives, avec un système d'évaluation 
et de primes pour les professeurs.

---

## 🚀 Technologies utilisées

| Technologie | Rôle |
|---|---|
| Python 3.13 | Langage principal |
| Django 6.0 | Framework backend |
| Django REST Framework | API RESTful |
| SQLite | Base de données |
| JWT (SimpleJWT) | Authentification API |
| HTML/CSS/JS | Frontend (templates Django) |

---

## ⚙️ Installation et configuration

### 1. Prérequis
- Python 3.10+
- pip
- Git

### 2. Cloner le projet
```bash
git clone https://github.com/TON_USERNAME/esmt-tasks.git
cd esmt-tasks
```

### 3. Créer l'environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Installer les dépendances
```bash
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow pytest-django
```

### 5. Appliquer les migrations
```bash
python manage.py makemigrations users
python manage.py makemigrations projects
python manage.py makemigrations tasks
python manage.py migrate
```

### 6. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur
```bash
python manage.py runserver
```

### 8. Accéder à l'application
- Interface web : http://127.0.0.1:8000
- Administration : http://127.0.0.1:8000/admin
- API : http://127.0.0.1:8000/api/

---

## 👥 Profils utilisateurs

| Profil | Permissions |
|---|---|
| **Étudiant** | Créer projets, gérer ses tâches, ne peut pas assigner un professeur |
| **Professeur** | Créer projets, assigner des tâches, voir ses statistiques et primes |
| **Admin** | Accès total, gestion des utilisateurs, voir toutes les primes |

---

## 🏆 Système de primes

| Taux de complétion | Prime |
|---|---|
| 100% dans les délais | **100 000 FCFA** |
| 90% à 99% dans les délais | **30 000 FCFA** |
| Moins de 90% | Pas de prime |

---

## 🗃️ Modèles de données

### CustomUser
```
id          - Identifiant unique
username    - Nom d'utilisateur
email       - Adresse email
first_name  - Prénom
last_name   - Nom de famille
role        - etudiant | professeur
avatar      - Photo de profil
bio         - Biographie
```

### Project
```
id          - Identifiant unique
name        - Nom du projet
description - Description
created_by  - Créateur (FK → CustomUser)
members     - Membres (M2M → CustomUser)
created_at  - Date de création
updated_at  - Date de modification
```

### Task
```
id          - Identifiant unique
title       - Titre de la tâche
description - Description
project     - Projet (FK → Project)
assigned_to - Assigné à (FK → CustomUser)
created_by  - Créé par (FK → CustomUser)
status      - a_faire | en_cours | termine
priority    - basse | normale | haute | urgente
due_date    - Date limite
completed_at- Date de complétion
```

### PrimeEvaluation
```
id              - Identifiant unique
professeur      - Professeur (FK → CustomUser)
period          - T1 | T2 | T3 | T4 | annuel
year            - Année
total_tasks     - Nombre total de tâches
tasks_on_time   - Tâches terminées dans les délais
completion_rate - Taux de complétion (%)
prime_amount    - 0 | 30000 | 100000
```

---

## 🌐 Routes disponibles

### Pages Django Templates

| URL | Description |
|---|---|
| `/` | Tableau de bord |
| `/login/` | Connexion |
| `/register/` | Inscription |
| `/logout/` | Déconnexion |
| `/profile/` | Mon profil |
| `/projects/` | Liste des projets |
| `/projects/create/` | Créer un projet |
| `/projects/<id>/` | Détail d'un projet |
| `/projects/<id>/edit/` | Modifier un projet |
| `/projects/<id>/delete/` | Supprimer un projet |
| `/tasks/create/<project_id>/` | Créer une tâche |
| `/tasks/<id>/edit/` | Modifier une tâche |
| `/tasks/<id>/delete/` | Supprimer une tâche |
| `/tasks/statistics/` | Statistiques et primes |
| `/admin/` | Interface administration |

### API REST

| Méthode | URL | Description |
|---|---|---|
| POST | `/api/auth/register/` | Créer un compte |
| POST | `/api/auth/login/` | Connexion (JWT) |
| POST | `/api/auth/refresh/` | Rafraîchir le token |
| GET/PUT | `/api/users/me/` | Mon profil |
| GET | `/api/users/` | Liste des utilisateurs |
| GET/POST | `/api/projects/` | Projets |
| GET/PUT/DELETE | `/api/projects/<id>/` | Détail projet |
| GET/POST | `/api/projects/<id>/tasks/` | Tâches d'un projet |
| GET/PUT/DELETE | `/api/tasks/<id>/` | Détail tâche |
| GET | `/api/statistics/` | Statistiques et primes |

### Authentification API (JWT)
```bash
# 1. Obtenir un token
POST /api/auth/login/
{
  "username": "votre_username",
  "password": "votre_password"
}

# 2. Utiliser le token dans les requêtes
Headers: Authorization: Bearer 
```

---

## 🧪 Tests
```bash
# Installer pytest
pip install pytest-django

# Lancer les tests
pytest tests/ -v
```

---

## 📁 Structure du projet
```
esmt-tasks/
├── backend/
│   ├── settings.py
│   └── urls.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── projects/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── partials/
│   ├── users/
│   ├── projects/
│   └── tasks/
├── static/
├── media/
├── manage.py
├── .gitignore
└── README.md
```

---

## 👩‍💻 Développé par

**[Ton Prénom Nom]**  
Étudiant(e) en Développement d'Applications et Réseaux — ESMT  
Année académique 2025-2026
```

---

## 🎬 PARTIE 3 : Démo fonctionnelle

Pour la présentation, voici le script à suivre :

### Plan de démonstration (10-15 min)
```
1️⃣ INSCRIPTION & CONNEXION (2 min)
   → Créer un compte Professeur
   → Créer un compte Étudiant
   → Se connecter

2️⃣ GESTION DES PROJETS (3 min)
   → Créer un projet
   → Ajouter des membres
   → Voir la liste des projets

3️⃣ GESTION DES TÂCHES (3 min)
   → Créer des tâches avec dates limites
   → Assigner aux membres
   → Changer les statuts (à faire → en cours → terminé)
   → Montrer les filtres

4️⃣ STATISTIQUES & PRIMES (3 min)
   → Voir le tableau de bord
   → Aller dans Statistiques
   → Montrer le calcul des primes professeurs

5️⃣ API REST (2 min)
   → Ouvrir http://127.0.0.1:8000/api/
   → Montrer le token JWT
   → Faire une requête GET /api/projects/

6️⃣ ADMINISTRATION (2 min)
   → Se connecter à /admin/
   → Montrer la gestion des utilisateurs
   → Changer le rôle d'un utilisateur
```

---

## ✅ Checklist finale avant soumission
```
☐ Code sur GitHub/GitLab
☐ README.md complet
☐ .gitignore présent (pas de db.sqlite3 ni venv dans le repo)
☐ Toutes les fonctionnalités testées
☐ Superuser créé pour la démo
☐ Données de test créées (projets, tâches, utilisateurs)
☐ Tests unitaires qui passent
Dis-moi si tu veux de l'aide pour une étape en particulier ! 😊 Et félicitations pour ce projet complet 🎉

J'ai supprimer mon projet ans faire epres

18:33
Oh non ! 😱 Pas de panique, on peut recréer tout ça !

Dis-moi exactement ce qui s'est passé :

Q : Qu'est-ce que tu as supprimé exactement ?
R : Tout le dossier ProjetPy

Q : Est-ce que tu as encore les fichiers quelque part ?
R : Oui dans la Corbeille Windows

18:34
Super, les fichiers sont encore dans la Corbeille ! 😮‍💨 Vite, avant de faire quoi que ce soit d'autre :

🚨 ÉTAPE 1 — Restaurer depuis la Corbeille (MAINTENANT)
Double-clique sur l'icône Corbeille sur ton Bureau
Cherche le dossier ProjetPy
Clic droit dessus → Restaurer
Le dossier revient automatiquement à son emplacement original : C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy
✅ ÉTAPE 2 — Vérifier que tout est là
Une fois restauré, ouvre PyCharm et vérifie que tu vois bien :

ProjetPy/
  venv/
  backend/
    manage.py
    backend/
    users/
    projects/
    tasks/
    templates/
✅ ÉTAPE 3 — Tester que ça fonctionne encore
bash
cd C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\backend
venv\Scripts\activate
python manage.py runserver
Dis-moi dès que c'est restauré ! 😊 Et cette fois on va immédiatement le pousser sur GitHub pour ne plus jamais risquer ça ! 🔒

je ne vois rien dans la corbeille j'avais fait un restauration de toute la corbeille car hier je n'avais plus d'espace donc j'ai supprimer pleins de choses

18:36
Oh non... 😔 Si la corbeille a été vidée, les fichiers sont probablement irrécupérables par les moyens normaux.

Mais avant de paniquer, essayons une dernière chose :

Q : Est-ce que tu avais poussé le code sur GitHub avant de supprimer ?
R : Non, je n'avais pas encore fait ça

Q : Est-ce que PyCharm a encore le projet ouvert (même si les fichiers sont supprimés) ?
R : Oui PyCharm est encore ouvert avec le projet

18:36
🎉 PyCharm ouvert = fichiers encore en mémoire = on peut tout sauver !

🚨 FAIS ÇA MAINTENANT — Ne ferme surtout pas PyCharm !
Étape 1 — Recréer le dossier
Dans le terminal PyCharm, tape :

bash
mkdir C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy
mkdir C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\backend
```

### Étape 2 — Sauvegarder depuis PyCharm

Dans PyCharm, pour **chaque fichier** encore visible dans l'arborescence à gauche :
1. Clique sur le fichier
2. **Ctrl+A** pour tout sélectionner
3. **Ctrl+C** pour copier
4. Recrée le fichier au bon endroit et colle

**OU encore plus simple :**

Dans PyCharm → menu **File** → **Save All** (Ctrl+S) — PyCharm va tenter de réécrire les fichiers.

---

### Étape 3 — Vérifier les fichiers visibles

Dis-moi ce que tu vois encore dans l'arborescence PyCharm à gauche. Quelque chose comme ça ?
```
📁 backend
  📁 backend (settings.py, urls.py...)
  📁 users
  📁 projects  
  📁 tasks
  📁 templates
  📄 manage.py
Dis-moi exactement ce que tu vois et on sauve fichier par fichier si nécessaire ! 😊

The path C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy does not exist.
If it is on a removable or network drive, please make sure that the drive is connecte

18:37
Fais File → Save All dans PyCharm d'abord, puis dis-moi ce que tu vois dans l'arborescence à gauche (le panneau Project).

En attendant, crée le dossier autrement :

Dans le terminal Windows (pas PyCharm) — touche Windows + R → tape cmd
cmd
mkdir "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy"
mkdir "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\backend"
Puis dans PyCharm, essaie File → Save All encore une fois.

Mais la vraie question c'est : est-ce que tu vois encore les fichiers dans l'arborescence PyCharm à gauche ? Fais une capture d'écran ou dis-moi ce que tu vois dans le panneau "Project" à gauche de PyCharm.

Si les fichiers sont encore visibles là, on peut tout récupérer ! 😊

Je ne vois rien on peut refaire le projet

18:38
Pas de problème, on repart de zéro ensemble ! 💪 J'ai tout en mémoire depuis notre session.

🚀 Étape 1 — Recréer la structure
Dans le terminal Windows (cmd) :

cmd
mkdir "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy"
cd "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy"
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow
django-admin startproject backend .
cd backend
python manage.py startapp users
python manage.py startapp projects
python manage.py startapp tasks
mkdir templates
mkdir templates\users
mkdir templates\projects
mkdir templates\tasks
mkdir templates\partials
mkdir static
mkdir media
Dis-moi quand c'est fait et on attaque les fichiers un par un dans l'ordre ! 😊

Et cette fois on pousse sur GitHub dès le début pour ne plus jamais perdre le travail. 🔒

Windows PowerShell
Copyright (C) Microsoft Corporation. Tous droits réservés.
Installez la dernière version de PowerShell pour de nouvelles fonctionnalités et améliorations ! https://aka.ms/PSWindows
(.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\PythonProject> mkdir C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy
    Répertoire : C:\Users\HP\Desktop\Cours-Semestre1-DAR\python
Mode                 LastWriteTime         Length Name            
----                 -------------         ------ ----            
d-----        12/03/2026     18:40                ProjetPy        
(.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\PythonProject>

Afficher plus
18:41
Bien ! Le dossier est créé. Continue avec les commandes suivantes une par une :

powershell
cd "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy"
powershell
python -m venv venv
powershell
venv\Scripts\activate
powershell
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow
powershell
django-admin startproject backend .
powershell
cd backend
powershell
python manage.py startapp users
python manage.py startapp projects
python manage.py startapp tasks
powershell
mkdir templates
mkdir templates\users
mkdir templates\projects
mkdir templates\tasks
mkdir templates\partials
mkdir static
mkdir media
Dis-moi quand chaque étape est terminée ou si tu as une erreur ! 😊


Windows PowerShell Copyright (C) Microsoft Corporation. Tous droits réservés. Installez la dernière version de PowerShell pour de nouvelles fonctionnalités et améliorations ! https://aka.ms/PSWindows (.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\PythonProject> mkdir C:\Users\HP\De

pasted

18:46
Parfait, la structure est créée ! 🎉 Maintenant on attaque les fichiers.

⚠️ Note importante : cette fois le projet est à la racine de ProjetPy/ et non dans ProjetPy/backend/. Donc toutes les commandes se font depuis ProjetPy/.

Fichier 1 — backend/settings.py
Ouvre backend/settings.py dans PyCharm, Ctrl+A puis tout remplacer par :

python
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-esmt-tasks-2026-secret-key-change-in-production'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'users',
    'projects',
    'tasks',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Dakar'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

CORS_ALLOW_ALL_ORIGINS = True
Sauvegarde avec Ctrl+S et dis-moi quand c'est fait ! 😊

je ne vois aucun des dossiers creer

18:47
Le projet a été créé à la racine de ProjetPy/ et non dans un sous-dossier backend/. Ouvre PyCharm et fais ceci :

Ouvrir le bon dossier dans PyCharm
File → Open → navigue vers :

C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy
→ Clique OK

PyCharm doit afficher cette structure à gauche :

📁 ProjetPy
  📁 backend
  📁 media
  📁 projects
  📁 static
  📁 tasks
  📁 templates
    📁 partials
    📁 projects
    📁 tasks
    📁 users
  📁 users
  📁 venv
  📄 manage.py
Dis-moi ce que tu vois après avoir ouvert ce dossier ! 😊

rien

18:48
Vérifions si les fichiers existent vraiment. Dans PowerShell :

powershell
dir "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy"
Copie-colle le résultat ici ! 😊

esktop\Cours-Semestre1-DAR\python\ProjetPy>dir "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy"
    Répertoire: 
    C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy
Mode                 LastWriteTime         Length Name            
----                 -------------         ------ ----            
d-----        12/03/2026     18:45                backend         
d-----        12/03/2026     18:46                media           
d-----        12/03/2026     18:45                projects        
d-----        12/03/2026     18:46                static          
d-----        12/03/2026     18:46                tasks           
d-----        12/03/2026     18:46                templates       
d-----        12/03/2026     18:45                users           
d-----        12/03/2026     18:41                venv            
-a----        12/03/2026     18:43            685 manage.py       
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>

Afficher plus
18:48
Les fichiers existent bien ! C'est juste PyCharm qui n'est pas ouvert sur le bon dossier.

Dans PyCharm :
File → Open → navigue jusqu'à :

C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy
Clique sur le dossier ProjetPy (pas dedans, juste le sélectionner) → OK

PyCharm va demander :

"Open in new window or this window?"

Choisis "This Window"

Tu devrais voir apparaître tous les dossiers à gauche. Dis-moi quand c'est fait ! 😊

c'est fait

18:51
Parfait ! 🎉 Maintenant on attaque les fichiers un par un.

Fichier 1 — backend/settings.py
Dans PyCharm, ouvre backend/settings.py, fais Ctrl+A puis Suppr, et colle ceci :

python
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-esmt-tasks-2026-secret-key-change-in-production'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'users',
    'projects',
    'tasks',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Dakar'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

CORS_ALLOW_ALL_ORIGINS = True
Ctrl+S pour sauvegarder. Dis-moi quand c'est fait ! 😊

oui

18:51
Fichier 2 — backend/urls.py
Ouvre backend/urls.py, Ctrl+A → Suppr, colle ceci :

python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    path('api/', include('users.api_urls')),
    path('api/', include('projects.api_urls')),
    path('api/', include('tasks.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Ctrl+S → dis-moi quand c'est fait ! 😊

fait

18:52
Fichier 3 — users/models.py
Ouvre users/models.py, Ctrl+A → Suppr, colle ceci :

python
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('etudiant', 'Étudiant'),
        ('professeur', 'Professeur'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='etudiant')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_professeur(self):
        return self.role == 'professeur'

    @property
    def is_etudiant(self):
        return self.role == 'etudiant'
Ctrl+S → dis-moi quand c'est fait ! 😊

f

18:52
Fichier 4 — users/forms.py
Crée un nouveau fichier users/forms.py (clic droit sur le dossier users → New → Python File → forms), colle ceci :

python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'bio', 'avatar']
Ctrl+S → dis-moi quand c'est fait ! 😊

f

18:53
Fichier 5 — users/views.py
Ouvre users/views.py, Ctrl+A → Suppr, colle ceci :

python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, ProfileForm
from tasks.models import Task
from projects.models import Project


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
            return redirect('dashboard')
        else:
            messages.error(request, 'Identifiants incorrects.')
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):
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
Ctrl+S → dis-moi quand c'est fait ! 😊

f

18:54
Fichier 6 — users/urls.py
Ouvre users/urls.py, Ctrl+A → Suppr, colle ceci :

python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
Ctrl+S → dis-moi quand c'est fait ! 😊

amene moi tout et quand je fini tout je te fait un retour

18:59
Voici TOUS les fichiers restants d'un coup ! 💪

Fichier 7 — users/serializers.py
Crée users/serializers.py :

python
from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'avatar', 'bio']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
Fichier 8 — users/api_views.py
Crée users/api_views.py :

python
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class MeAPIView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
Fichier 9 — users/api_urls.py
Crée users/api_urls.py :

python
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import RegisterAPIView, MeAPIView, UserListAPIView

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name='api_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='api_login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='api_refresh'),
    path('users/me/', MeAPIView.as_view(), name='api_me'),
    path('users/', UserListAPIView.as_view(), name='api_users'),
]
Fichier 10 — projects/models.py
Ouvre projects/models.py, Ctrl+A → Suppr :

python
from django.db import models
from users.models import CustomUser


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_projects')
    members = models.ManyToManyField(CustomUser, related_name='member_projects', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_completion_rate(self):
        total = self.tasks.count()
        if total == 0:
            return 0
        done = self.tasks.filter(status='termine').count()
        return round((done / total) * 100)
Fichier 11 — projects/forms.py
Crée projects/forms.py :

python
from django import forms
from .models import Project
from users.models import CustomUser


class ProjectForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Membres'
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'members']
Fichier 12 — projects/views.py
Ouvre projects/views.py, Ctrl+A → Suppr :

python
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
Fichier 13 — projects/urls.py
Ouvre projects/urls.py, Ctrl+A → Suppr :

python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
]
Fichier 14 — projects/serializers.py
Crée projects/serializers.py :

python
from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    completion_rate = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_by', 'members', 'completion_rate', 'created_at']

    def get_completion_rate(self, obj):
        return obj.get_completion_rate()
Fichier 15 — projects/api_views.py
Crée projects/api_views.py :

python
from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer
from tasks.serializers import TaskSerializer
from tasks.models import Task


class ProjectListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user) | \
               Project.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)


class TaskListCreateAPI(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['pk'])
        serializer.save(project=project, created_by=self.request.user)
Fichier 16 — projects/api_urls.py
Crée projects/api_urls.py :

python
from django.urls import path
from .api_views import ProjectListCreateAPI, ProjectDetailAPI, TaskListCreateAPI

urlpatterns = [
    path('projects/', ProjectListCreateAPI.as_view(), name='api_projects'),
    path('projects/<int:pk>/', ProjectDetailAPI.as_view(), name='api_project_detail'),
    path('projects/<int:pk>/tasks/', TaskListCreateAPI.as_view(), name='api_project_tasks'),
]
Fichier 17 — tasks/models.py
Ouvre tasks/models.py, Ctrl+A → Suppr :

python
from django.db import models
from django.utils import timezone
from users.models import CustomUser
from projects.models import Project


class Task(models.Model):
    STATUS_CHOICES = [
        ('a_faire', 'À faire'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
    ]
    PRIORITY_CHOICES = [
        ('basse', 'Basse'),
        ('normale', 'Normale'),
        ('haute', 'Haute'),
        ('urgente', 'Urgente'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='a_faire')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normale')
    due_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.status == 'termine' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status != 'termine':
            self.completed_at = None
        super().save(*args, **kwargs)

    def is_overdue(self):
        if self.due_date and self.status != 'termine':
            return timezone.now() > self.due_date
        return False

    def completed_on_time(self):
        if self.completed_at and self.due_date:
            return self.completed_at <= self.due_date
        return False


class PrimeEvaluation(models.Model):
    PERIOD_CHOICES = [
        ('T1', 'Trimestre 1'),
        ('T2', 'Trimestre 2'),
        ('T3', 'Trimestre 3'),
        ('T4', 'Trimestre 4'),
        ('annuel', 'Annuel'),
    ]

    professeur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='evaluations')
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    year = models.IntegerField()
    total_tasks = models.IntegerField(default=0)
    tasks_on_time = models.IntegerField(default=0)
    completion_rate = models.FloatField(default=0)
    prime_amount = models.IntegerField(default=0)

    def calculate_prime(self):
        if self.total_tasks == 0:
            return 0
        self.completion_rate = (self.tasks_on_time / self.total_tasks) * 100
        if self.completion_rate == 100:
            self.prime_amount = 100000
        elif self.completion_rate >= 90:
            self.prime_amount = 30000
        else:
            self.prime_amount = 0
        return self.prime_amount
Fichier 18 — tasks/forms.py
Crée tasks/forms.py :

python
from django import forms
from .models import Task
from users.models import CustomUser


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'status', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_etudiant:
            self.fields['assigned_to'].queryset = CustomUser.objects.filter(role='etudiant')
        else:
            self.fields['assigned_to'].queryset = CustomUser.objects.all()
Fichier 19 — tasks/views.py
Ouvre tasks/views.py, Ctrl+A → Suppr :

python
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
Fichier 20 — tasks/urls.py
Ouvre tasks/urls.py, Ctrl+A → Suppr :

python
from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:project_pk>/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('statistics/', views.statistics_view, name='statistics'),
]
Fichier 21 — tasks/serializers.py
Crée tasks/serializers.py :

python
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assigned_to',
                  'created_by', 'status', 'priority', 'due_date', 'completed_at',
                  'created_at', 'is_overdue']
        read_only_fields = ['created_by', 'completed_at', 'created_at']

    def get_is_overdue(self, obj):
        return obj.is_overdue()
Fichier 22 — tasks/api_views.py
Crée tasks/api_views.py :

python
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project__created_by=self.request.user) | \
               Task.objects.filter(assigned_to=self.request.user)


class StatisticsAPI(generics.GenericAPIView):
    def get(self, request):
        from django.utils import timezone
        from rest_framework.response import Response
        year = timezone.now().year
        tasks = Task.objects.filter(assigned_to=request.user)
        total = tasks.count()
        done = tasks.filter(status='termine').count()
        on_time = sum(1 for t in tasks if t.completed_on_time())
        rate = round((on_time / total * 100)) if total > 0 else 0
        prime = 100000 if rate == 100 else (30000 if rate >= 90 else 0)
        return Response({
            'year': year, 'total_tasks': total,
            'done_tasks': done, 'on_time': on_time,
            'completion_rate': rate, 'prime': prime
        })
Fichier 23 — tasks/api_urls.py
Crée tasks/api_urls.py :

python
from django.urls import path
from .api_views import TaskDetailAPI, StatisticsAPI

urlpatterns = [
    path('tasks/<int:pk>/', TaskDetailAPI.as_view(), name='api_task_detail'),
    path('statistics/', StatisticsAPI.as_view(), name='api_statistics'),
]
Fichier 24 — users/admin.py
Ouvre users/admin.py, Ctrl+A → Suppr :

python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'role', 'is_staff']
    list_filter = ['role', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Profil ESMT', {'fields': ('role', 'avatar', 'bio')}),
    )
Fichier 25 — projects/admin.py
Ouvre projects/admin.py, Ctrl+A → Suppr :

python
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at']
    list_filter = ['created_at']
Fichier 26 — tasks/admin.py
Ouvre tasks/admin.py, Ctrl+A → Suppr :

python
from django.contrib import admin
from .models import Task, PrimeEvaluation


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'assigned_to', 'status', 'priority', 'due_date']
    list_filter = ['status', 'priority']


@admin.register(PrimeEvaluation)
class PrimeEvaluationAdmin(admin.ModelAdmin):
    list_display = ['professeur', 'period', 'year', 'completion_rate', 'prime_amount']
Fichiers 27-35 — Templates
templates/base.html
Crée ce fichier :

html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}ESMT Tasks{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        :root {
            --brown-dark:#5c3d2e; --brown:#7d5a4f; --brown-light:#a67c6d;
            --brown-pale:#c8a99a; --beige-dark:#e8d5c4; --beige:#f2e8dc;
            --beige-light:#f8f2eb; --cream:#fdf9f5; --white:#ffffff;
            --gray-600:#6b5c54; --gray-800:#3d2c26;
            --green:#5a8a6a; --red:#b85c5c; --blue:#5c7aa8;
            --sidebar-w:265px; --navbar-h:64px;
            --radius:16px; --radius-sm:10px;
            --shadow:0 4px 24px rgba(92,61,46,.07);
            --shadow-lg:0 8px 40px rgba(92,61,46,.13);
            --transition:all .22s cubic-bezier(.4,0,.2,1);
        }
        *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
        body{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--gray-800);min-height:100vh;}
        .navbar{position:fixed;top:0;left:0;right:0;height:var(--navbar-h);background:var(--brown-dark);display:flex;align-items:center;justify-content:space-between;padding:0 2rem;z-index:1000;box-shadow:0 2px 20px rgba(92,61,46,.25);}
        .navbar-brand{display:flex;align-items:center;gap:.65rem;text-decoration:none;}
        .logo-icon{width:38px;height:38px;background:linear-gradient(135deg,var(--beige-dark),var(--beige));border-radius:11px;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:700;color:var(--brown-dark);}
        .brand-text{font-family:'Cormorant Garamond',serif;color:var(--beige-light);font-size:1.35rem;font-weight:600;}
        .navbar-right{display:flex;align-items:center;gap:.75rem;}
        .user-chip{display:flex;align-items:center;gap:.5rem;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:50px;padding:.3rem .75rem .3rem .3rem;text-decoration:none;transition:var(--transition);}
        .user-chip:hover{background:rgba(255,255,255,.14);}
        .user-avatar{width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,var(--beige-dark),var(--brown-pale));display:flex;align-items:center;justify-content:center;font-size:.85rem;font-weight:700;color:var(--brown-dark);}
        .user-name{color:var(--beige-light);font-size:.85rem;font-weight:500;}
        .role-badge{font-size:.67rem;font-weight:600;padding:.15rem .5rem;border-radius:20px;text-transform:uppercase;letter-spacing:.05em;}
        .role-badge.professeur{background:rgba(200,169,154,.2);color:var(--beige-dark);}
        .role-badge.etudiant{background:rgba(92,122,168,.2);color:#a8c0e8;}
        .nav-btn{color:rgba(255,255,255,.6);text-decoration:none;padding:.4rem .65rem;border-radius:var(--radius-sm);transition:var(--transition);font-size:.95rem;}
        .nav-btn:hover{color:var(--beige-light);background:rgba(255,255,255,.08);}
        .app-layout{display:flex;padding-top:var(--navbar-h);min-height:100vh;}
        .sidebar{width:var(--sidebar-w);background:var(--white);border-right:1px solid var(--beige-dark);position:fixed;top:var(--navbar-h);bottom:0;left:0;overflow-y:auto;padding:1.5rem .9rem;display:flex;flex-direction:column;gap:.2rem;}
        .sidebar-section{font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--brown-pale);padding:1rem .75rem .35rem;}
        .sidebar-link{display:flex;align-items:center;gap:.7rem;padding:.65rem .85rem;border-radius:var(--radius-sm);color:var(--gray-600);text-decoration:none;font-size:.88rem;font-weight:500;transition:var(--transition);position:relative;}
        .sidebar-link i{font-size:1rem;width:20px;text-align:center;color:var(--brown-pale);}
        .sidebar-link:hover{background:var(--beige-light);color:var(--brown-dark);}
        .sidebar-link.active{background:var(--beige);color:var(--brown-dark);font-weight:600;}
        .sidebar-link.active::before{content:'';position:absolute;left:0;top:18%;bottom:18%;width:3px;background:var(--brown);border-radius:0 3px 3px 0;}
        .sidebar-divider{height:1px;background:var(--beige-dark);margin:.6rem .5rem;}
        .main-content{margin-left:var(--sidebar-w);flex:1;padding:2.25rem 2.5rem;}
        .page-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:2rem;gap:1rem;flex-wrap:wrap;}
        .page-subtitle{font-size:.82rem;color:var(--brown-pale);margin-bottom:.2rem;text-transform:uppercase;letter-spacing:.08em;font-weight:600;}
        .page-title{font-family:'Cormorant Garamond',serif;font-size:2rem;color:var(--brown-dark);font-weight:700;}
        .breadcrumb{display:flex;align-items:center;gap:.4rem;font-size:.78rem;color:var(--brown-pale);list-style:none;margin-bottom:.5rem;}
        .breadcrumb a{color:var(--brown-pale);text-decoration:none;}
        .card{background:var(--white);border-radius:var(--radius);box-shadow:var(--shadow);border:1px solid var(--beige-dark);overflow:hidden;}
        .card-header{padding:1.2rem 1.5rem;border-bottom:1px solid var(--beige);display:flex;align-items:center;justify-content:space-between;}
        .card-title{font-family:'Cormorant Garamond',serif;font-size:1.15rem;color:var(--brown-dark);font-weight:600;}
        .card-body{padding:1.5rem;}
        .stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1.25rem;margin-bottom:2rem;}
        .stat-card{background:var(--white);border-radius:var(--radius);padding:1.5rem;border:1px solid var(--beige-dark);box-shadow:var(--shadow);position:relative;overflow:hidden;transition:var(--transition);}
        .stat-card:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg);}
        .stat-card::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;}
        .stat-card.c1::after{background:var(--brown-dark);}
        .stat-card.c2::after{background:var(--green);}
        .stat-card.c3::after{background:var(--blue);}
        .stat-card.c4::after{background:var(--brown-light);}
        .stat-icon{width:44px;height:44px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;margin-bottom:.9rem;}
        .stat-icon.c1{background:#ede0d4;color:var(--brown-dark);}
        .stat-icon.c2{background:#d4ede0;color:var(--green);}
        .stat-icon.c3{background:#d4dff0;color:var(--blue);}
        .stat-icon.c4{background:#f0e4de;color:var(--brown-light);}
        .stat-value{font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:700;color:var(--brown-dark);line-height:1;margin-bottom:.25rem;}
        .stat-label{font-size:.8rem;color:var(--brown-pale);font-weight:500;}
        .btn{display:inline-flex;align-items:center;gap:.45rem;padding:.55rem 1.15rem;border-radius:var(--radius-sm);font-size:.875rem;font-weight:600;border:none;cursor:pointer;text-decoration:none;transition:var(--transition);font-family:'DM Sans',sans-serif;}
        .btn-primary{background:var(--brown-dark);color:var(--beige-light);}
        .btn-primary:hover{background:var(--brown);transform:translateY(-1px);}
        .btn-outline{background:transparent;border:1.5px solid var(--beige-dark);color:var(--gray-600);}
        .btn-outline:hover{border-color:var(--brown);color:var(--brown-dark);background:var(--beige-light);}
        .btn-danger{background:#f5e8e8;color:var(--red);border:1.5px solid #e8c8c8;}
        .btn-danger:hover{background:var(--red);color:white;}
        .btn-sm{padding:.35rem .8rem;font-size:.8rem;}
        .form-group{margin-bottom:1.25rem;}
        .form-label{display:block;font-size:.83rem;font-weight:600;color:var(--brown-dark);margin-bottom:.4rem;}
        input[type=text],input[type=email],input[type=password],input[type=datetime-local],select,textarea{width:100%;padding:.65rem .95rem;border:1.5px solid var(--beige-dark);border-radius:var(--radius-sm);font-size:.9rem;font-family:'DM Sans',sans-serif;color:var(--gray-800);background:var(--beige-light);transition:var(--transition);outline:none;}
        input:focus,select:focus,textarea:focus{border-color:var(--brown);background:var(--white);box-shadow:0 0 0 3px rgba(92,61,46,.08);}
        textarea{resize:vertical;min-height:90px;}
        .errorlist{color:var(--red);font-size:.78rem;list-style:none;margin-top:.3rem;}
        .badge{display:inline-flex;align-items:center;padding:.25rem .7rem;border-radius:20px;font-size:.73rem;font-weight:600;}
        .badge-a_faire{background:#f0ebe5;color:#7d6557;}
        .badge-en_cours{background:#dde8f5;color:#3a5f8a;}
        .badge-termine{background:#d8eddf;color:#2f6b45;}
        .project-card{background:var(--white);border-radius:var(--radius);border:1.5px solid var(--beige-dark);overflow:hidden;transition:var(--transition);}
        .project-card:hover{box-shadow:var(--shadow-lg);transform:translateY(-3px);}
        .project-name{font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;color:var(--brown-dark);text-decoration:none;display:block;margin-bottom:.25rem;}
        .progress-wrap{height:5px;background:var(--beige);border-radius:10px;overflow:hidden;margin:.4rem 1.25rem .6rem;}
        .progress-fill{height:100%;border-radius:10px;background:linear-gradient(90deg,var(--brown-dark),var(--brown-light));}
        .progress-fill.high{background:linear-gradient(90deg,var(--green),#8ac4a0);}
        .task-card{background:var(--white);border:1.5px solid var(--beige-dark);border-radius:var(--radius);padding:1.1rem 1.3rem;transition:var(--transition);margin-bottom:.75rem;}
        .task-card:hover{border-color:var(--brown-pale);box-shadow:0 4px 16px rgba(92,61,46,.09);}
        .task-card.overdue{border-left:3px solid var(--red);}
        .task-title{font-weight:600;color:var(--brown-dark);font-size:.93rem;}
        .task-meta{display:flex;align-items:center;gap:.75rem;flex-wrap:wrap;font-size:.77rem;color:var(--brown-pale);margin-top:.45rem;}
        .alert{padding:.85rem 1.1rem;border-radius:var(--radius-sm);font-size:.875rem;display:flex;align-items:center;gap:.6rem;margin-bottom:1rem;}
        .alert-success{background:#e0f0e6;color:#2f6040;border:1px solid #b8dcca;}
        .alert-error,.alert-danger{background:#f5e0e0;color:#8a2020;border:1px solid #e0b8b8;}
        .alert-info{background:#e0eaf5;color:#2a4a78;border:1px solid #b8cce0;}
        .alert-warning{background:#f5ecd8;color:#7a5010;border:1px solid #e0cca8;}
        .alert-close{margin-left:auto;background:none;border:none;cursor:pointer;color:inherit;opacity:.6;}
        .table-container{overflow-x:auto;}
        table{width:100%;border-collapse:collapse;font-size:.875rem;}
        thead th{background:var(--brown-dark);color:rgba(255,255,255,.85);font-weight:600;padding:.9rem 1.1rem;text-align:left;font-size:.78rem;text-transform:uppercase;}
        tbody tr{border-bottom:1px solid var(--beige);transition:var(--transition);}
        tbody tr:hover{background:var(--beige-light);}
        tbody td{padding:.9rem 1.1rem;}
        .filter-bar{display:flex;align-items:center;gap:.75rem;padding:.9rem 1.25rem;background:var(--white);border-radius:var(--radius);border:1px solid var(--beige-dark);margin-bottom:1.5rem;flex-wrap:wrap;}
        .filter-label{font-size:.75rem;font-weight:700;color:var(--brown-pale);text-transform:uppercase;letter-spacing:.08em;}
        .filter-select{padding:.4rem .8rem;border:1.5px solid var(--beige-dark);border-radius:8px;font-size:.84rem;color:var(--brown-dark);background:var(--beige-light);outline:none;width:auto;}
        .empty-state{text-align:center;padding:4rem 2rem;color:var(--brown-pale);}
        .empty-state i{font-size:3rem;display:block;margin-bottom:1rem;opacity:.35;}
        .empty-state h4{color:var(--brown);margin-bottom:.5rem;font-family:'Cormorant Garamond',serif;font-size:1.2rem;}
        .auth-wrapper{min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(150deg,var(--brown-dark) 0%,var(--brown) 50%,var(--brown-light) 100%);padding:2rem;}
        .auth-card{background:var(--white);border-radius:22px;width:100%;max-width:440px;box-shadow:0 30px 70px rgba(0,0,0,.25);overflow:hidden;}
        .auth-card-header{background:linear-gradient(135deg,var(--brown-dark),var(--brown));padding:2.25rem 2rem;text-align:center;}
        .auth-logo{width:58px;height:58px;background:linear-gradient(135deg,var(--beige-dark),var(--beige-light));border-radius:18px;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:1.6rem;font-weight:700;color:var(--brown-dark);margin:0 auto 1rem;}
        .auth-card-header h2{font-family:'Cormorant Garamond',serif;color:var(--beige-light);font-size:1.65rem;margin-bottom:.3rem;}
        .auth-card-header p{color:rgba(255,255,255,.55);font-size:.85rem;}
        .auth-card-body{padding:2rem;}
        .auth-link{color:var(--brown-dark);font-weight:600;text-decoration:none;}
        @media(max-width:768px){.sidebar{display:none;}.main-content{margin-left:0;padding:1.25rem;}}
    </style>
</head>
<body>
{% block content %}{% endblock %}
</body>
</html>
templates/partials/navbar.html
Crée ce fichier :

html
<nav class="navbar">
    <a href="{% url 'dashboard' %}" class="navbar-brand">
        <div class="logo-icon">E</div>
        <span class="brand-text">ESMT <span>Tasks</span></span>
    </a>
    <div class="navbar-right">
        <a href="{% url 'profile' %}" class="user-chip">
            <div class="user-avatar">{{ request.user.username.0|upper }}</div>
            <span class="user-name">{{ request.user.username }}</span>
            <span class="role-badge {{ request.user.role }}">{{ request.user.get_role_display }}</span>
        </a>
        <a href="{% url 'logout' %}" class="nav-btn"><i class="bi bi-box-arrow-right"></i></a>
    </div>
</nav>
templates/partials/sidebar.html
Crée ce fichier :

html
<aside class="sidebar">
    <div class="sidebar-section">Navigation</div>
    <a href="{% url 'dashboard' %}" class="sidebar-link {% if request.resolver_match.url_name == 'dashboard' %}active{% endif %}">
        <i class="bi bi-grid-1x2"></i> Tableau de bord
    </a>
    <a href="{% url 'project_list' %}" class="sidebar-link {% if 'project' in request.resolver_match.url_name %}active{% endif %}">
        <i class="bi bi-folder2"></i> Projets
    </a>
    <a href="{% url 'statistics' %}" class="sidebar-link {% if request.resolver_match.url_name == 'statistics' %}active{% endif %}">
        <i class="bi bi-bar-chart"></i> Statistiques
    </a>
    <div class="sidebar-divider"></div>
    <div class="sidebar-section">Compte</div>
    <a href="{% url 'profile' %}" class="sidebar-link {% if request.resolver_match.url_name == 'profile' %}active{% endif %}">
        <i class="bi bi-person"></i> Mon Profil
    </a>
    {% if request.user.is_staff %}
    <a href="/admin/" class="sidebar-link">
        <i class="bi bi-shield-check"></i> Administration
    </a>
    {% endif %}
    <div class="sidebar-divider"></div>
    <a href="{% url 'logout' %}" class="sidebar-link">
        <i class="bi bi-box-arrow-right"></i> Déconnexion
    </a>
</aside>
templates/dashboard.html
Crée ce fichier :

html
{% extends 'base.html' %}
{% block title %}Tableau de bord{% endblock %}
{% block content %}

{% include 'partials/navbar.html' %}

<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">

        {% if messages %}
            {% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}">
                <i class="bi bi-info-circle"></i> {{ message }}
                <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
            </div>
            {% endfor %}
        {% endif %}

        <div class="page-header">
            <div>
                <p class="page-subtitle">Bonjour 👋</p>
                <h1 class="page-title">{{ request.user.get_full_name|default:request.user.username }}</h1>
            </div>
            <a href="{% url 'project_create' %}" class="btn btn-primary">
                <i class="bi bi-plus-lg"></i> Nouveau projet
            </a>
        </div>

        <div class="stat-grid">
            <div class="stat-card c1">
                <div class="stat-icon c1"><i class="bi bi-folder2"></i></div>
                <div class="stat-value">{{ total_projects }}</div>
                <div class="stat-label">Projets</div>
            </div>
            <div class="stat-card c2">
                <div class="stat-icon c2"><i class="bi bi-check2-circle"></i></div>
                <div class="stat-value">{{ done_tasks }}</div>
                <div class="stat-label">Tâches terminées</div>
            </div>
            <div class="stat-card c3">
                <div class="stat-icon c3"><i class="bi bi-list-check"></i></div>
                <div class="stat-value">{{ total_tasks }}</div>
                <div class="stat-label">Total tâches</div>
            </div>
            <div class="stat-card c4">
                <div class="stat-icon c4"><i class="bi bi-people"></i></div>
                <div class="stat-value">{{ my_projects.count }}</div>
                <div class="stat-label">Mes projets</div>
            </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
            <div class="card">
                <div class="card-header">
                    <span class="card-title"><i class="bi bi-folder2"></i> Mes projets récents</span>
                    <a href="{% url 'project_list' %}" class="btn btn-outline btn-sm">Voir tout</a>
                </div>
                <div class="card-body">
                    {% for project in my_projects|slice:":4" %}
                    <div style="display:flex;justify-content:space-between;align-items:center;padding:.65rem 0;border-bottom:1px solid var(--beige);">
                        <a href="{% url 'project_detail' project.pk %}" style="font-weight:600;color:var(--brown-dark);text-decoration:none;font-size:.9rem;">{{ project.name }}</a>
                        <span style="font-size:.78rem;color:var(--brown-pale);">{{ project.get_completion_rate }}%</span>
                    </div>
                    {% empty %}
                    <div class="empty-state" style="padding:2rem;">
                        <i class="bi bi-folder-plus"></i>
                        <p>Aucun projet</p>
                    </div>
                    {% endfor %}
                </div>
            </div>

            <div class="card">
                <div class="card-header">
                    <span class="card-title"><i class="bi bi-clipboard"></i> Mes tâches à venir</span>
                </div>
                <div class="card-body">
                    {% for task in my_tasks %}
                    <div class="task-card {% if task.is_overdue %}overdue{% endif %}" style="margin-bottom:.5rem;">
                        <div style="display:flex;justify-content:space-between;">
                            <span class="task-title">{{ task.title }}</span>
                            <span class="badge badge-{{ task.status }}">{{ task.get_status_display }}</span>
                        </div>
                        <div class="task-meta">
                            <span><i class="bi bi-folder2"></i> {{ task.project.name }}</span>
                            {% if task.due_date %}
                            <span><i class="bi bi-calendar3"></i> {{ task.due_date|date:"d/m/Y" }}</span>
                            {% endif %}
                        </div>
                    </div>
                    {% empty %}
                    <div class="empty-state" style="padding:2rem;">
                        <i class="bi bi-clipboard"></i>
                        <p>Aucune tâche assignée</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>

    </main>
</div>

{% endblock %}
templates/users/login.html
html
{% extends 'base.html' %}
{% block title %}Connexion{% endblock %}
{% block content %}
<div class="auth-wrapper">
    <div class="auth-card">
        <div class="auth-card-header">
            <div class="auth-logo">E</div>
            <h2>ESMT Tasks</h2>
            <p>Connectez-vous à votre espace</p>
        </div>
        <div class="auth-card-body">
            {% if messages %}{% for message in messages %}
            <div class="alert alert-{{ message.tags|default:'info' }}" style="margin-bottom:1rem;">{{ message }}</div>
            {% endfor %}{% endif %}
            <form method="post">
                {% csrf_token %}
                <div class="form-group">
                    <label class="form-label">Nom d'utilisateur</label>
                    <input type="text" name="username" placeholder="Votre identifiant" required>
                </div>
                <div class="form-group">
                    <label class="form-label">Mot de passe</label>
                    <input type="password" name="password" placeholder="••••••••" required>
                </div>
                <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;padding:.75rem;">
                    <i class="bi bi-box-arrow-in-right"></i> Se connecter
                </button>
            </form>
            <p style="text-align:center;margin-top:1.5rem;font-size:.875rem;color:var(--brown-pale);">
                Pas encore de compte ? <a href="{% url 'register' %}" class="auth-link">S'inscrire</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
templates/users/register.html
html
{% extends 'base.html' %}
{% block title %}Inscription{% endblock %}
{% block content %}
<div class="auth-wrapper">
    <div class="auth-card">
        <div class="auth-card-header">
            <div class="auth-logo">E</div>
            <h2>Créer un compte</h2>
            <p>Rejoignez la plateforme ESMT</p>
        </div>
        <div class="auth-card-body">
            <form method="post">
                {% csrf_token %}
                {% for field in form %}
                <div class="form-group">
                    <label class="form-label">{{ field.label }}</label>
                    {{ field }}
                    {% if field.errors %}<div class="errorlist">{{ field.errors|join:", " }}</div>{% endif %}
                </div>
                {% endfor %}
                <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;padding:.75rem;">
                    <i class="bi bi-check-circle"></i> Créer mon compte
                </button>
            </form>
            <p style="text-align:center;margin-top:1.5rem;font-size:.875rem;color:var(--brown-pale);">
                Déjà un compte ? <a href="{% url 'login' %}" class="auth-link">Se connecter</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
templates/users/profile.html
html
{% extends 'base.html' %}
{% block title %}Mon Profil{% endblock %}
{% block content %}
{% include 'partials/navbar.html' %}
<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">
        {% if messages %}{% for message in messages %}
        <div class="alert alert-{{ message.tags|default:'info' }}">{{ message }}
            <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
        </div>
        {% endfor %}{% endif %}
        <div class="page-header">
            <div>
                <p class="page-subtitle">Paramètres</p>
                <h1 class="page-title">Mon Profil</h1>
            </div>
        </div>
        <div style="display:grid;grid-template-columns:280px 1fr;gap:1.5rem;">
            <div class="card" style="align-self:start;">
                <div class="card-body" style="text-align:center;padding:2rem;">
                    <div style="width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,var(--beige-dark),var(--brown-pale));display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:700;color:var(--brown-dark);margin:0 auto 1rem;">
                        {{ user.username.0|upper }}
                    </div>
                    <h4 style="font-family:'Cormorant Garamond',serif;color:var(--brown-dark);">{{ user.get_full_name|default:user.username }}</h4>
                    <span class="role-badge {{ user.role }}" style="margin-top:.3rem;display:inline-block;">{{ user.get_role_display }}</span>
                    <p style="font-size:.85rem;color:var(--brown-pale);margin-top:.5rem;">{{ user.email }}</p>
                </div>
            </div>
            <div class="card">
                <div class="card-header"><span class="card-title">Modifier mes informations</span></div>
                <div class="card-body">
                    <form method="post" enctype="multipart/form-data">
                        {% csrf_token %}
                        {% for field in form %}
                        <div class="form-group">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}<div class="errorlist">{{ field.errors|join:", " }}</div>{% endif %}
                        </div>
                        {% endfor %}
                        <button type="submit" class="btn btn-primary"><i class="bi bi-save"></i> Sauvegarder</button>
                    </form>
                </div>
            </div>
        </div>
    </main>
</div>
{% endblock %}
templates/projects/list.html
html
{% extends 'base.html' %}
{% block title %}Projets{% endblock %}
{% block content %}
{% include 'partials/navbar.html' %}
<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">
        {% if messages %}{% for message in messages %}
        <div class="alert alert-{{ message.tags|default:'info' }}">{{ message }}
            <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
        </div>
        {% endfor %}{% endif %}
        <div class="page-header">
            <div>
                <p class="page-subtitle">Gestion</p>
                <h1 class="page-title">Mes Projets</h1>
            </div>
            <a href="{% url 'project_create' %}" class="btn btn-primary"><i class="bi bi-plus-lg"></i> Nouveau projet</a>
        </div>
        {% if my_projects %}
        <p style="font-size:.8rem;font-weight:700;text-transform:uppercase;color:var(--brown-pale);margin-bottom:1rem;">Projets créés par moi</p>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.25rem;margin-bottom:2rem;">
            {% for project in my_projects %}
            <div class="project-card">
                <div style="padding:1.25rem;">
                    <a href="{% url 'project_detail' project.pk %}" class="project-name">{{ project.name }}</a>
                    <p style="font-size:.82rem;color:var(--brown-pale);">{{ project.description|truncatewords:12 }}</p>
                </div>
                <div class="progress-wrap">
                    <div class="progress-fill {% if project.get_completion_rate >= 80 %}high{% endif %}" style="width:{{ project.get_completion_rate }}%"></div>
                </div>
                <div style="display:flex;gap:1rem;padding:.7rem 1.25rem;border-top:1px solid var(--beige);font-size:.79rem;color:var(--gray-600);">
                    <span><i class="bi bi-people"></i> {{ project.members.count }}</span>
                    <span><i class="bi bi-list-check"></i> {{ project.tasks.count }}</span>
                    <span style="margin-left:auto;font-weight:700;color:var(--brown-dark);">{{ project.get_completion_rate }}%</span>
                </div>
                <div style="padding:.75rem 1.25rem;border-top:1px solid var(--beige);display:flex;gap:.5rem;background:var(--beige-light);">
                    <a href="{% url 'project_detail' project.pk %}" class="btn btn-primary btn-sm">Voir</a>
                    <a href="{% url 'project_edit' project.pk %}" class="btn btn-outline btn-sm">Modifier</a>
                    <a href="{% url 'project_delete' project.pk %}" class="btn btn-danger btn-sm"><i class="bi bi-trash"></i></a>
                </div>
            </div>
            {% endfor %}
        </div>
        {% endif %}
        {% if member_projects %}
        <p style="font-size:.8rem;font-weight:700;text-transform:uppercase;color:var(--brown-pale);margin-bottom:1rem;">Projets auxquels je participe</p>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.25rem;">
            {% for project in member_projects %}
            <div class="project-card">
                <div style="padding:1.25rem;">
                    <a href="{% url 'project_detail' project.pk %}" class="project-name">{{ project.name }}</a>
                    <p style="font-size:.8rem;color:var(--brown-pale);"><i class="bi bi-person"></i> {{ project.created_by.username }}</p>
                </div>
                <div style="padding:.75rem 1.25rem;border-top:1px solid var(--beige);background:var(--beige-light);">
                    <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline btn-sm" style="width:100%;justify-content:center;">Voir le projet</a>
                </div>
            </div>
            {% endfor %}
        </div>
        {% endif %}
        {% if not my_projects and not member_projects %}
        <div class="empty-state">
            <i class="bi bi-folder-plus"></i>
            <h4>Aucun projet</h4>
            <p>Créez votre premier projet</p>
            <a href="{% url 'project_create' %}" class="btn btn-primary"><i class="bi bi-plus"></i> Créer un projet</a>
        </div>
        {% endif %}
    </main>
</div>
{% endblock %}
templates/projects/form.html
html
{% extends 'base.html' %}
{% block title %}{{ action }} un projet{% endblock %}
{% block content %}
{% include 'partials/navbar.html' %}
<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">
        <div style="max-width:600px;">
            <div class="page-header">
                <div>
                    <p class="page-subtitle">Formulaire</p>
                    <h1 class="page-title">{{ action }} un projet</h1>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        {% for field in form %}
                        <div class="form-group">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}<div class="errorlist">{{ field.errors|join:", " }}</div>{% endif %}
                        </div>
                        {% endfor %}
                        <div style="display:flex;gap:.75rem;margin-top:1.5rem;">
                            <button type="submit" class="btn btn-primary"><i class="bi bi-save"></i> {{ action }}</button>
                            <a href="{% url 'project_list' %}" class="btn btn-outline">Annuler</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </main>
</div>
{% endblock %}
templates/projects/detail.html
html
{% extends 'base.html' %}
{% block title %}{{ project.name }}{% endblock %}
{% block content %}
{% include 'partials/navbar.html' %}
<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">
        {% if messages %}{% for message in messages %}
        <div class="alert alert-{{ message.tags|default:'info' }}">{{ message }}
            <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
        </div>
        {% endfor %}{% endif %}
        <div class="page-header">
            <div>
                <p class="page-subtitle">Projet</p>
                <h1 class="page-title">{{ project.name }}</h1>
                {% if project.description %}<p style="color:var(--brown-pale);margin-top:.3rem;">{{ project.description }}</p>{% endif %}
            </div>
            {% if is_creator %}
            <div style="display:flex;gap:.5rem;">
                <a href="{% url 'task_create' project.pk %}" class="btn btn-primary"><i class="bi bi-plus"></i> Ajouter tâche</a>
                <a href="{% url 'project_edit' project.pk %}" class="btn btn-outline"><i class="bi bi-pencil"></i></a>
            </div>
            {% endif %}
        </div>
        <div class="filter-bar">
            <span class="filter-label">Filtrer :</span>
            <form method="get" style="display:flex;gap:.75rem;align-items:center;">
                <select name="status" class="filter-select" onchange="this.form.submit()">
                    <option value="">Tous les statuts</option>
                    <option value="a_faire" {% if status_filter == 'a_faire' %}selected{% endif %}>À faire</option>
                    <option value="en_cours" {% if status_filter == 'en_cours' %}selected{% endif %}>En cours</option>
                    <option value="termine" {% if status_filter == 'termine' %}selected{% endif %}>Terminé</option>
                </select>
                {% if status_filter %}<a href="{% url 'project_detail' project.pk %}" class="btn btn-outline btn-sm">✕</a>{% endif %}
            </form>
        </div>
        {% if tasks %}
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;">
            {% for task in tasks %}
            <div class="task-card {% if task.is_overdue %}overdue{% endif %}">
                <div style="display:flex;justify-content:space-between;gap:.5rem;">
                    <span class="task-title">{{ task.title }}</span>
                    <span class="badge badge-{{ task.status }}">{{ task.get_status_display }}</span>
                </div>
                {% if task.description %}<p style="font-size:.82rem;color:var(--brown-pale);margin:.3rem 0;">{{ task.description|truncatewords:10 }}</p>{% endif %}
                <div class="task-meta">
                    {% if task.assigned_to %}<span><i class="bi bi-person"></i> {{ task.assigned_to.username }}</span>{% endif %}
                    {% if task.due_date %}<span><i class="bi bi-calendar3"></i> {{ task.due_date|date:"d/m/Y" }}{% if task.is_overdue %} ⚠️{% endif %}</span>{% endif %}
                </div>
                {% if is_creator or task.assigned_to == request.user %}
                <div style="display:flex;gap:.5rem;margin-top:.75rem;padding-top:.75rem;border-top:1px solid var(--beige);">
                    <a href="{% url 'task_update' task.pk %}" class="btn btn-outline btn-sm"><i class="bi bi-pencil"></i> Modifier</a>
                    {% if is_creator %}<a href="{% url 'task_delete' task.pk %}" class="btn btn-danger btn-sm" onclick="return confirm('Supprimer ?')"><i class="bi bi-trash"></i></a>{% endif %}
                </div>
                {% endif %}
            </div>
            {% endfor %}
        </div>
        {% else %}
        <div class="empty-state">
            <i class="bi bi-clipboard"></i>
            <h4>Aucune tâche</h4>
            {% if is_creator %}<a href="{% url 'task_create' project.pk %}" class="btn btn-primary"><i class="bi bi-plus"></i> Créer une tâche</a>{% endif %}
        </div>
        {% endif %}
    </main>
</div>
{% endblock %}
templates/projects/confirm_delete.html
html
{% extends 'base.html' %}
{% block title %}Supprimer{% endblock %}
{% block content %}
{% include 'partials/navbar.html' %}
<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">
        <div style="max-width:480px;margin:3rem auto;">
            <div class="card" style="border-top:3px solid var(--red);">
                <div class="card-body" style="text-align:center;padding:2.5rem;">
                    <i class="bi bi-exclamation-triangle" style="font-size:3rem;color:var(--red);opacity:.7;display:block;margin-bottom:1rem;"></i>
                    <h3 style="font-family:'Cormorant Garamond',serif;color:var(--brown-dark);margin-bottom:.75rem;">Supprimer ce projet ?</h3>
                    <p style="color:var(--brown-pale);margin-bottom:.5rem;">Vous allez supprimer <strong>{{ project.name }}</strong></p>
                    <p style="color:var(--red);font-size:.85rem;margin-bottom:2rem;">⚠️ Toutes les tâches associées seront supprimées !</p>
                    <form method="post" style="display:flex;gap:.75rem;justify-content:center;">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-danger"><i class="bi bi-trash"></i> Oui, supprimer</button>
                        <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline">Annuler</a>
                    </form>
                </div>
            </div>
        </div>
    </main>
</div>
{% endblock %}
templates/tasks/form.html
html
{% extends 'base.html' %}
{% block title %}{{ action }} une tâche{% endblock %}
{% block content %}
{% include 'partials/navbar.html' %}
<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">
        <div style="max-width:600px;">
            <div class="page-header">
                <div>
                    <p class="page-subtitle">Formulaire</p>
                    <h1 class="page-title">{{ action }} une tâche</h1>
                </div>
            </div>
            <div class="card">
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        {% for field in form %}
                        <div class="form-group">
                            <label class="form-label">{{ field.label }}</label>
                            {{ field }}
                            {% if field.errors %}<div class="errorlist">{{ field.errors|join:", " }}</div>{% endif %}
                        </div>
                        {% endfor %}
                        <div style="display:flex;gap:.75rem;margin-top:1.5rem;">
                            <button type="submit" class="btn btn-primary"><i class="bi bi-save"></i> {{ action }}</button>
                            <a href="{% url 'project_detail' project.pk %}" class="btn btn-outline">Annuler</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </main>
</div>
{% endblock %}
templates/tasks/statistics.html
html
{% extends 'base.html' %}
{% block title %}Statistiques{% endblock %}
{% block content %}
{% include 'partials/navbar.html' %}
<div class="app-layout">
    {% include 'partials/sidebar.html' %}
    <main class="main-content">
        <div class="page-header">
            <div>
                <p class="page-subtitle">Analyse</p>
                <h1 class="page-title">Statistiques & Primes</h1>
            </div>
        </div>
        <div class="card" style="margin-bottom:1.5rem;">
            <div class="card-header"><span class="card-title"><i class="bi bi-calendar3"></i> Mes statistiques {{ year }}</span></div>
            <div class="card-body">
                <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;">
                    {% for q in quarterly_stats %}
                    <div style="text-align:center;padding:1.25rem;border-radius:var(--radius);border:1.5px solid var(--beige-dark);">
                        <div style="font-size:.75rem;font-weight:700;text-transform:uppercase;color:var(--brown-pale);margin-bottom:.5rem;">{{ q.quarter }}</div>
                        <div style="font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:700;color:var(--brown-dark);">{{ q.rate }}%</div>
                        <div style="font-size:.78rem;color:var(--brown-pale);margin:.3rem 0;">{{ q.on_time }}/{{ q.total }} dans les délais</div>
                        {% if q.rate == 100 %}
                        <span style="background:#d8eddf;color:#2f6b45;padding:.2rem .6rem;border-radius:20px;font-size:.72rem;font-weight:600;">🏆 100 000 FCFA</span>
                        {% elif q.rate >= 90 %}
                        <span style="background:#f5ecd8;color:#7a5010;padding:.2rem .6rem;border-radius:20px;font-size:.72rem;font-weight:600;">⭐ 30 000 FCFA</span>
                        {% else %}
                        <span style="background:var(--beige);color:var(--brown-pale);padding:.2rem .6rem;border-radius:20px;font-size:.72rem;">Pas de prime</span>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
        {% if evaluations %}
        <div class="card">
            <div class="card-header"><span class="card-title"><i class="bi bi-award"></i> Évaluations Professeurs — {{ year }}</span></div>
            <div class="table-container">
                <table>
                    <thead>
                        <tr><th>Professeur</th><th>Tâches</th><th>Dans les délais</th><th>Taux</th><th>Prime</th></tr>
                    </thead>
                    <tbody>
                        {% for eval in evaluations %}
                        <tr>
                            <td><strong>{{ eval.user.get_full_name|default:eval.user.username }}</strong></td>
                            <td>{{ eval.total }}</td>
                            <td>{{ eval.on_time }}</td>
                            <td>{{ eval.rate }}%</td>
                            <td>
                                {% if eval.prime == 100000 %}<span style="background:#d8eddf;color:#2f6b45;padding:.3rem .75rem;border-radius:20px;font-size:.8rem;font-weight:700;">🏆 100 000 FCFA</span>
                                {% elif eval.prime == 30000 %}<span style="background:#f5ecd8;color:#7a5010;padding:.3rem .75rem;border-radius:20px;font-size:.8rem;font-weight:700;">⭐ 30 000 FCFA</span>
                                {% else %}<span style="background:var(--beige);color:var(--brown-pale);padding:.3rem .75rem;border-radius:20px;">—</span>{% endif %}
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        {% endif %}
    </main>
</div>
{% endblock %}
Dernière étape — Migrations et lancement 🚀
Une fois tous les fichiers créés, dans PowerShell :

powershell
python manage.py makemigrations users
python manage.py makemigrations projects
python manage.py makemigrations tasks
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Dis-moi quand tu as tout copié et on fait les migrations ensemble ! 😊

j'ai tout copier

19:19
Parfait ! Lance les commandes une par une dans PowerShell :

powershell
python manage.py makemigrations users
Dis-moi le résultat ! 😊

d-----        12/03/2026     18:41                venv            
-a----        12/03/2026     18:43            685 manage.py       
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py makemigrations users
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py makemigrations projects
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py makemigrations tasks
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py migrate
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py migrate
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py createsuperuser                                                            
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py runserver                                                                 
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>

Afficher plus
19:21
Les commandes semblent s'être exécutées sans afficher de résultat, ce qui est bizarre. Vérifions :

powershell
python manage.py makemigrations users
```

Copie-colle **exactement** ce qui s'affiche après cette commande (les lignes de résultat). Normalement tu devrais voir quelque chose comme :
```
Migrations for 'users':
  users/migrations/0001_initial.py
    - Create model CustomUser
Si tu ne vois rien ou une erreur, dis-moi ! 😊

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py makemigrations users                                                      
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>

19:22
Ça veut dire que les migrations n'ont pas été créées. Le fichier users/models.py n'est probablement pas sauvegardé correctement.

Vérifions :

powershell
type users\models.py
Copie-colle ce qui s'affiche ! 😊

.py migrate
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py migrate
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py createsuperuser                                                            
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py runserver                                                                 
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py makemigrations users                                                      
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> type users\models.py
type : Impossible de trouver le chemin d'accès «
C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\users\models.py», car 
il n'existe pas.
Au caractère Ligne:1 : 1
+ type users\models.py
+ ~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\Des...users\models 
   .py:String) [Get-Content], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetC 
   ontentCommand

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>

Afficher plus
19:22
Le fichier users/models.py n'existe pas ! Les fichiers n'ont pas été sauvegardés au bon endroit. Vérifions ce qui existe vraiment :

powershell
dir users
Copie-colle le résultat ! 😊

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> dir users
dir : Impossible de trouver le chemin d'accès «
C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\users», car il 
n'existe pas.
Au caractère Ligne:1 : 1
+ dir users
+ ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\Des...\ProjetPy\us 
   ers:String) [Get-ChildItem], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetC 
   hildItemCommand

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>

Afficher plus
19:23
Le dossier users n'existe pas ! Vérifions ce qui est réellement dans le dossier :

powershell
dir
Copie-colle le résultat ! 😊

hildItemCommand

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> dir
dir : Impossible de trouver le chemin d'accès «
C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy», car il n'existe pas.
Au caractère Ligne:1 : 1
+ dir
+ ~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\Des...python\Proje 
   tPy:String) [Get-ChildItem], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetC 
   hildItemCommand

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>

Afficher plus
19:23
Le dossier ProjetPy n'existe plus ! On recommence depuis le début. Copie-colle ces commandes toutes en une fois :

powershell
cd "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python"
mkdir ProjetPy
cd ProjetPy
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow
django-admin startproject backend .
python manage.py startapp users
python manage.py startapp projects
python manage.py startapp tasks
mkdir templates
mkdir templates\users
mkdir templates\projects
mkdir templates\tasks
mkdir templates\partials
mkdir static
mkdir media
Dis-moi quand c'est fait ! 😊

Et cette fois on va immédiatement pousser sur GitHub avant de faire quoi que ce soit d'autre ! 🔒


(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py createsuperuser Traceback (most recent call last): File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\db\migrations\loader.py", line 189, in check_key return s

pasted

20:09
L'erreur dit que users n'a pas de migrations. Il faut d'abord faire les makemigrations dans le bon ordre :

powershell
python manage.py makemigrations users
python manage.py makemigrations projects
python manage.py makemigrations tasks
python manage.py migrate
Copie-colle le résultat de chaque commande ! 😊

e "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\venv\Lib\site-packages\django\db\migrations\loader.py", line 196, in check_key
    raise ValueError(
        "Dependency on app with no migrations: %s" % key[0]
    )
ValueError: Dependency on app with no migrations: users            python manage.py makemigrations users
Migrations for 'users':esktop\Cours-Semestre1-DAR\python\ProjetPy> 
  users\migrations\0001_initial.py
    + Create model CustomUser
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py makemigrations projects
Migrations for 'projects':
  projects\migrations\0001_initial.py
    + Create model Project
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py makemigrations tasks
Migrations for 'tasks':
  tasks\migrations\0001_initial.py
    + Create model PrimeEvaluation
    + Create model Task
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, projects, sessions, tasks, users
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying users.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying projects.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying tasks.0001_initial... OK

Afficher plus
20:09
Parfait, tout est migré ! 🎉 Maintenant crée le superuser :

powershell
python manage.py createsuperuser
```

Utilise ces informations :
```
Username : admin
Email : admin@esmt.sn
Password : Admin1234!
Dis-moi quand c'est fait ! 😊

gain): 
Superuser created successfully.
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> 
`` : Le terme «``» n'est pas reconnu comme nom d'applet de commande, fonction, fichier de script ou programme exécutable. Vérifiez l'orthographe 
du nom, ou si un chemin d'accès existe, vérifiez que le chemin d'accès est correct et réessayez.
Au caractère Ligne:1 : 1
+ 
+ ~~~
    + CategoryInfo          : ObjectNotFound: (``:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> 
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> Utilise ces informations :
Utilise : Le terme «Utilise» n'est pas reconnu comme nom d'applet de commande, fonction, fichier de script ou programme exécutable. Vérifiez 
l'orthographe du nom, ou si un chemin d'accès existe, vérifiez que le chemin d'accès est correct et réessayez.
Au caractère Ligne:1 : 1
+ Utilise ces informations :
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (Utilise:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> 
`` : Le terme «``» n'est pas reconnu comme nom d'applet de commande, fonction, fichier de script ou programme exécutable. Vérifiez l'orthographe 
du nom, ou si un chemin d'accès existe, vérifiez que le chemin d'accès est correct et réessayez.
Au caractère Ligne:1 : 1
+ 
+ ~~~
    + CategoryInfo          : ObjectNotFound: (``:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> Username : admin
Username : Le terme «Username» n'est pas reconnu comme nom d'applet de commande, fonction, fichier de script ou programme exécutable. Vérifiez 
l'orthographe du nom, ou si un chemin d'accès existe, vérifiez que le chemin d'accès est correct et réessayez.
Au caractère Ligne:1 : 1
+ Username : admin
+ ~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (Username:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> Email : admin@esmt.sn
Email : Le terme «Email» n'est pas reconnu comme nom d'applet de commande, fonction, fichier de script ou programme exécutable. Vérifiez 
l'orthographe du nom, ou si un chemin d'accès existe, vérifiez que le chemin d'accès est correct et réessayez.
Au caractère Ligne:1 : 1
+ Email : admin@esmt.sn
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (Email:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> Password : Admin1234!

Afficher plus
20:11
😄 Tu as copié mes instructions dans le terminal ! Pas de souci, le superuser a déjà été créé avec succès — j'ai vu "Superuser created successfully" !

Maintenant lance le serveur :

powershell
python manage.py runserver
Puis ouvre http://127.0.0.1:8000 dans ton navigateur et dis-moi ce que tu vois ! 😊

On me dit identifiants incorrect

20:13
C'est normal, il faut d'abord créer un compte utilisateur normal via /register/. Le superuser admin est uniquement pour /admin/.

Va sur http://127.0.0.1:8000/register/ et crée un compte :

Username : Fadhima
Email : fadhima@esmt.sn
Password : Admin1234!
Role : Étudiant
Dis-moi quand c'est fait ! 😊

Connectez-vous à votre espace
Identifiants incorrects.
Nom d'utilisateur
Mot de passe
Se connecter

20:15
Le compte a été créé mais la connexion échoue. Essaie avec le superuser directement :

Username : admin
Password : Admin1234!
Si ça ne marche pas non plus, dis-moi et on va vérifier la vue login_view dans users/views.py. 😊

JE PEUX MOFIFIER PARCE QUE RIEN NE MARCHE

20:22
Pas de panique ! 😊 Le problème est dans users/views.py.

Ouvre users/views.py dans PyCharm, Ctrl+A → Suppr, et colle ceci :

python
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
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
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
Ctrl+S, puis va sur http://127.0.0.1:8000/register/ et crée un nouveau compte. Dis-moi ce qui se passe ! 😊

Je n'ai pas compris

20:23
Pas de souci ! Voici étape par étape 😊

Étape 1 — Dans PyCharm
Regarde le panneau à gauche de PyCharm
Clique sur le dossier users
Double-clique sur le fichier views.py
Étape 2 — Remplacer le contenu
Fais Ctrl+A (sélectionne tout)
Fais Suppr (efface tout)
Colle le nouveau code que je t'ai donné au-dessus
Fais Ctrl+S (sauvegarde)
Étape 3 — Tester
Va sur http://127.0.0.1:8000/register/ dans ton navigateur et crée un compte.

Dis-moi où tu bloques exactement :

s PowerShell Copyright (C) Microsoft Corporation. Tous droits réservés.  Installez la dernière version de PowerShell pour de nouvelles fonctionnalités et améliorations ! https://aka.ms/PSWindows  (.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python> python manage.py runserver C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\PythonProject\.venv/Scripts\python.exe: can't open file 'C:\\Users\\HP\\Desktop\\Cours-Semestre1-DAR\\python\\manage.py': [Errno 2] No such file or directory (.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python> python manage.py runserver C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\PythonProject\.venv/Scripts\python.exe: can't open file 'C:\\Users\\HP\\Desktop\\Cours-Semestre1-DAR\\python\\manage.py': [Errno 2] No such file or directory (.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python> python manage.py runserver C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\PythonProject\.venv/Scripts\python.exe: can't open file 'C:\\Users\\HP\\Desktop\\Cours-Semestre1-DAR\\python\\manage.py': [Errno 2] No such file or directory (.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python>  (.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python>

Afficher plus
20:29
Tu es dans le mauvais dossier ! Tape exactement ceci :

powershell
cd "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy"
python manage.py runserver
Le problème c'est que tu es dans python\ au lieu de python\ProjetPy\ 😊

\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\manage.py", line 11, in main                                          
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\manage.py", line 22, in <module>                                      
    main()
    ~~~~^^
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\manage.py", line 13, in main                                          
    raise ImportError(
    ...<3 lines>...
    ) from exc
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?                                
(.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy> python manage.py runserver
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\manage.py", line 11, in main                                          
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\manage.py", line 22, in <module>                                      
    main()
    ~~~~^^
  File "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy\manage.py", line 13, in main                                          
    raise ImportError(
    ...<3 lines>...
    ) from exc
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?                                
(.venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR

Afficher plus
20:29
Le venv n'est pas activé ! Tape ces deux commandes :

powershell
venv\Scripts\activate
python manage.py runserver
Tu dois voir (venv) au début de la ligne avant de lancer le serveur 😊

Je n'arrive toujourrs pas a me connecter

20:30
Ok, le serveur tourne ! Maintenant dis-moi exactement ce qui se passe :

Q : Qu'est-ce qui se passe exactement ?
R : Autre

20:31
Décris-moi exactement ce que tu vois sur l'écran en ce moment — une capture d'écran ou quelques mots suffisent 😊

20:31
La page est magnifique ! 🎨 Le problème c'est que le compte Fadhima n'existe plus — c'est un nouveau projet, nouvelle base de données.

Va sur http://127.0.0.1:8000/register/ pour créer un nouveau compte, puis connecte-toi avec ce compte. 😊

J e ne peux pas me connecter en admin?

20:34
Si ! Essaie avec :

Nom d'utilisateur : admin
Mot de passe : Admin1234!
Si ça ne marche pas, c'est parce que le superuser admin a été créé avec l'ancien projet supprimé. Il faut en recréer un.

Dans PowerShell, arrête le serveur avec Ctrl+C puis :

powershell
python manage.py createsuperuser
```

Mets :
```
Username : admin
Email : admin@esmt.sn
Password : Admin1234!
Puis relance :

powershell
python manage.py runserver
Et connecte-toi avec admin / Admin1234! 😊

jentre ces info ou

20:37
Dans le terminal PowerShell ! Quand tu tapes python manage.py createsuperuser, Django va te poser des questions directement dans le terminal :

Username (leave blank to use 'hp'): admin        ← tape admin puis Entrée
Email address: admin@esmt.sn                      ← tape l'email puis Entrée
Password: Admin1234!                              ← tape le mot de passe (invisible) puis Entrée
Password (again): Admin1234!                      ← retape le mot de passe puis Entrée
Tu verras "Superuser created successfully" 😊

oui cest fait cest pour pouvoir me connecter en admin

20:37
Super ! Maintenant connecte-toi sur http://127.0.0.1:8000/login/ avec :

Nom d'utilisateur : admin
Mot de passe : Admin1234!
Dis-moi ce qui se passe ! 😊

identifiants incorrects

20:39
Le problème vient du fait que le superuser ne peut pas se connecter via la page login normale car son role n'est pas défini.

Essaie plutôt de te connecter via l'interface admin :

http://127.0.0.1:8000/admin/

Avec :

Nom d'utilisateur : admin
Mot de passe : Admin1234!
Dis-moi si ça marche ! 😊

20:41
Tu essaies avec Fadhima mais ce compte n'existe plus ! Utilise admin :

Nom d'utilisateur : admin
Mot de passe : Admin1234!
⚠️ Attention aux majuscules — admin en minuscules ! 😊

tjrs rien

20:42
Le superuser a peut-être été créé avec un mauvais mot de passe. On va le réinitialiser.

Dans PowerShell, Ctrl+C pour arrêter le serveur, puis :

powershell
python manage.py shell
Puis dans le shell Python qui s'ouvre, tape exactement :

python
from django.contrib.auth import get_user_model
User = get_user_model()
u = User.objects.get(username='admin')
u.set_password('Admin1234!')
u.save()
exit()
Puis relance le serveur :

powershell
python manage.py runserver
Et essaie de te connecter sur http://127.0.0.1:8000/admin/ avec admin / Admin1234! 😊

r

20:45
Dis-moi exactement ce qui s'affiche après avoir tapé ces commandes dans le shell ! 😊


Cahier des Charges : Application de Gestion des Tâches Collaboratives Contexte Votre mission consiste à développer une application web pour gérer des tâches dans un environnement collaboratif je préfère dire que l’application sera orientée ESMT pour les enseignants et étudiants). Chaque utilisa

pasted

Peux tu verifier si le travail qu'on a fait est correct

21:09
J'ai relu le cahier des charges. Voici ce qu'on a fait et ce qui manque :

✅ Ce qui est fait
Gestion des utilisateurs

Inscription, connexion, déconnexion
Profils avec avatar, email, nom, rôle (étudiant/professeur)
Gestion des projets

Créer, modifier, supprimer un projet
Ajouter des membres
Gestion des tâches

Titre, description, date limite, statut, utilisateur assigné
Filtres par statut
Étudiants ne peuvent pas assigner un professeur
Permissions

Seul le créateur peut ajouter/supprimer des tâches
Les assignés peuvent modifier leurs tâches
Statistiques & Primes

Statistiques trimestrielles et annuelles
Prime 30 000 FCFA (90%+) et 100 000 FCFA (100%)
API REST

DRF + JWT configurés
Toutes les routes API créées
⚠️ Ce qui manque encore
Priorité haute :

🔴 Connexion qui ne fonctionne pas encore — à régler maintenant
🔴 Tests unitaires avec pytest-django
🔴 GitHub/GitLab
Priorité normale :

🟡 Mise à jour du mot de passe dans le profil
🟡 README complet
🚀 Priorité immédiate
On règle d'abord le problème de connexion. Dans PowerShell :

powershell
python manage.py shell
Puis tape :

python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.all().values('username', 'is_active', 'is_staff')
Copie-colle le résultat ! 😊

c bon

21:11
🎉 Tu es connectée ? Qu'est-ce que tu vois à l'écran ? Envoie une capture d'écran ! 😊

sa sert a quoi ca

21:13
C'est pour voir la liste des utilisateurs créés dans la base de données — ça nous aide à comprendre pourquoi la connexion ne marche pas.

Copie-colle le résultat qui s'affiche après avoir tapé cette commande ! 😊

mais on a pas creer de bd

21:14
Si ! Django crée automatiquement la base de données SQLite (db.sqlite3) quand tu fais python manage.py migrate. Elle existe déjà dans ton dossier ProjetPy.

Tape cette commande dans le shell Python :

python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.all().values('username', 'is_active', 'is_staff')
Dis-moi ce qui s'affiche ! 😊

on.
(InteractiveConsole)
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> User.objects.all().values('username', 'is_active', 'is_staff')
<QuerySet [{'username': 'Fadima', 'is_active': True, 'is_staff': True}, {'username': 'Fatou', 'is_active': True, 'is_staff': False}, {'username': 'ProfesseurBah', 'is_active': True, 'is_staff': False}, {'username': 'admin', 'is_active': True, 'is_staff': True}]>
>>> exit()
now exiting InteractiveConsole...
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>python manage.py runserver                                          
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
March 12, 2026 - 21:12:27
Django version 6.0.3, using settings 'backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
[12/Mar/2026 21:12:29] "GET / HTTP/1.1" 200 17269
[12/Mar/2026 21:12:33] "GET / HTTP/1.1" 200 17269
[12/Mar/2026 21:12:35] "GET /projects/ HTTP/1.1" 200 15284
[12/Mar/2026 21:12:37] "GET /tasks/statistics/ HTTP/1.1" 200 18475
[12/Mar/2026 21:12:42] "GET /logout/ HTTP/1.1" 302 0
[12/Mar/2026 21:12:42] "GET /login/ HTTP/1.1" 200 14685
[12/Mar/2026 21:12:45] "POST /login/ HTTP/1.1" 302 0
[12/Mar/2026 21:12:45] "GET / HTTP/1.1" 200 17269

Afficher plus
21:14
🎉 Ça marche !!! Tu es connectée !

Je vois dans les logs :

POST /login/ HTTP/1.1" 302 → connexion réussie !
GET / HTTP/1.1" 200 → tableau de bord chargé !
Et tu as déjà 4 utilisateurs créés : Fadima, Fatou, ProfesseurBah, admin

Envoie une capture d'écran de ce que tu vois dans le navigateur ! 😊

quel navigateur

21:16
Le navigateur que tu utilises habituellement — Microsoft Edge, Chrome, Firefox...

Ouvre-le et va sur :

http://127.0.0.1:8000
Dis-moi ce que tu vois ! 😊

21:17
🎉🎉🎉 C'EST MAGNIFIQUE !!! ÇA MARCHE PARFAITEMENT !!!

Le tableau de bord est superbe avec :

✅ La navbar avec ProfesseurBah et son badge PROFESSEUR
✅ La sidebar avec Navigation et Compte
✅ Les 4 cartes de statistiques
✅ Mes projets récents et Mes tâches à venir
✅ Le bouton Nouveau projet
✅ Le thème beige/marron 🍂
🚀 Prochaines étapes
Maintenant on va :

Tester toutes les fonctionnalités — crée un projet, ajoute des tâches
Pousser sur GitHub pour ne plus jamais perdre le code
Faire le README
On commence par GitHub pour sécuriser le travail. Dans PowerShell (Ctrl+C d'abord pour arrêter le serveur) :

powershell
cd "C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy"
git init
git add .
git commit -m "Initial commit - ESMT Tasks App"
Dis-moi quand c'est fait ! 😊

OUI APRES

21:19
Super ! Maintenant on pousse sur GitHub 🔒

Étape 1 — Créer le dépôt sur GitHub
Va sur https://github.com
Connecte-toi ou crée un compte
Clique sur le bouton vert "New" ou "+" en haut à droite
Remplis :
Repository name : esmt-tasks
Visibility : Public
⚠️ NE PAS cocher "Add README"
Clique "Create repository"
Dis-moi quand le dépôt est créé ! 😊

c fait

21:23
Parfait ! Maintenant copie l'URL de ton dépôt GitHub. Elle ressemble à :

https://github.com/TON_USERNAME/esmt-tasks.git
Tu la trouves sur la page GitHub qui vient de s'ouvrir après la création. Copie-colle l'URL ici ! 😊

oui

21:24
Copie-colle l'URL exacte ici (elle commence par https://github.com/...) 😊

https://github.com/FadhimaAmadouBah/esmt-tasks.git

21:24
Parfait ! Maintenant tape ces commandes dans PowerShell :

powershell
git remote add origin https://github.com/FadhimaAmadouBah/esmt-tasks.git
git branch -M main
git push -u origin main
GitHub va te demander ton username et mot de passe GitHub. Dis-moi quand c'est fait ! 😊

non mais sa a marcher

21:26
🎉 Excellent ! Ton code est maintenant sur GitHub !

Va vérifier sur https://github.com/FadhimaAmadouBah/esmt-tasks — tu dois voir tous tes fichiers ! 😊

Récapitulatif de ce qui est fait ✅
✅ Code sur GitHub — sécurisé !
✅ Tableau de bord fonctionnel
✅ Connexion/Inscription
✅ Thème beige/marron
✅ API REST + JWT
✅ Statistiques & Primes
Prochaines étapes 🚀
Tester — crée un projet et des tâches
README.md — documentation
Tests unitaires — pytest-django
On teste l'application maintenant ? Relance le serveur :

powershell
python manage.py runserver
Et crée un projet sur http://127.0.0.1:8000/projects/create/ 😊

1

21:27
Super, on teste ! 🎉

Va sur http://127.0.0.1:8000/projects/create/ et crée un projet :

Nom : Projet Web ESMT
Description : Application de gestion des tâches
Membres : sélectionne Fatou et ProfesseurBah
Clique Créer et dis-moi ce qui se passe ! 😊

SA MARCHE

21:27
🎉🎉🎉 FÉLICITATIONS !!!

Maintenant teste le reste :

1️⃣ Créer une tâche
Clique sur ton projet Projet Web ESMT
Clique Ajouter tâche
Remplis :
Titre : Créer la page d'accueil
Assigné à : Fatou
Statut : À faire
Priorité : Haute
Date limite : 20/03/2026
2️⃣ Changer le statut
Clique Modifier sur la tâche
Change le statut en En cours
3️⃣ Voir les statistiques
Clique sur Statistiques dans la sidebar
Dis-moi si tout fonctionne ! 😊

L es tests je les ferai fesont le point 2 MTN

21:28
📄 README.md
Crée un fichier README.md à la racine de ProjetPy/ dans PyCharm et colle ceci :

markdown
# 📋 ESMT Tasks — Application de Gestion des Tâches Collaboratives

Application web développée pour l'ESMT permettant aux enseignants et étudiants 
de gérer des projets et tâches collaboratives, avec un système d'évaluation 
et de primes pour les professeurs.

---

## 🚀 Technologies utilisées

| Technologie | Rôle |
|---|---|
| Python 3.13 | Langage principal |
| Django 6.0 | Framework backend |
| Django REST Framework | API RESTful |
| SQLite | Base de données |
| JWT (SimpleJWT) | Authentification API |
| HTML/CSS/JS | Frontend (templates Django) |

---

## ⚙️ Installation et configuration

### 1. Prérequis
- Python 3.10+
- pip
- Git

### 2. Cloner le projet
```bash
git clone https://github.com/FadhimaAmadouBah/esmt-tasks.git
cd esmt-tasks
```

### 3. Créer l'environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Installer les dépendances
```bash
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow
```

### 5. Appliquer les migrations
```bash
python manage.py makemigrations users
python manage.py makemigrations projects
python manage.py makemigrations tasks
python manage.py migrate
```

### 6. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur
```bash
python manage.py runserver
```

### 8. Accéder à l'application
- Interface web : http://127.0.0.1:8000
- Administration : http://127.0.0.1:8000/admin
- API : http://127.0.0.1:8000/api/

---

## 👥 Profils utilisateurs

| Profil | Permissions |
|---|---|
| **Étudiant** | Créer projets, gérer ses tâches, ne peut pas assigner un professeur |
| **Professeur** | Créer projets, assigner des tâches, voir ses statistiques et primes |
| **Admin** | Accès total, gestion des utilisateurs |

---

## 🏆 Système de primes

| Taux de complétion | Prime |
|---|---|
| 100% dans les délais | **100 000 FCFA** |
| 90% à 99% dans les délais | **30 000 FCFA** |
| Moins de 90% | Pas de prime |

---

## 🗃️ Modèles de données

### CustomUser
| Champ | Type | Description |
|---|---|---|
| username | CharField | Nom d'utilisateur |
| email | EmailField | Adresse email |
| role | CharField | etudiant / professeur |
| avatar | ImageField | Photo de profil |
| bio | TextField | Biographie |

### Project
| Champ | Type | Description |
|---|---|---|
| name | CharField | Nom du projet |
| description | TextField | Description |
| created_by | ForeignKey | Créateur |
| members | ManyToManyField | Membres |

### Task
| Champ | Type | Description |
|---|---|---|
| title | CharField | Titre |
| project | ForeignKey | Projet associé |
| assigned_to | ForeignKey | Utilisateur assigné |
| status | CharField | a_faire / en_cours / termine |
| priority | CharField | basse / normale / haute / urgente |
| due_date | DateTimeField | Date limite |

### PrimeEvaluation
| Champ | Type | Description |
|---|---|---|
| professeur | ForeignKey | Professeur évalué |
| period | CharField | T1 / T2 / T3 / T4 / annuel |
| year | IntegerField | Année |
| completion_rate | FloatField | Taux de complétion |
| prime_amount | IntegerField | 0 / 30000 / 100000 |

---

## 🌐 Routes disponibles

### Pages Web

| URL | Description |
|---|---|
| `/` | Tableau de bord |
| `/login/` | Connexion |
| `/register/` | Inscription |
| `/profile/` | Mon profil |
| `/projects/` | Liste des projets |
| `/projects/create/` | Créer un projet |
| `/projects/<id>/` | Détail d'un projet |
| `/projects/<id>/edit/` | Modifier un projet |
| `/projects/<id>/delete/` | Supprimer un projet |
| `/tasks/create/<project_id>/` | Créer une tâche |
| `/tasks/<id>/edit/` | Modifier une tâche |
| `/tasks/<id>/delete/` | Supprimer une tâche |
| `/tasks/statistics/` | Statistiques et primes |
| `/admin/` | Administration |

### API REST

| Méthode | URL | Description |
|---|---|---|
| POST | `/api/auth/register/` | Créer un compte |
| POST | `/api/auth/login/` | Connexion JWT |
| POST | `/api/auth/refresh/` | Rafraîchir token |
| GET/PUT | `/api/users/me/` | Mon profil |
| GET | `/api/users/` | Liste utilisateurs |
| GET/POST | `/api/projects/` | Projets |
| GET/PUT/DELETE | `/api/projects/<id>/` | Détail projet |
| GET/POST | `/api/projects/<id>/tasks/` | Tâches du projet |
| GET/PUT/DELETE | `/api/tasks/<id>/` | Détail tâche |
| GET | `/api/statistics/` | Statistiques |

### Authentification API (JWT)
```bash
# Obtenir un token
POST /api/auth/login/
{
  "username": "votre_username",
  "password": "votre_password"
}

# Utiliser le token
Headers: Authorization: Bearer 
```

---

## 📁 Structure du projet
```
esmt-tasks/
├── backend/
│   ├── settings.py
│   └── urls.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_views.py
│   └── api_urls.py
├── projects/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_views.py
│   └── api_urls.py
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_views.py
│   └── api_urls.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── partials/
│   ├── users/
│   ├── projects/
│   └── tasks/
├── static/
├── media/
├── manage.py
└── README.md
```

---

## 👩‍💻 Développé par

**Fadhima Amadou Bah**  
Étudiante en Développement d'Applications et Réseaux — ESMT  
Année académique 2025-2026
Sauvegarde avec Ctrl+S puis pousse sur GitHub :

powershell
git add README.md
git commit -m "Add README documentation"
git push
Dis-moi quand c'est fait ! 😊

is is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
[12/Mar/2026 21:26:44] "GET / HTTP/1.1" 200 17269
[12/Mar/2026 21:27:04] "GET /projects/create/ HTTP/1.1" 200 17036
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>git add README.md
fatal: pathspec 'README.md' did not match any files
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>git add README.MD                                                   
fatal: pathspec 'README.MD' did not match any files
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>git add README.md                                                   
fatal: pathspec 'README.md' did not match any files
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>git add README                                                      
fatal: pathspec 'README' did not match any files
(venv) PS C:\Users\HP\Desktop\Cours-Semestre1-DAR\python\ProjetPy>

Afficher plus
21:34
Le fichier README.md n'a pas encore été créé ! Fais-le directement depuis PowerShell :

powershell
New-Item README.md
Puis ouvre-le dans PyCharm (il apparaîtra dans l'arborescence à gauche), colle le contenu du README que je t'ai donné, Ctrl+S, puis :

powershell
git add README.md
git commit -m "Add README documentation"
git push
Dis-moi quand c'est fait ! 😊




# 📋 ESMT Tasks — Application de Gestion des Tâches Collaboratives Application web développée pour l'ESMT permettant aux enseignants et étudiants de gérer des projets et tâches collaboratives, avec un système d'évaluation et de primes pour les professeurs. --- ## 🚀 Technologies utilisé

pasted




Claude est une IA et peut faire des erreurs. Veuillez vérifier les réponses.















Contenu collé
5.69 Ko •223 lignes
Le formatage peut être différent de la source

# 📋 ESMT Tasks — Application de Gestion des Tâches Collaboratives

Application web développée pour l'ESMT permettant aux enseignants et étudiants 
de gérer des projets et tâches collaboratives, avec un système d'évaluation 
et de primes pour les professeurs.

---

## 🚀 Technologies utilisées

| Technologie | Rôle |
|---|---|
| Python 3.13 | Langage principal |
| Django 6.0 | Framework backend |
| Django REST Framework | API RESTful |
| SQLite | Base de données |
| JWT (SimpleJWT) | Authentification API |
| HTML/CSS/JS | Frontend (templates Django) |

---

## ⚙️ Installation et configuration

### 1. Prérequis
- Python 3.10+
- pip
- Git

### 2. Cloner le projet
```bash
git clone https://github.com/FadhimaAmadouBah/esmt-tasks.git
cd esmt-tasks
```

### 3. Créer l'environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Installer les dépendances
```bash
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow
```

### 5. Appliquer les migrations
```bash
python manage.py makemigrations users
python manage.py makemigrations projects
python manage.py makemigrations tasks
python manage.py migrate
```

### 6. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur
```bash
python manage.py runserver
```

### 8. Accéder à l'application
- Interface web : http://127.0.0.1:8000
- Administration : http://127.0.0.1:8000/admin
- API : http://127.0.0.1:8000/api/

---

## 👥 Profils utilisateurs

| Profil | Permissions |
|---|---|
| **Étudiant** | Créer projets, gérer ses tâches, ne peut pas assigner un professeur |
| **Professeur** | Créer projets, assigner des tâches, voir ses statistiques et primes |
| **Admin** | Accès total, gestion des utilisateurs |

---

## 🏆 Système de primes

| Taux de complétion | Prime |
|---|---|
| 100% dans les délais | **100 000 FCFA** |
| 90% à 99% dans les délais | **30 000 FCFA** |
| Moins de 90% | Pas de prime |

---

## 🗃️ Modèles de données

### CustomUser
| Champ | Type | Description |
|---|---|---|
| username | CharField | Nom d'utilisateur |
| email | EmailField | Adresse email |
| role | CharField | etudiant / professeur |
| avatar | ImageField | Photo de profil |
| bio | TextField | Biographie |

### Project
| Champ | Type | Description |
|---|---|---|
| name | CharField | Nom du projet |
| description | TextField | Description |
| created_by | ForeignKey | Créateur |
| members | ManyToManyField | Membres |

### Task
| Champ | Type | Description |
|---|---|---|
| title | CharField | Titre |
| project | ForeignKey | Projet associé |
| assigned_to | ForeignKey | Utilisateur assigné |
| status | CharField | a_faire / en_cours / termine |
| priority | CharField | basse / normale / haute / urgente |
| due_date | DateTimeField | Date limite |

### PrimeEvaluation
| Champ | Type | Description |
|---|---|---|
| professeur | ForeignKey | Professeur évalué |
| period | CharField | T1 / T2 / T3 / T4 / annuel |
| year | IntegerField | Année |
| completion_rate | FloatField | Taux de complétion |
| prime_amount | IntegerField | 0 / 30000 / 100000 |

---

## 🌐 Routes disponibles

### Pages Web

| URL | Description |
|---|---|
| `/` | Tableau de bord |
| `/login/` | Connexion |
| `/register/` | Inscription |
| `/profile/` | Mon profil |
| `/projects/` | Liste des projets |
| `/projects/create/` | Créer un projet |
| `/projects/<id>/` | Détail d'un projet |
| `/projects/<id>/edit/` | Modifier un projet |
| `/projects/<id>/delete/` | Supprimer un projet |
| `/tasks/create/<project_id>/` | Créer une tâche |
| `/tasks/<id>/edit/` | Modifier une tâche |
| `/tasks/<id>/delete/` | Supprimer une tâche |
| `/tasks/statistics/` | Statistiques et primes |
| `/admin/` | Administration |

### API REST

| Méthode | URL | Description |
|---|---|---|
| POST | `/api/auth/register/` | Créer un compte |
| POST | `/api/auth/login/` | Connexion JWT |
| POST | `/api/auth/refresh/` | Rafraîchir token |
| GET/PUT | `/api/users/me/` | Mon profil |
| GET | `/api/users/` | Liste utilisateurs |
| GET/POST | `/api/projects/` | Projets |
| GET/PUT/DELETE | `/api/projects/<id>/` | Détail projet |
| GET/POST | `/api/projects/<id>/tasks/` | Tâches du projet |
| GET/PUT/DELETE | `/api/tasks/<id>/` | Détail tâche |
| GET | `/api/statistics/` | Statistiques |



## 📁 Structure du projet
```
esmt-tasks/
├── backend/
│   ├── settings.py
│   └── urls.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_views.py
│   └── api_urls.py
├── projects/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_views.py
│   └── api_urls.py
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── urls.py
│   ├── api_views.py
│   └── api_urls.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── partials/
│   ├── users/
│   ├── projects/
│   └── tasks/
├── static/
├── media/
├── manage.py
└── README.md
```

---

## 👩‍💻 Développée par

Fadhima Amadou Bah
Étudiante en Développement d'Applications et Réseaux — ESMT  
Année académique 2025-2026
