from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import DATABASE


def products_view(request):
    if request.method == "GET":
        id_product = request.GET.get('id')
        if id_product:
            if id_product in DATABASE.keys():
                return JsonResponse(DATABASE[id_product], json_dumps_params={'ensure_ascii': False,
                                                              'indent': 4})
            else:
                return HttpResponseNotFound("Данного продукта нет в базе данных")
        else:
            return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                          'indent': 4})


def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()
        return HttpResponse(data)


def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:
                    with open(f'store/products/{page}.html', encoding="utf-8") as f:
                        data_1 = f.read()
                    return HttpResponse(data_1)
        elif isinstance(page, int):
            data = DATABASE.get(str(page))
            if data:
                with open(f'store/products/{data["html"]}.html', encoding="utf-8") as f:
                    data_1 = f.read()
                    return HttpResponse(data_1)
        return HttpResponse(status=404)

