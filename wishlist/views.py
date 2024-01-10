from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from logic.services import view_in_wishlist, add_to_wishlist, remove_from_wishlist
from django.contrib.auth import get_user
from store.models import DATABASE


def wishlist_view(request):
    if request.method == "GET":
        current_user = get_user(request).username
        data = view_in_wishlist(request)[current_user]
        # if request.GET.get('format') == 'JSON':
        #     return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
        #                                              'indent': 4})

        products = []  # Список продуктов
        for product_id in data['products']:
            product = DATABASE[product_id]
            products.append(product)
        return render(request, "wishlist/wishlist.html", context={"products": products})


# @login_required(login_url='app_login:login_view')
def wishlist_add_json(request, id_product: str):
    """
    Добавление продукта в избранное и возвращение информации об успехе или неудаче в JSON
    """
    if request.method == "GET":
        result = add_to_wishlist(request, id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в избранное"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в избранное"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def wishlist_del_json(request, id_product: str):
    """
    Удаление продукта из избранного и возвращение информации об успехе или неудаче в JSON
    """
    if request.method == "GET":
        result = remove_from_wishlist(request, id_product)  # TODO вызовите обработчик из services.py удаляющий продукт из избранного
        if result:
            return  JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})# TODO верните JsonResponse с ключом "answer" и значением "Продукт успешно удалён из избранного"

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})  # TODO верните JsonResponse с ключом "answer" и значением "Неудачное удаление из избранного" и параметром status=404


def wishlist_json(request):
    """
    Просмотр всех продуктов в избранном для пользователя и возвращение этого в JSON
    """
    if request.method == "GET":
        current_user = get_user(request).username  # from django.contrib.auth import get_user
        data = view_in_wishlist(request)[current_user]   # TODO получите данные о списке товаров в избранном у пользователя
        if data:
            return JsonResponse(data,
                                json_dumps_params={'ensure_ascii': False})  # TODO верните JsonResponse c data

        return JsonResponse({"answer": "Пользователь не авторизован"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})   # TODO верните JsonResponse с ключом "answer" и значением "Пользователь не авторизирован" и параметром status=404


