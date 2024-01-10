from django.shortcuts import render


def wishlist_view(request):
    if request.method == "GET":
        return render(request, 'wishlist/wishlist.html')



