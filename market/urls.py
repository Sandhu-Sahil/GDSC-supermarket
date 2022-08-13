from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("category/<str:category>", views.category_view, name="category"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_to_watchlist/<str:product>", views.add_to_watchlist, name="add_to_watchlist"),
    path("increase-quantity/<str:product>", views.increase_quantity, name="increase-quantity"),
    path("decrease-quantity/<str:product>", views.decrease_quantity, name="decrease-quantity"),
    path("remove-watchlist/<str:product>", views.remove_watchlist, name="remove-watchlist"),
    path("product/<str:product>", views.product_view, name="product_view"),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)