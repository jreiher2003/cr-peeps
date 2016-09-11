import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NFLCreateBet 

with open('Schedule.2016.json') as data_file:    
        data = json.load(data_file)

def home(request):
    return render(request, "nfl_home.html", {})

def nfl_schedule(request):
    t = datetime.time()
    d = datetime.date.today()
    dt = datetime.datetime.combine(d,t)
    dataset_list = data
    paginator = Paginator(dataset_list, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data_list = paginator.page(page)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)
    context = {"data": data_list, "dt":dt}
    return render(request, "nfl_schedule.html", context)


def nfl_public_board(request):
    return render(request, "nfl_public_board.html", {})

def nfl_picked_bet(request):
    return HttpResponse("nfl_picked_bet")

def nfl_confirm_bet(request):
    return HttpResponse("nfl_confirm_bet")

def nfl_create_bet(request):
    data_list = data
    game = {}
    for d in data_list:
        if d['GameKey'] == '201610115':
            game ={
                "home_team": d['HomeTeam'],
                "away_team": d['AwayTeam'],
                "point_spread": d["PointSpread"],
                "totals": d["OverUnder"],
                "team": [d["HomeTeam"],d["AwayTeam"]]
                }
    form = NFLCreateBet(game)
    context = {"data_list":data_list, "form": form}
    return render(request, "nfl_create_bet.html", context)

