from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def monthly_challenge(request, month):

    challenge_text = {
        "january": "Eat no meat for the entire month!",
        "february": "Walk for at least 20 minutes every day!",
        "march": "Learn Django for at least 20 minutes every day!"
    }

    if month not in challenge_text:
        return HttpResponseNotFound("This month is not supoorted!")
    
    return HttpResponse(challenge_text[month])