from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from delivery.models import Item
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    
    return redirect('cart')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=id)
    cart.remove(product)
    
    return redirect('cart')


def cart_detail(request):
    return redirect ('cart')