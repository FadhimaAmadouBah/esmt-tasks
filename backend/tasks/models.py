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