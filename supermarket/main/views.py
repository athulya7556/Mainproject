from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Category,Product,Cart,AllItems,Wishlist,Order,OrderItem
from .forms import RegForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView,DetailView,CreateView,DeleteView,View,TemplateView
from django.contrib.auth.models import User
from .forms import Up_product,Up_category,Up_items
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import random

# def admin_home(request):
#     return render(request,'admin/home.html')

def home(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'home.html',context)

    
def products(request,name):
    products=Product.objects.filter(category=name)
    return render(request,'all_products.html',{'products':products})

def allitems(request,name):
    items=AllItems.objects.filter(product=name)
    return render(request,'items.html',{'items':items})

def detail(request,name):
    details=AllItems.objects.get(pk=name)            
    return render(request,'details.html',{'details':details})


def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Registered')
            return redirect(home)
    else:           
        form = RegForm()
    return render(request,'user_reg.html',{'form':form})


def loginpage(request):    
    if request.method == 'POST':
        user = request.POST['username']
        pass1 = request.POST['password']
        user1 =  authenticate(request,username=user,password=pass1)
        if user1:
            login(request,user1)
            messages.success(request,'User has been logged in')
            return redirect(home)
        else:
            messages.error(request,'no such user')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    messages.success(request,'User has been logout')
    return redirect(home)

def search(request):
    search_products=request.GET['search_products']
    get=AllItems.objects.filter(name__icontains=search_products)  
    return render(request,'search_products.html',{'get':get})

    
    
@login_required(login_url='lo')
def viewcart(request):
    cart=Cart.objects.filter(user=request.user) 
    total_price=sum(item.quantity * item.allitems.price for item in cart)
    context={'cart_items':cart,
             'total_price':total_price}
    return render(request,'view_cart.html',context)

@login_required(login_url='lo')
def addcart(request,name):
    item=AllItems.objects.get(pk=name)
    cart_item,created = Cart.objects.get_or_create(allitems=item,user=request.user)
    cart_item.quantity+=1
    cart_item.save() 
    messages.success(request,'Added to cart')      
    return redirect(viewcart)
    
def rejectcart(request,id):
    cart_item=Cart.objects.get(pk=id)
    cart_item.delete()
    return redirect(viewcart)
    
class add_category(CreateView):
    model=Category
    fields='__all__'
    context_object_name='form'
    success_url='admin_home'
    template_name='admin/addcategories.html'
    
    
class add_product(CreateView):
    model=Product
    fields='__all__'
    context_object_name='form'
    success_url='admin_home'
    template_name='admin/add_products.html'
    
class add_items(CreateView):
    model=AllItems
    fields='__all__'
    context_object_name='form'
    success_url='admin_home'
    template_name='admin/add_items.html'
 
def view_category(request):
    view=Category.objects.all()
    return render(request,'admin/view_cat.html',{'view':view})
   
def view_product(request):
    view=Product.objects.all()
    return render(request,'admin/view_products.html',{'view':view})
    
def view_items(request):
    view=AllItems.objects.all()
    return render(request,'admin/view_items.html',{'view':view})
    
def up_pro(request,name):
    a1=Product.objects.get(pk=name)
    if request.method == 'POST':
        form=Up_product(request.POST,request.FILES,instance=a1)
        if form.is_valid():
            form.save()
            return redirect(view_product)
    else:    
        form=Up_product(instance=a1)
    return render(request,'admin/edit_products.html',{'form':form})

def pro_delete(request,name):
    d1=Product.objects.get(pk=name)
    if request.method=='POST':
        d1.delete()
        return redirect(view_product)
    return render(request,'admin/delete_pro.html',{'d1':d1})

def up_category(request,name):
    a1=Category.objects.get(pk=name)
    if request.method == 'POST':
        form=Up_category(request.POST,request.FILES,instance=a1)
        if form.is_valid():
            form.save()
            return redirect(view_category)
    else:    
        form=Up_category(instance=a1)
    return render(request,'admin/edit_cat.html',{'form':form})

def cat_delete(request,name):
    d1=Category.objects.get(pk=name)
    if request.method=='POST':
        d1.delete()
        return redirect(view_category)
    return render(request,'admin/delete_cat.html',{'d1':d1})


def up_items(request,name):
    a1=AllItems.objects.get(pk=name)
    if request.method == 'POST':
        form=Up_items(request.POST,request.FILES,instance=a1)
        if form.is_valid():
            form.save()
            return redirect(view_items)
    else:    
        form=Up_items(instance=a1)
    return render(request,'admin/edit_items.html',{'form':form})

def items_delete(request,name):
    d1=AllItems.objects.get(pk=name)
    if request.method=='POST':
        d1.delete()
        return redirect(view_items)
    return render(request,'admin/delete_items.html',{'d1':d1})

def about(request):
    return render(request,'about.html')


@login_required(login_url='lo')
def wishlist(request):
    wish=Wishlist.objects.filter(user=request.user) 
    return render(request,'wishlist.html',{'wish':wish})

@login_required(login_url='lo')
def add_to_wish(request,name):
    item=AllItems.objects.get(pk=name)
    wish_item,created = Wishlist.objects.get_or_create(items=item,user=request.user)
    wish_item.save() 
    messages.success(request,'Added to wishlist')      
    return redirect(home)
    
def rejectwish(request,id):
    wish_item=Wishlist.objects.get(pk=id)
    wish_item.delete()
    return redirect(wishlist)


# def placed(request):
#     return render(request,'orderplaced.html')

# views.py

def check_available_stock(request):
    products = AllItems.objects.all()
    stock_data = {product.name: product.stock_quantity for product in products}
    return JsonResponse(stock_data)

def check_out_of_stock(request, product_name):
    product = get_object_or_404(AllItems, name=product_name)

    if product.stock_quantity == 0:
        return JsonResponse({'message': f'{product_name} is out of stock.'})
    else:
        return JsonResponse({'message': f'{product_name} is in stock.'})



def payment(request):
    return render(request,'payment.html')

def order_list(request):
    orders = OrderItem.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})


@login_required(login_url='lo')
def placeorder(request):
    if request.method == 'POST':
        neworder=Order()
        neworder.user=request.user
        neworder.name=request.POST.get('name')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.pin_code=request.POST.get('pincode')
        neworder.payment_mode=request.POST.get('payment_mode')
        
        cart=Cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price=cart_total_price + item.allitems.price * item.quantity
         
        neworder.total_price=cart_total_price
        # tractno='sharma'+str(random.randint(1111111,9999999))  
        # while Order.objects.filter(tracking_no=tractno) is None:
        #     tractno='sharma'+str(random.randint(1111111,9999999))  
            
        # neworder.tracking_no=tractno
        neworder.save()  
        
        neworderitems=Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.allitems,
                price=item.allitems.price,
                quantity=item.quantity                
            )  
        orderproduct=AllItems.objects.filter(name=item.allitems).first()
        orderproduct.stock_quantity=orderproduct.stock_quantity - item.quantity
        orderproduct.save()  
        
        # Cart.objects.filter(user=request.user).delete()
        messages.success(request,'your order has been  placed')    

        return redirect(home)
    
    else:
        return render(request,'bill.html')
            
