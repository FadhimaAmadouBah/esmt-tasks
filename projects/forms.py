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