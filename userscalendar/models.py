from django.db import models


class Day(models.Model):
    day = models.PositiveIntegerField()
    calendar_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.name

#
# class Month(models.Model):
#     name = models.CharField(max_length=50)
#     day = models.ManyToManyField(Day)


class Calendar(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    month = models.ManyToManyField(Day)

    def __str__(self):
        return self.name


class Day_Calendar(models.Model):
    day_id = models.PositiveIntegerField()
    calendar_id = models.PositiveIntegerField()

    def __str__(self):
        return '{} {}'.format(self.day_id, self.calendar_id)
