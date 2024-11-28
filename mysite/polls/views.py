from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(requets: HttpRequest) -> HttpResponse:
  return HttpResponse("Hello, Otus!")
