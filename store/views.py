from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import DATABASE


def products_view(request):
    if request.method == "GET":
        id_product = request.GET.get('id')
        if id_product:
            for product in DATABASE.keys():
                if product == id_product:
                    return JsonResponse(product.values, json_dumps_params={'ensure_ascii': False,
                                                                     'indent': 4})
                else:
                    return HttpResponseNotFound("Данного продукта нет в базе данных")
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                                  'indent': 4})


def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()
        return HttpResponse(data)
