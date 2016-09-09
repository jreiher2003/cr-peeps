from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. NFL home page.")

def nfl_home(request):
    return HttpResponse("nfl_home")

def nfl_public_board(request):
    return HttpResponse("nfl_public_board")

def nfl_picked_bet(request):
    return HttpResponse("nfl_picked_bet")

def nfl_confirm_bet(request):
    return HttpResponse("nfl_confirm_bet")

def nfl_create_bet(request):
    return HttpResponse("nfl_create_bet")

