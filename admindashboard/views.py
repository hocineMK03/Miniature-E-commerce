from django.shortcuts import render,redirect
from core.models import Customers,Product,Order,Session_model,Category,CategoryofCategories
from django.contrib.auth.decorators import login_required
from .forms import Customers_forms,Products_forms
from django.contrib import messages
# Create your views here.





def dashboard(request):
    session_id=request.COOKIES.get('session_id')
    
    if session_id is not None:
        try:
            sessioncust=Session_model.objects.get(session_id=session_id)
            print(sessioncust.user.Name)
            u=sessioncust.user
           
            cust=Customers.objects.get(id=u.id)
            if not cust.is_superuser and not cust.is_staff:
                return redirect('base:home')
            
        except:
            print("not login")
            return redirect('base:home')
           
    else:
        return redirect('base:home')




    customers=Customers.objects.all()
    
    
    
   
    
    context={
        'customers':customers,
        
        
        
    }
    
    
    return render(request,'admindashboard_templates/home.html',context)




def addproducts(request):
    session_id=request.COOKIES.get('session_id')
    
    if session_id is not None:
        try:
            sessioncust=Session_model.objects.get(session_id=session_id)
            print(sessioncust.user.Name)
            u=sessioncust.user
           
            cust=Customers.objects.get(id=u.id)
            if not cust.is_superuser and not cust.is_staff:
                return redirect('base:home')
            
        except:
            print("not login")
            return redirect('base:home')
           
    else:
        return redirect('base:home')
    products=Product.objects.all().order_by('category')
    context={
    'products':products,
    }
    return render(request,'admindashboard_templates/home.html',context)



def addorders(request):
    session_id=request.COOKIES.get('session_id')
    
    if session_id is not None:
        try:
            sessioncust=Session_model.objects.get(session_id=session_id)
            print(sessioncust.user.Name)
            u=sessioncust.user
           
            cust=Customers.objects.get(id=u.id)
            if not cust.is_superuser and not cust.is_staff:
                return redirect('base:home')
            
        except:
            print("not login")
            return redirect('base:home')
           
    else:
        return redirect('base:home')
    orders=Order.objects.all()
    context={
        'orders':orders,
    }
    return render(request,'admindashboard_templates/home.html',context)



def addcategories(request):
    session_id=request.COOKIES.get('session_id')
    
    if session_id is not None:
        try:
            sessioncust=Session_model.objects.get(session_id=session_id)
            print(sessioncust.user.Name)
            u=sessioncust.user
           
            cust=Customers.objects.get(id=u.id)
            if not cust.is_superuser and not cust.is_staff:
                return redirect('base:home')
            
        except:
            print("not login")
            return redirect('base:home')
           
    else:
        return redirect('base:home')
    category_of_categories=CategoryofCategories.objects.all().order_by('categoryfrom')
    print(category_of_categories)
    context={
    'category_of_categories':category_of_categories,
    }
    return render(request,'admindashboard_templates/home.html',context)


def adddata(request,whichone):
    form1=Customers_forms()
    form2=Products_forms()
    
    if request.method=='POST':
        if whichone=="customers":
            
            form1=Customers_forms(request.POST)
            if form1.is_valid():
                
                cust=form1.save(commit=False)
                cust.save()
                return redirect('dashboard')
        elif whichone=="products":
            
            form2=Products_forms(request.POST,request.FILES)
            if form2.is_valid():
                
                prod=form2.save(commit=False)
                prod.save()
                return redirect('addproducts')

    print(whichone)
   
    context={
        'form1':form1,
        'form2':form2,
        'whichone':whichone,
    }
    return render(request,'admindashboard_templates/forms.html',context)



def delete_customer(request, customer_id):
    if request.method == 'POST':
        try:
            customer = Customers.objects.get(id=customer_id)
            customer.delete()
            messages.success(request, 'Customer deleted successfully.')
        except Customers.DoesNotExist:
            messages.error(request, 'Customer not found.')
    return redirect('dashboard')  # Replace 'customer_list' with the URL name of your customers list view

def delete_product(request, product_id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            messages.success(request, 'Product deleted successfully.')
        except Product.DoesNotExist:
            messages.error(request, 'Product not found.')
    return redirect('addproducts')  # Replace 'product_list' with the URL name of your products list view

def delete_order(request, order_id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            messages.success(request, 'Order deleted successfully.')
        except Order.DoesNotExist:
            messages.error(request, 'Order not found.')
    return redirect('addorders')  # Replace 'order_list' with the URL name of your orders list view

def delete_category(request, category_id):
    if request.method == 'POST':
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            messages.success(request, 'Category deleted successfully.')
        except Category.DoesNotExist:
            messages.error(request, 'Category not found.')
    return redirect('addcategories')