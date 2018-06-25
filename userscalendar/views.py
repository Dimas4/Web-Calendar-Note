from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.http import Http404

import uuid

from .additional import i_to_month_day, give_month_for_data
from .forms import CreateEditCalendarForm
from .models import Day, Calendar

from users_cards.forms import EventForm
from event.models import Event


def home_page_start(request):
    return render(request, "home/start_page_calendar.html")


def home_page(request, slug):
    global obj

    calendar = get_object_or_404(Calendar, url=slug)

    obj = Day.objects.filter(calendar_url=slug)

    if len(obj) == 0:
        obj = Day.objects.bulk_create([
            Day(day=i,
                calendar_url=slug,
                day_in_month=i_to_month_day(i),
                month=give_month_for_data(i),
                name=str(i),
                content=str(i)) for i in range(1, 367)
        ])

    context = {
        "objects": obj,
        "calendar_url": slug,
    }

    return render(request, "home/calendar.html", context)


def create_page(request):
    form = CreateEditCalendarForm(request.POST or None)
    if form.is_valid():
        new_calendar = form.save(commit=False)
        new_calendar.url = uuid.uuid4()
        new_calendar.save()
        return new_calendar.get_absolute_url()

    context = {
        "form": form
    }

    return render(request, "home/create_calendar.html", context)


def detail_page(request, url, id):
    obj = Day.objects.get(calendar_url=url, id=id)
    model_type = ContentType.objects.get_for_model(Day)
    object_id = '{}{}'.format(url, id)
    objects = Event.objects.filter(content_type=model_type, object_id=object_id).order_by("-data")

    # myCal = calendar.HTMLCalendar(calendar.SUNDAY)
    # new = myCal.formatmonth(2009, 7)
    context = {
        "obj": obj,
        "url": url,
        "objects": objects,
        "url_id": object_id
    }
    return render(request, "home/detail_calendar.html", context)


def edit_page(request, url, id):
    obj = Day.objects.get(calendar_url=url, id=id)

    form = CreateEditCalendarForm(request.POST or None, instance=obj)

    if form.is_valid():
        day = form.save(commit=False)
        day.name = form.cleaned_data.get("name")
        day.content = form.cleaned_data.get("content")
        day.save()
        return obj.get_absolute_url(url)

    context = {
        "form": form,
        "day_id": id,
        "url": url
    }

    return render(request, "home/edit_calendar_page.html", context)


def create_event(request, url, id):
    form = EventForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        image = form.cleaned_data.get("image")

        model_type = ContentType.objects.get_for_model(Day)

        object_id = '{}{}'.format(url, id)
        event = Event.objects.create(title=title,
                                     content=content,
                                     image=image,
                                     content_type=model_type,
                                     object_id=object_id
                                     )
        return event.get_calendar_url(url, id)

    context = {
        "form": form,
        "url": url,
        "calendar_id": id
    }

    return render(request, "home/create_event_calendar.html", context)


def event_finished_delete(request, url, id, slug):
    if slug not in ['delete', 'finished']:
        return Http404

    event = Event.objects.get(object_id=url, id=id)

    if slug == 'delete':
        event.delete()
        return event.get_calendar_url(url[:36], url[36:])

    if slug == 'finished':
        event.finished = True
        event.save()
        return event.get_calendar_url(url[:36], url[36:])


def month_page(request, url, month):
    if month.title() not in ["September", "October", "November",
                     "December", "January", "February",
                     "March", "April", "May", "June",
                     "July", "August"]:

        return Http404

    obj = Day.objects.filter(calendar_url=url)
    obj = Day.get_month(obj, url, month)

    context = {
        "obj": obj,
        "month": month.title()
    }

    return render(request, "home/month_page.html", context)
