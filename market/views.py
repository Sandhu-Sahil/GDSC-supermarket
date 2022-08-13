from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import CustomUserCreationForm

from .models import User, Product, Category, Watchlist, Quantity

def index(request):
    products = Product.objects.all().order_by('id').reverse()
    categories = Category.objects.all()
    user = request.user 
    if user.id is None:
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, "market/index.html", context)
    my_watchlist = Watchlist.objects.get(user=request.user)
    
    context = {
        'products': products,
        'my_watchlist': my_watchlist,
        'categories': categories,
    }
    return render(request, "market/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "market/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, "market/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request, user)
            watchlist = Watchlist.objects.create(user = request.user)
            watchlist.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "market/register.html", {
                "message": "An error has been occured during registration",
                'form':form
            })
        
        # username = request.POST["username"]
        # email = request.POST["email"]

        # # Ensure password matches confirmation
        # password = request.POST["password"]
        # confirmation = request.POST["confirmation"]
        # if password != confirmation:
        #     return render(request, "market/register.html", {
        #         "message": "Passwords must match."
        #     })

        # # Attempt to create new user
        # try:
        #     user = User.objects.create_user(username, email, password)
        #     user.save()
        # except IntegrityError:
        #     return render(request, "market/register.html", {
        #         "message": "Username already taken."
        #     })
        # login(request, user)
        # watchlist = Watchlist.objects.create(user = request.user)
        # watchlist.save()
        # return HttpResponseRedirect(reverse("index"))
    else:
        form = CustomUserCreationForm()
        return render(request, "market/register.html",{'form':form})

@login_required
def watchlist(request):
    categories = Category.objects.all()
    if request.user.id is None:
        return redirect('index')

    my_watchlist = Watchlist.objects.get(user=request.user)
    quantity = Quantity.objects.filter(user=request.user)
    total = 0
    for quanti in quantity:
        for product in my_watchlist.products.all():
            if quanti.products.id == product.id:
                total = total + (product.price*quanti.quantity)

    context = {
        'total':total,
        'quantity': quantity,
        'my_watchlist': my_watchlist,
        'categories': categories,
    }
    return render(request, "market/watchlist.html", context)


def category_view(request, category):
    category_name = Category.objects.get(name=category)
    products = Product.objects.filter(category=category_name).order_by('id').reverse()
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'category_name': category_name,
        'categories': categories,
    }
    return render(request, "market/category.html", context)

def product_view(request, product):
    if request.method == 'GET':
        categories = Category.objects.all()
        if request.user.id is None:
            return redirect('login')

        my_watchlist = Watchlist.objects.get(user=request.user)
        product = Product.objects.get(id=product)
        if (Quantity.objects.filter(user=request.user).filter(products=product)):
            quantity = Quantity.objects.filter(user = request.user).filter(products = product)
            quantity = Quantity.objects.get(id = quantity[0].id)
        else:
            quantity= None
        context = {
            'quantity':quantity,
            'product': product,
            'my_watchlist': my_watchlist,
            'categories': categories,
        }
        return render(request, 'market/product_view.html', context)

@login_required
def add_to_watchlist(request, product):
    product_to_add = Product.objects.get(id=product)
    watchlist = Watchlist.objects.get(user=request.user)
    if product_to_add not in watchlist.products.all():
        watchlist.products.add(product_to_add)
        watchlist.save()
        quantity = Quantity.objects.create(user = request.user, products = product_to_add, quantity = 1 )
        quantity.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def increase_quantity(request, product):
    product_to_add = Product.objects.get(id=product)
    quantity = Quantity.objects.filter(user = request.user).filter(products = product_to_add)
    quantity = Quantity.objects.get(id = quantity[0].id)
    quantity.quantity = quantity.quantity + 1
    quantity.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def decrease_quantity(request, product):
    product_to_add = Product.objects.get(id=product)
    quantity = Quantity.objects.filter(user = request.user).filter(products = product_to_add)
    quantity = Quantity.objects.get(id = quantity[0].id)
    quantity.quantity = quantity.quantity - 1
    quantity.save()
    if (quantity.quantity < 1):
        return remove_watchlist(request, product)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_watchlist(request, product):
    product_to_add = Product.objects.get(id=product)
    watchlist = Watchlist.objects.get(user=request.user)
    if product_to_add in watchlist.products.all():
        watchlist.products.remove(product_to_add)
        watchlist.save()
        quantity = Quantity.objects.filter(user = request.user).filter(products = product_to_add)
        quantity = Quantity.objects.get(id = quantity[0].id)
        quantity.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))