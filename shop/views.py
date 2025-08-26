from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from .cart import Cart
from author.models import User

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect("basket")

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("basket")

def reduce_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.reduce(product)
    return redirect("basket")

def catolog(request):
    products = Product.objects.all()
    return render(request, "shop/catolog.html", {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "shop/product_detail.html", {'product': product})

def favorite_products(request, product_id):
    if request.user.is_authenticated:
        user = request.user

        product = get_object_or_404(Product, id=product_id)

        if user.favorite.filter(id=product_id).exists():
            user.favorite.remove(product)
        else:
            user.favorite.add(product)
        
        return redirect("main")
    else:
        return redirect("log_in")

def basket(request):
    cart = Cart(request)
    items = list(cart)
    total = sum(item["total_price"] for item in items)

    errors=[]
        
    print(request.POST)
    if request.method == "POST":
        if "submit_product" in request.POST:
            for name, value in request.POST.items():
                if not name.startwith("quantity_"):
                    continue
                _,product_id = name.split("quantity_", 1)[1]
                try:
                    quant = int(value)
                except (TypeError, ValueError):
                    continue
                if quant > 0:
                    cart.update(product_id, quant)
                else:
                    cart.remove(product_id)
            return redirect("basket")

        if "submit_order" in request.POST:
            name = request.POST.get("customer_name")
            telephone = request.POST.get("cutomer_phone")
            city = request.POST.get("city")
            street = request.POST.get("street")
            house = request.POST.get("house")
            entrance = request.POST.get("entrance")
            apartment = request.POST.get("apartment")

            if not errors:
                order=Order.objects.create(
                    customer_name = name,
                    customer_phone = telephone,
                    city = city,
                    streat = street,
                    house = house,
                    entrance = entrance,
                    apartment = apartment,
                    totalprice = total
                )
                for item in cart:
                    OrderItem.objects.create(
                        order = order,
                        product = item["product"],
                        quantity = item["quantity"],
                    )
                print("работает")
                cart.clear()
                return render(request, "shop/order_created.html", {
                    'order': order
                })
    return render(request, "shop/basket.html", {
        'cart': cart,
        'total': total,
        'items': items,
        'errors':errors
        })