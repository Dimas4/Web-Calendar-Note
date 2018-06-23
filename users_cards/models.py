from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from event.models import Event

from django.http import HttpResponseRedirect
from django.urls import reverse


class Card(models.Model):
    url = models.TextField()
    title = models.CharField(max_length=50)
    content = models.TextField()

    image = models.ImageField(upload_to="media", blank=True, null=True)

    current_events = GenericRelation(Event)

    data = models.DateTimeField(auto_now_add=True)

    def get_card_url(self, url):
        return HttpResponseRedirect(reverse("users_cards:card_detail", kwargs={'url': url}))

    def __str__(self):
        return self.title
