from django.shortcuts import render, redirect
from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Person, OrderItem
from resturant.models import Branches
#from django.views.generic import TemplateView
# Create your views here.
'''class  CartView(TemplateView):
    template_name = 'delivery/cart.html' '''

def cartView(request):
    cart = Cart(request)
    if not cart:
        context={
            'orderbtn':'d-none'
        }
    else:
        context={
            'orderbtn':'',
            'branch':Branches.objects.all()
        }
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render (request,"delivery/cart.html",context)

def orderView(request):
    cart = Cart(request)
    if request.method == 'POST':
        name = request.POST['nam']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        postal = request.POST['postal']
        branh = request.POST['branch']
        total = request.POST['total']
        
        order, created = Person.objects.get_or_create(name=name, phone=phone, email=email, address=address, postal_code=postal)
        
        person_id = 0
        for item in cart:
            OrderItem.objects.create(order=order,
                        item=item['product'],
                        price=total,
                        quantity=item['quantity'],
                        from_branch=Branches.objects.get(name=branh))
        person_id = int(order.id)
        if created==False:
            status = 'o'
        elif created==True:
            status = 'n'
    cart.clear()    
    return redirect('thank',person_id,status)
        
