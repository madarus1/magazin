class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        id_product_add = str(product.id)
        if id_product_add in self.cart and quantity < product.stock:
            self.cart[id_product_add]["quantity"] += quantity
        else:
            self.cart[id_product_add] = {
                "quantity": quantity,
                "price": str(product.price)
            }
        self.save()

# удаляет один продукт
    def reduce(self, product, quantity=1):
        id_product_reduce = str(product.id)
        if id_product_reduce in self.cart and self.cart[id_product_reduce]["quantity"] > 1:
            self.cart[id_product_reduce]["quantity"] -= quantity
        else:
            del self.cart[id_product_reduce]
        self.save()

# удаляет весь продукт(один товар)
    def remove(self, product):
        id_product_add = str(product.id)
        if id_product_add in self.cart:
            del self.cart[id_product_add]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session["cart"] = {}
        self.save()

    def update(self, product_id, quantity):
        prodid = str(product_id)
        if prodid in self.cart:
            self.cart[prodid]["quantity"] = quantity
            self.save


















































    def __iter__(self):
        from shop.models import Product
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            cart_item = self.cart[str(product.id)]
            cart_item["product"] = product
            cart_item["total_price"] = float(cart_item["price"]) * cart_item["quantity"]
            yield cart_item 































