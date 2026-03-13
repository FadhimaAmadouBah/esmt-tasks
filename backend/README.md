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
git clone https://github.com/Fadhima/ProjetPy.git
cd ProjetPy
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
  "username": "Fadhima",
  "password": "Passer123"
}

# 2. Utiliser le token dans les requêtes
Headers: Authorization: Bearer <access_token>
```



---

## 📁 Structure du projet
```
esmt-tasks/
├── backend/
│   
├── users/
│   
├── projects/
│   
├── tasks/
│   
├── templates/
│   
├── static/
├── media/
├── manage.py
├── .gitignore
└── README.md
```

---

## 👩‍💻 Développé par

Fadhima Amadou Bah
Étudiant(e) en Développement d'Applications Reparties — ESMT  
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
