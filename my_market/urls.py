from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add/<int:id>", views.add_product_user, name="add_product_user"),
    path("addStore/<int:id>", views.add_store_user, name="add_store_user"),
    path("remove/<int:id>", views.remove_product_user, name="remove_product_user"),
    path("removeStore/<int:id>", views.remove_store_user, name="remove_store_user"),
    path("products/<slug:slug>", views.product_details, name="product_details"),
    path("stores/<slug:slug>", views.products_by_store, name="store_details"),
    path(
        "stores/<slug:s_slug>/remove",
        views.remove_store,
        name="remove_store_owner",
    ),
    path("stores/<slug:slug>/addProduct", views.add_product, name="add_product"),
    path(
        "stores/<slug:s_slug>/removeProduct/<slug:p_slug>",
        views.remove_product,
        name="remove_product",
    ),
]
