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
| Angular 21 | Frontend (Objectif 2) |
| HTML/CSS/JS | Frontend (Templates Django - Objectif 1) |

---

## ⚙️ Installation et configuration

### 1. Prérequis
- Python 3.10+
- Node.js 18+
- pip
- Git

### 2. Cloner le projet
```bash
git clone https://github.com/FadhimaAmadouBah/esmt-tasks.git
cd esmt-tasks
```

### 3. Backend Django
```bash
# Créer l'environnement virtuel
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Installer les dépendances
pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow

# Appliquer les migrations
python manage.py makemigrations users
python manage.py makemigrations projects
python manage.py makemigrations tasks
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

### 4. Frontend Angular
```bash
cd frontend

# Installer les dépendances
npm install

# Lancer Angular
ng serve
```

### 5. Accéder à l'application

| Interface | URL |
|---|---|
| Django Templates (Objectif 1) | http://127.0.0.1:8000 |
| Angular (Objectif 2) | http://localhost:4200 |
| Administration Django | http://127.0.0.1:8000/admin |
| API REST | http://127.0.0.1:8000/api/ |

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

### Pages Django Templates (Objectif 1)

| URL | Description |
|---|---|
| `/` | Tableau de bord |
| `/login/` | Connexion |
| `/register/` | Inscription |
| `/profile/` | Mon profil |
| `/projects/` | Liste des projets |
| `/projects/create/` | Créer un projet |
| `/projects/<id>/` | Détail d'un projet |
| `/tasks/statistics/` | Statistiques et primes |
| `/admin/` | Administration |

### Pages Angular (Objectif 2)

| URL | Description |
|---|---|
| `/login` | Connexion |
| `/register` | Inscription |
| `/dashboard` | Tableau de bord |
| `/projects` | Liste des projets |
| `/projects/:id/tasks` | Tâches d'un projet |

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
Headers: Authorization: Bearer <access_token>
```

---

## 🧪 Tests
```bash
pip install pytest-django
python -m pytest tests.py -v
```

Résultat : **9/9 tests passés ✅**

---

## 📁 Structure du projet
```
esmt-tasks/
├── backend/           ← Config Django
├── users/             ← App utilisateurs
├── projects/          ← App projets
├── tasks/             ← App tâches
├── templates/         ← Templates Django (Objectif 1)
├── static/
├── media/
├── frontend/          ← Application Angular (Objectif 2)
│   └── src/
│       └── app/
│           ├── components/
│           │   ├── login/
│           │   ├── register/
│           │   ├── dashboard/
│           │   ├── projects/
│           │   └── tasks/
│           ├── services/
│           └── interceptors/
├── tests.py           ← Tests unitaires
├── manage.py
└── README.md
```

---

## 👩‍💻 Développé par

**Fadhima Amadou Bah**  
Étudiante en Développement d'Applications et Réseaux — ESMT  
Année académique 2025-2026