from django.shortcuts import render, get_object_or_404
from django.http import Http404

import calendar
import uuid

from .additional import i_to_month_day
from .forms import CreateCalendarForm
from .models import Day, Calendar


def home_page_start(request):
    return render(request, "home/start_page_calendar.html")


def create_page(request):
    form = CreateCalendarForm(request.POST or None)
    if form.is_valid():
        new_calendar = form.save(commit=False)
        new_calendar.url = uuid.uuid4()
        new_calendar.save()
        return new_calendar.get_absolute_url()

    context = {
        "form": form
    }

    return render(request, "home/create_calendar.html", context)


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


def detail_page(request, url, id):
    obj = Day.objects.get(calendar_url=url, id=id)

    myCal = calendar.HTMLCalendar(calendar.SUNDAY)
    new = myCal.formatmonth(2009, 7)

    context = {
        "obj": obj,
        "new": new,
    }
    return render(request, "home/detail_calendar.html", context)


def home_page(request, slug):
    global obj

    calendar = get_object_or_404(Calendar, url=slug)

    obj = Day.objects.filter(calendar_url=slug)
    if len(obj) == 0:
        obj = Day.objects.bulk_create([
            Day(day=i,
                calendar_url=slug,
                day_in_month=i_to_month_day(i),
                name=str(i),
                content=str(i)) for i in range(1, 367)
        ])

    context = {
        "objects": obj,
        "calendar_url": slug,
    }

    return render(request, "home/calendar.html", context)


# class CustomManager(models.Manager):
#     def bulk_create(self, qs, **kwargs):
#         super().bulk_create(qs, **kwargs)
#         print(qs)
#         print(self.day_in_month)
#         print(self.objects)
#         for i in qs:
#             print(i)
#             if i.day_in_month in range(1, 31):
#                 i.month = "September"
#
#             if i.day_in_month in range(31, 62):
#                 i.month = "October"
#                 i.day_in_month = i.day_in_month - 30
#
#             if i.day_in_month in range(62, 92):
#                 i.month = "November"
#                 i.day_in_month = i.day_in_month - 61
#
#             if i.day_in_month in range(92, 123):
#                 i.month = "December"
#                 i.day_in_month = i.day_in_month - 91
#
#             if i.day_in_month in range(123, 154):
#                 i.month = "January"
#                 i.day_in_month = i.day_in_month - 122
#
#             if i.day_in_month in range(154, 183):
#                 i.month = "February"
#                 i.day_in_month = i.day_in_month - 153
#
#             if i.day_in_month in range(183, 214):
#                 i.month = "March"
#                 i.day_in_month = i.day_in_month - 182
#
#             if i.day_in_month in range(214, 244):
#                 i.month = "April"
#                 i.day_in_month = i.day_in_month - 213
#
#             if i.day_in_month in range(244, 275):
#                 i.month = "May"
#                 i.day_in_month = i.day_in_month - 242
#
#             if i.day_in_month in range(275, 305):
#                 i.month = "June"
#                 self.day_in_month = i.day_in_month - 273
#
#             if i.day_in_month in range(305, 336):
#                 i.month = "July"
#                 i.day_in_month = i.day_in_month - 303
#
#             if i.day_in_month in range(336, 367):
#                 i.month = "August"
#                 i.day_in_month = i.day_in_month - 343
