from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests as rq
from ast import literal_eval
from dateutil.parser import parse
import json

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'login.html', {})

@login_required
def dashboard(request):
    data = rq.get("https://s3.us-east-2.wasabisys.com/akshit/dataset-django/ft_assignment.json")
    data = literal_eval(data.text)

    context = {}

    appNames = []
    for js in data:
        appNames.append(js['app_name'])

    if request.method == 'GET':
        context["appNames"] = appNames

    elif request.method == 'POST':
        appName = request.POST.get("appName")
        sdate = request.POST.get("sdate")
        edate = request.POST.get("edate")
        
        di = appNames.index(appName)
        appData = data[di]['date_wise_metrics']

        chat = {}
        for ok,ov in appData.items():
            for ik,iv in ov.items():
                if parse(ik).date() >= parse(sdate).date() and parse(ik).date() <= parse(edate).date():
                    if chat.get(ik):
                        chat[ik].append(iv)
                    else:
                        chat[ik] = [iv%1000]
        
        showChart = []
        for k,v in chat.items():
            lstdata = [k]
            lstdata.extend(v)
            showChart.append(lstdata)
        
        context['appName'] = appName
        context['sdate'] = sdate
        context['edate'] = edate
        context['showChart'] = json.dumps(showChart)

    return render(request, 'dashboard.html', context)