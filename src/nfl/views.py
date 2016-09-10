import json
from django.shortcuts import render
from django.http import HttpResponse

with open('Schedule.2016.json') as data_file:    
        data = json.load(data_file)

def home(request):
    # for d in data:
    #     print d["GameKey"]
    return HttpResponse("Hello, world. NFL home page.%s" % [d["GameKey"] for d in data])

def nfl_schedule(request):

    context = {"data": data}
    return render(request, "nfl_schedule.html", context)

def nfl_public_board(request):
    return HttpResponse("nfl_public_board")

def nfl_picked_bet(request):
    return HttpResponse("nfl_picked_bet")

def nfl_confirm_bet(request):
    return HttpResponse("nfl_confirm_bet")

def nfl_create_bet(request):
    return render(request, "nfl_create_bet.html", {})

