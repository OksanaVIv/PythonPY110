from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def datetime_view(request):
    if request.method == "GET":
        data = datetime.now()  # Написать, что будет возвращаться из данного представления
        return HttpResponse(data)
