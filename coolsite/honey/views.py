from django.core.exceptions import PermissionDenied, BadRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Site Honey Skin")




def categories(request,category):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>all categories =) </h1><p>{category}</p>")

def archive(request,year):
    if int(year) > 2023:
        raise Http404()
    elif int(year) == 2021:
        raise PermissionDenied
    elif int(year) == 2004:
        raise BadRequest()
    return HttpResponse(f"<h1>archives =) </h1><p>{year}</p>")
def not_found(request, exception):
    return HttpResponseNotFound('<h1> 404 </h1> <h2> Stranitsa ne naidena! </h2> ')
def closed_access(request, exception):
    return HttpResponseNotFound('<h1>Dostup zakryt!</h1>')
def bad_request(request, exception):
    return HttpResponseBadRequest("<h1>Nevozmozhno obnovit' zapros!</h1>")
def server_error(request):
    return HttpResponseServerError('<h1> Oshibka servera! </h1>')


