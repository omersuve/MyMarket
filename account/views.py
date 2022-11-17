from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from my_market.models import Store


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "account/login.html",
                {"error": "username or password is wrong!"},
            )
    else:
        return render(request, "account/login.html")


def signup_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        is_owner = None
        store_name = None
        if "is_owner" in request.POST.keys():
            is_owner = request.POST["is_owner"]
            store_name = request.POST["store_name"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(
                    request,
                    "account/signup.html",
                    {"error": "username already exists!"},
                )
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                p = user.profile
                if is_owner:
                    p.is_store_owner = True
                    p.owned_store_name = store_name
                else:
                    p.is_store_owner = False
                    p.owned_store_name = None
                p.save()
                if store_name is not None:
                    new_store = Store.objects.create(name=store_name)
                    new_store.save()
                return redirect("login")
        else:
            return render(
                request,
                "account/signup.html",
                {"error": "passwords are not equal!"},
            )
    else:
        return render(request, "account/signup.html")


def logout_request(request):
    logout(request)
    return redirect("home")
