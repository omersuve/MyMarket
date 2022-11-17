from django.shortcuts import render, redirect
from my_market.models import Store, Product


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        "stores": Store.objects.all(),
        "products": Product.objects.all(),
        "fav_products": Product.objects.filter(profiles__id=request.user.profile.id),
        "fav_stores": Store.objects.filter(profiles__id=request.user.profile.id),
    }
    return render(request, "my_market/index.html", context)


def add_product_user(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    p = Product.objects.get(id=id)
    p.profiles.add(request.user.profile)
    context = {
        "fav_products": Product.objects.filter(profiles__id=request.user.profile.id),
        "fav_stores": Store.objects.filter(profiles__id=request.user.profile.id),
        "stores": Store.objects.all(),
        "products": Product.objects.filter(
            stores__slug=Store.objects.get(product=p).slug
        ),
        "selected_store": Store.objects.get(product=p).slug,
    }
    return render(request, "my_market/index.html", context)


def add_store_user(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    s = Store.objects.get(id=id)
    s.profiles.add(request.user.profile)
    context = {
        "fav_products": Product.objects.filter(profiles__id=request.user.profile.id),
        "fav_stores": Store.objects.filter(profiles__id=request.user.profile.id),
        "stores": Store.objects.all(),
        "products": Product.objects.filter(stores__id=id),
        "selected_store": s.slug,
    }
    return render(request, "my_market/index.html", context)


def remove_store_user(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    s = Store.objects.get(id=id)
    s.profiles.remove(request.user.profile)
    context = {
        "fav_products": Product.objects.filter(profiles__id=request.user.profile.id),
        "fav_stores": Store.objects.filter(profiles__id=request.user.profile.id),
        "stores": Store.objects.all(),
        "products": Product.objects.filter(stores__id=id),
        "selected_store": s.slug,
    }
    return render(request, "my_market/index.html", context)


def remove_product_user(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    p = Product.objects.get(id=id)
    p.profiles.remove(request.user.profile)
    context = {
        "fav_products": Product.objects.filter(profiles__id=request.user.profile.id),
        "fav_stores": Store.objects.filter(profiles__id=request.user.profile.id),
        "stores": Store.objects.all(),
        "products": Product.objects.filter(
            stores__slug=Store.objects.get(product=p).slug
        ),
        "selected_store": Store.objects.get(product=p).slug,
    }
    return render(request, "my_market/index.html", context)


def products_by_store(request, slug):
    context = {
        "fav_products": Product.objects.filter(profiles__id=request.user.profile.id),
        "fav_stores": Store.objects.filter(profiles__id=request.user.profile.id),
        "products": Product.objects.filter(stores__slug=slug),
        "stores": Store.objects.all(),
        "selected_store": slug,
    }
    print(context)
    return render(request, "my_market/index.html", context)


def remove_store(request, s_slug):
    if request.method == "POST":
        s = Store.objects.get(slug=s_slug)
        s.delete()
        context = {
            "stores": Store.objects.all(),
            "selected_store": s_slug,
        }
        request.user.profile.is_store_owner = False
        request.user.profile.owned_store_name = None
        request.user.save()
        return render(request, "my_market/index.html", context)
    else:
        context = {"stores": Store.objects.all(), "products": Product.objects.all()}
        return render(request, "my_market/index.html", context)


def product_details(request, slug):
    context = {"product": Product.objects.get(slug=slug)}
    return render(request, "my_market/product-details.html", context)


def store_details(request, slug):
    store = Store.objects.get(slug=slug)
    context = {"store": store}
    return render(request, "my_market/store-details.html", context)


def store_info_details(request, slug):
    store = Store.objects.get(slug=slug)
    context = {"store": store}
    return render(request, "my_market/store-details.html", context)


def add_product(request, slug):
    print("slug", slug)
    if request.method == "POST":
        s = Store.objects.get(slug=slug)
        name = request.POST["product_name"]
        description = request.POST["product_description"]
        price = request.POST["price"]
        if len(name) == 0 or len(price) == 0 or len(description) == 0 or int(price) < 0:
            return render(
                request,
                "my_market/index.html",
                {
                    "error": "all fields required!",
                    "stores": Store.objects.all(),
                    "products": Product.objects.all(),
                },
            )
        p = Product.objects.create(
            name=name, price=price, description=description, stores_id=s.id
        )
        p.save()
        context = {
            "stores": Store.objects.all(),
            "products": Product.objects.filter(stores__id=s.id),
            "selected_store": slug,
        }
        return render(request, "my_market/index.html", context)
    else:
        context = {"stores": Store.objects.all(), "products": Product.objects.all()}
        return render(request, "my_market/index.html", context)


def remove_product(request, s_slug, p_slug):
    if request.method == "POST":
        p = Product.objects.get(slug=p_slug)
        print("product", p)
        print("s_slug", s_slug)
        print("p_slug", p_slug)
        print(Product.objects.filter(stores__slug=s_slug))
        p.delete()
        context = {
            "stores": Store.objects.all(),
            "products": Product.objects.filter(stores__slug=s_slug),
            "selected_store": s_slug,
        }
        return render(request, "my_market/index.html", context)
    else:
        context = {"stores": Store.objects.all(), "products": Product.objects.all()}
        return render(request, "my_market/index.html", context)
