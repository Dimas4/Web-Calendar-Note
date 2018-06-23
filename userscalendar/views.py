from django.shortcuts import render, get_object_or_404
from .models import Day, Calendar
from django.http import Http404


def detail_page(request, pk, id):
    obj = Day.objects.get(calendar_id=pk, id=id)
    context = {
        "obj": obj
    }
    return render(request, "home/detail_calendar.html", context)


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
                name=str(i),
                content=str(i)) for i in range(1, 365)
        ])

    context = {
        "objects": obj
    }

    return render(request, "home/calendar.html", context)
