from calendar import c
from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Drink at least 2 liters of water daily!",
    "may": "Read at least 10 pages of a book every day!",
    "june": "Try a new hobby or skill each week!",
    "july": "Meditate for at least 10 minutes every day!",
    "august": "Write down three things you're grateful for every day!",
    "september": "Limit social media usage to 30 minutes per day!",
    "october": "Do at least 10 push-ups and 10 sit-ups daily!",
    "november": "Avoid added sugar for the whole month!",
    "december": "Perform one random act of kindness every day!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    
    return render(request, "challenges/index.html", {
        "months": months,
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month not in range(1, len(months)):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize(),
        })
        
    except:
        return HttpResponseNotFound("<h1>This month is not supoorted!</h1>")