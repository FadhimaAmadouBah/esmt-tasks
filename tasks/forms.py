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