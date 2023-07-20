from django.shortcuts import render, redirect, get_object_or_404
from .models import Participant, ConfigData
from .forms import ParticipantForm
from math import floor


def indexPage(request):
    RomaObj = get_object_or_404(Participant, name='Roma')
    RomaMaxBookLength = get_object_or_404(ConfigData, pk=1).romaBookLength
    MargoObj = get_object_or_404(Participant, name='Margo')
    MargoMaxBookLength = get_object_or_404(ConfigData, pk=1).margoBookLength
    RomaDays = RomaObj.getDays()
    MargoDays = MargoObj.getDays()
    RomaResultsHeight = 200 - min(max(RomaDays), RomaMaxBookLength) / RomaMaxBookLength * 200
    MargoResultsHeight = 200 - min(max(MargoDays), MargoMaxBookLength) / MargoMaxBookLength * 200
    RomaPercent = str(floor(min(max(RomaDays), RomaMaxBookLength) / RomaMaxBookLength * 100)) + '%'
    MargoPercent = str(floor(min(max(MargoDays), MargoMaxBookLength) / MargoMaxBookLength * 100)) + '%'
    dateOfStart = str(get_object_or_404(ConfigData, pk=1).dateOfStart)
    context	= {
        'Roma': RomaObj,
        'Margo': MargoObj,
        'RomaDays': RomaDays,
        'MargoDays': MargoDays,
        'RomaResultsHeight': RomaResultsHeight,
        'MargoResultsHeight': MargoResultsHeight,
        'RomaPercent': RomaPercent,
        'MargoPercent': MargoPercent,
        'dateOfStart': dateOfStart,
    }
    if RomaPercent == '100%':
        context['winner'] = 'ROMA WON!'
    elif MargoPercent == '100%':
        context['winner'] = 'MARGO WON!'
    return render(request, 'app/index.html', context=context)


def RomaUpdate(request):
    try:
        dayToChange = ''
        for i in request.POST:
            if i.startswith('day'):
                dayToChange = i
                break
        RomaObj = get_object_or_404(Participant, name='Roma')
        setattr(RomaObj, dayToChange, request.POST[dayToChange])
        RomaObj.save()
    except ValueError:
      print('err')
    return redirect('indexPage')


def MargoUpdate(request):
    try:
        dayToChange = ''
        for i in request.POST:
            if i.startswith('day'):
                dayToChange = i
                break
        MargoObj = get_object_or_404(Participant, name='Margo')
        setattr(MargoObj, dayToChange, request.POST[dayToChange])
        MargoObj.save()
    except ValueError:
      print('err')
    return redirect('indexPage')