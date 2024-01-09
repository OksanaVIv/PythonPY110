from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "GET":
        return render(request, "login/login.html")

    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            login(request, user)
            return redirect("/")
        return render(request, "login/login.html", context={"error": "Неверные данные"})


def logout_view(request):
    if request.method == "GET":
        logout(request)  # Функция разлогинивает пользователя
        return redirect("/")

