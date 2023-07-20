from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    day1 = models.IntegerField(default=0)
    day2 = models.IntegerField(default=0)
    day3 = models.IntegerField(default=0)
    day4 = models.IntegerField(default=0)
    day5 = models.IntegerField(default=0)
    day6 = models.IntegerField(default=0)
    day7 = models.IntegerField(default=0)
    day8 = models.IntegerField(default=0)
    day9 = models.IntegerField(default=0)
    day10 = models.IntegerField(default=0)
    day11 = models.IntegerField(default=0)
    day12 = models.IntegerField(default=0)
    day13 = models.IntegerField(default=0)
    day14 = models.IntegerField(default=0)
    
    def getDays(self):
        days = []
        for i in range(14):
            days.append(getattr(self, f'day{i + 1}'))
        return days
    
    def __str__(self):
        return self.name


class ConfigData(models.Model):
    margoBookLength = models.IntegerField()
    romaBookLength = models.IntegerField()
    dateOfStart = models.DateField(blank=True)

    def __str__(self):
        return 'Main Config Data'

