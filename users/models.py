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