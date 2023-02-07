from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Site Honey Skin")

def categories(request, catid):
    if(request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Category</h1> <p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Archive year</h1> <p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Not Found str</h1>')


