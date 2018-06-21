from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from .forms import CardForm, EventForm
from event.models import Event
from .models import Card

import uuid


def home(request):
    return render(request, "home/home_page.html")


def card_delete(request):
    pass


def card_detail(request, url):
    card = Card.objects.get(url=url)
    model_type = ContentType.objects.get_for_model(Card)
    obj = Event.objects.filter(content_type=model_type, object_url=url).order_by("-data")

    context = {
        "objects": obj,
        "card": card,
    }

    return render(request, "home/detail.html", context)


def create_card(request):
    form = CardForm(request.POST or None)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = request.user
        uuid_current = uuid.uuid4()
        new_form.url = uuid_current
        new_form.save()

        return new_form.get_card_url(uuid_current)

    context = {
        "form": form
    }

    return render(request, "home/create_card.html", context)


def card_add_event(request, url):
    form = EventForm(request.POST or None)

    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        model_type = ContentType.objects.get_for_model(Card)

        event = Event.objects.create(title=title, content=content, content_type=model_type, object_url=url)

        return event.get_card_url(url)

    context = {
        "form": form,
        "url": url
    }

    return render(request, "home/add_event.html", context)
