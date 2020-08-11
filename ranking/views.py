from django.shortcuts import render
from django.http import HttpResponse
from ranking.models import *
from django.http import JsonResponse
import json
import logging
from django.views.decorators.csrf import csrf_exempt
import csv

def index(request):
    return render(request, 'index.html')

def newgame(request):
    return render(request, 'newgame.html')

def getinf(request):
    return JsonResponse(list(Rankinf.objects.filter(gameid=request.GET['id']).order_by('-score').values()),safe=False)

def getcsv(request):
    output = []
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    query_set = Rankinf.objects.filter(gameid=request.GET['id']).order_by('-score')
    # Header
    writer.writerow(['playername', 'score'])
    for score in query_set:
        output.append([score.playername, score.score])
    # CSV Data
    writer.writerows(output)
    return response


@csrf_exempt
def postinf(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        Rankinf.objects.create(gameid=int(received_json_data['gameid']),playername=received_json_data['username'],score=int(received_json_data['score']))
        return HttpResponse("Data received.")

def postnewgame(request):
    if request.method == 'POST':
        try:
            return HttpResponse(json.dumps({'result': str(gameInfo.objects.create(name=request.POST['gamename']).id)}),
                                content_type="text/javascript")
        except Exception as e:
            return HttpResponse(json.dumps({'result': str(gameInfo.objects.get(name=request.POST['gamename']).id)}),
                                content_type="text/javascript")
