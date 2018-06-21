from django import forms

from event.models import Event
from .models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'title',
            'content'
        ]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'content'
        ]
