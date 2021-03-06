from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models


class Day(models.Model):
    day = models.PositiveIntegerField()
    month = models.CharField(max_length=20, blank=True)
    calendar_url = models.TextField()
    day_in_month = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    content = models.TextField()

    def get_absolute_url(self, url):
        return HttpResponseRedirect(reverse("userscalendar:detail_page", kwargs={'url': url, 'id': self.id}))

    def get_month(self, url, month):
        if month.title() == "September":
            return Day.objects.filter(calendar_url=url)[:30]
        if month.title() == "October":
            return Day.objects.filter(calendar_url=url)[30:61]
        if month.title() == "November":
            return Day.objects.filter(calendar_url=url)[61:91]
        if month.title() == "December":
            return Day.objects.filter(calendar_url=url)[91:122]
        if month.title() == "January":
            return Day.objects.filter(calendar_url=url)[122:153]
        if month.title() == "February":
            return Day.objects.filter(calendar_url=url)[153:182]
        if month.title() == "March":
            return Day.objects.filter(calendar_url=url)[182:213]
        if month.title() == "April":
            return Day.objects.filter(calendar_url=url)[213:243]
        if month.title() == "May":
            return Day.objects.filter(calendar_url=url)[243:274]
        if month.title() == "June":
            return Day.objects.filter(calendar_url=url)[274:304]
        if month.title() == "July":
            return Day.objects.filter(calendar_url=url)[304:335]
        if month.title() == "August":
            return Day.objects.filter(calendar_url=url)[335:366]

    def __str__(self):
        return self.name


class Calendar(models.Model):
    url = models.TextField()
    name = models.CharField(max_length=50)
    content = models.TextField()
    day = models.ManyToManyField(Day, blank=True)

    image = models.ImageField(upload_to="media", blank=True, null=True)

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse("userscalendar:home_page", kwargs={'slug': self.url}))

    def __str__(self):
        return str(self.id)
