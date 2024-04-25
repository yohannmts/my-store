from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from store.models import Cart, Order, Products
from django.db.models import Sum

# Create your views here.
def index(request):
    products = Products.objects.all()
    
    return render(request, 'store/index.html', context ={ "products" : products})

def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request,'store/detail.html',context={ "products" : product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Products, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)
   
    if created:
        cart.orders.add(order)
        cart.save()
        # Message flash pour confirmer l'ajout au panier
        messages.success(request, f"L'article '{product.name}' a été ajouté au panier avec succès!")
    else:
        order.quantity += 1
        order.save()
        # Message flash pour indiquer que la quantité a été mise à jour
        messages.info(request, f"La quantité de l'article '{product.name}' a été mise à jour dans votre panier.")

    return redirect(reverse("index"))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    orders = cart.orders.all()
    total_price = sum(order.product.price * order.quantity for order in orders)
    return render(request, 'store/cart.html', {'orders': orders, 'total_price': total_price})


def delete_cart(request):
    if cart:= request.user.cart:
        cart.delete()
    return redirect('index')

def remove_from_cart(request, order_id):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    order = get_object_or_404(Order, id=order_id, user=user, ordered=False)

    # Supprimer l'élément du panier
    cart.orders.remove(order)
    order.delete()

    return redirect('cart')  # Rediriger vers la page du panier après suppression