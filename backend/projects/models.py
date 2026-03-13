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