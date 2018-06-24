from django.shortcuts import render, get_object_or_404
from .models import Day, Calendar
from django.http import Http404
import calendar


def month_page(request, id, month):
    if month.title() not in ["September", "October", "November",
                     "December", "January", "February",
                     "Mart", "April", "March", "June",
                     "July", "August"]:

        return Http404

    obj = Day.objects.filter(calendar_id=id)
    obj = Day.get_month(obj, id, month)


    context = {
        "obj": obj
    }

    return render(request, "home/month_page.html", context)


def detail_page(request, pk, id):
    obj = Day.objects.get(calendar_id=pk, id=id)

    myCal = calendar.HTMLCalendar(calendar.SUNDAY)
    new = myCal.formatmonth(2009, 7)

    context = {
        "obj": obj,
        "new": new,
    }
    return render(request, "home/detail_calendar.html", context)


def i_to_month_day(i):
    if i in range(1, 31):
        return i

    if i in range(31, 62):
        return i - 30

    if i in range(62, 92):
        return i - 61

    if i in range(92, 123):
        return i - 91

    if i in range(123, 154):
        return i - 122

    if i in range(154, 183):
        return i - 153

    if i in range(183, 214):
        return i - 182

    if i in range(214, 244):
        return i - 213

    if i in range(244, 275):
        return i - 242

    if i in range(275, 305):
        return i - 273

    if i in range(305, 336):
        return i - 303

    if i in range(336, 367):
        return i - 343


def home_page(request):
    global obj

    try:
        calendar = Calendar.objects.get(id=1)
    except Calendar.DoesNotExist:
        calendar = Calendar.objects.create(name="First", content="My first calendar")

    try:
        obj = Day.objects.filter(calendar_id=calendar.id)
    except Day.DoesNotExist:
        obj = Day.objects.bulk_create([
            Day(day=i,
                calendar_id=calendar.id,
                day_in_month=i_to_month_day(i),
                name=str(i),
                content=str(i)) for i in range(1, 365)
        ])

    context = {
        "objects": obj
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
