from django import forms
from .models import Calendar


class CreateEditCalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = [
            "name",
            "content"
        ]
