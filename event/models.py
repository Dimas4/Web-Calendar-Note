from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    image = models.ImageField(upload_to="media", blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.TextField()
    content_object = GenericForeignKey('content_type', 'object_id')

    finished = models.BooleanField(default=False)

    data = models.DateTimeField(auto_now_add=True)

    def get_card_url(self, url):
        return HttpResponseRedirect(reverse("users_cards:card_detail", kwargs={'url': url}))

    def __str__(self):
        return self.title
