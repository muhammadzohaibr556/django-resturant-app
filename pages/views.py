from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
#from django.views.generic import TemplateView, DetailView, ListView
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from resturant.models import Branches,Halls,HallMeal
from reservation.models import Reserve_Halls
from delivery.models import Item,Person
from cart.forms import CartAddProductForm
from cart.cart import Cart
from datetime import date
from django.views.generic import *

# Create your views here.

def homeView(request):
    item = Item.objects.all()
    branch = Branches.objects.all()
    hall = Halls.objects.all()
    hallmeal = HallMeal.objects.all()
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    if not cart:
        context = {
            'item':item,
            'cart_product_form':cart_product_form,
            'branch':branch,
            'halls':hall,
            'hallmeal':hallmeal,
            'hall':'show',
            'meal':'',
            'deal':''
        }
    else:
        for itm in cart:
            products = Item.objects.get(title=itm['product'])
            if products.category=='Meal':
                context = {
                    'item':item,
                    'cart_product_form':cart_product_form,
                    'branch':branch,
                    'halls':hall,
                    'hallmeal':hallmeal,
                    'hall':'',
                    'meal':'show',
                    'deal':''
                }
            if products.category=='Deal':
                context = {
                    'item':item,
                    'cart_product_form':cart_product_form,
                    'branch':branch,
                    'halls':hall,
                    'hallmeal':hallmeal,
                    'hall':'',
                    'meal':'',
                    'deal':'show'
                }
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request,"pages/home.html",context)

class aboutDetailView(DetailView):
    model = Branches
    templat_name = "pages/about.html"
    context_object_name = 'post'

def aboutView(request):
    brh = Branches.objects.all()
    context = {
        'branch':brh
    }
    return render(request,"pages/about.html",context)

class servicesTemplateView(TemplateView):
    template_name = "pages/services.html"
def servicesView(request):
    return render(request,"pages/services.html")

def thankView(request,pk,status):
    if status!="h":
        psn = Person.objects.get(pk=pk)
        #pern = Person.objects.get(id=int(psn))
        
        if status=='o':
            context = {
                'person':psn.name+'. You will get Home Delivery within 30 minutes',
                'status':' Again for your Order'
            }
        elif status=='n':
            context = {
                'person':psn.name+'. You will get Home Delivery within 30 minutes',
                'status':' for your Order'
            }
    else:
        psn = Reserve_Halls.objects.get(pk=pk)
        status = 'for your Reservation of '+str(psn.hall)
        context={
            'status':status,
            'person':psn.Name+'. Visit our nearest resturant for conformation.',

        }
    return render(request,"pages/thank.html",context)

def aboutDetailView(request,pk):
    brh = Branches.objects.get(pk=pk)
    context = {
        'branch':brh
    }
    return render(request,"pages/about_detail.html",context)

def select(request,id):
    if request.method=='GET' and request.is_ajax():
        response_data =''
        branch = Branches.objects.get(id=id)
        hall = list(Halls.objects.filter(branch_in=branch).values())
        data = dict()
        data['halls'] = hall
        return JsonResponse(data)
    else:
        return HttpResponse("Nothing to see:")

@require_POST

def cart_add_home(request, id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    
    return redirect('home')

def cart_remove_home(request, id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=id)
    cart.remove(product)
    return redirect('home')

def reserve(request):
    if request.method == 'POST':
        branch = request.POST['branch']
        hall = request.POST['hall']
        size = request.POST['size']
        date = request.POST['date']
        time = request.POST['time']
        meal = request.POST['meal']
        y_name = request.POST['y_name']
        phone = request.POST['phone']
        email = request.POST['email']
        charges = request.POST['charges']
        Hall = Halls.objects.get(id=hall)
        Meal = HallMeal.objects.get(id=meal)
        reserve = Reserve_Halls(Name=y_name, Phone_no=phone, Email=email, Party_size=size, Date=date, Time=time, hall=Hall,meal_type=Meal, charges=charges)
        reserve.save()
        reserve_id = int(reserve.id)
        status ="h"
        return redirect('thank',reserve_id,status)
    else:
        return redirect('home')
    
def hall_charges(request,id):
    if request.method=='GET' and request.is_ajax():
        charges = Halls.objects.get(id=id)
        return HttpResponse(charges.charges_per_head)
    else:
        return HttpResponse("Nothing To See")

def check(request):
    if request.method=='GET' and request.is_ajax():
        queryset_list = Reserve_Halls.objects.all()
        rhall = list(queryset_list.filter(Date__gte=date.today()).values())
        data = dict()
        data['rhalls'] = rhall
        #rhall = queryset_list.filter(Date__gte=date.today())
        return JsonResponse(data)
        #return HttpResponse(rhall)
    else:
        return HttpResponse("Nothing To See")
