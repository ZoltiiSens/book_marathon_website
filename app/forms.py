from django.forms import ModelForm
from .models import Participant


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8', 'day9', 'day10', 'day11', 'day12', 'day13', 'day14']