from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from weather_api import current_weather
from django.http import JsonResponse


def datetime_view(request):
    if request.method == "GET":
        data = datetime.now()  # Написать, что будет возвращаться из данного представления
        return HttpResponse(data)


def my_weather(request):
    if request.method == "GET":
        data = current_weather(59.93, 30.31)
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})
