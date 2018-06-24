from django import forms
from .models import Calendar


class CreateCalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = [
            "name",
            "content"
        ]
