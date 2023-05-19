from django.shortcuts import render,redirect
from core.models import Customers,Product,Order,Session_model,Category,CategoryofCategories
from django.contrib.auth.decorators import login_required
# Create your views here.





def dashboard(request):
    session_id=request.COOKIES.get('session_id')
    
    if session_id is not None:
        try:
            sessioncust=Session_model.objects.get(session_id=session_id)
            print(sessioncust.user.Name)
            u=sessioncust.user
            print(u.id)
            cust=Customers.objects.get(id=u.id)
            if not cust.is_superuser and not cust.is_staff:
                hecan=False
                return redirect('base:home')
            hecan=True
        except:
            print("not login")




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
            print(u.id)
            cust=Customers.objects.get(id=u.id)
            if not cust.is_superuser and not cust.is_staff:
                hecan=False
                return redirect('base:home')
            hecan=True
        except:
            print("not login")
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
            print(u.id)
            cust=Customers.objects.get(id=u.id)
            if not cust.is_superuser and not cust.is_staff:
                hecan=False
                return redirect('base:home')
            hecan=True
        except:
            print("not login")
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
            print(u.id)
            cust=Customers.objects.get(id=u.id)
            if not cust.is_superuser and not cust.is_staff:
                hecan=False
                return redirect('base:home')
            hecan=True
        except:
            print("not login")
    category_of_categories=CategoryofCategories.objects.all().order_by('categoryfrom')
    print(category_of_categories)
    context={
    'category_of_categories':category_of_categories,
    }
    return render(request,'admindashboard_templates/home.html',context)