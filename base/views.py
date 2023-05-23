from django.shortcuts import render,redirect
from core.models import Customers,Session_model,Product,Category,CategoryofCategories,Order
from core.forms import Customers_forms
from .forms import Customers_forms1
from django.urls import reverse
import uuid
# Create your views here.

def fornav(request,authent):
   
         
    context={
          'authent':authent,
     }
    return render(request,'navbar.html',context)

def home(request):
    u=""
    cat=""
    pro=None
    searched=None
    session_id=request.COOKIES.get('session_id')
    the_dicts=[]
    the_categories=[]
    if session_id is not None:
         authent=True
    else:
         authent=False
    try:
        sessioncust=Session_model.objects.get(session_id=session_id)
        print(sessioncust.user.Name)
        u=sessioncust.user
        print(u.id)
    except:
         print("not login")

    
    #call for models

    products=Product.objects.all().order_by('Date_created')[:20]
    categories=Category.objects.all()

    for c in categories:
        
         the_categories.append(c.category_name)
        
         cat=c.categoryofcategories_set.all()
         for ca in cat:
              the_dict = {'name': c.category_name, 'subcategory': ca.category_name}
              the_dicts.append(the_dict)
             

    


    if request.method == 'POST':
            searched = request.POST.get('searched')
            pro=Product.objects.filter(product_name__contains=searched)
            
            context={'dictionary':the_dicts,
             'products':pro,
             'the_categories':the_categories,
             'authent':authent,}
    else:
         context={'dictionary':the_dicts,
             'products':products,
             'the_categories':the_categories,
             'authent':authent,}
    
    return render(request,'base_templates/home.html',context)

def log(request):
    
    b=True
    user1=""
    form=Customers_forms1()
    if request.method=='POST':
        form=Customers_forms1(request.POST)
        Email=request.POST.get('Email')  
        password=request.POST.get('password')
        
        try:
                user = Customers.objects.get(Email=Email)
                user1=user
                print(user1)
                while True:
                        # Generate a random UUID for the session
                        session_id = str(uuid.uuid4())

                        try:
                            # Try to create a session with the generated session_id
                            session = Session_model.objects.create(session_id=session_id, user=user)
                            print("success")
                            break
                        except :
                            # If a session with the same session_id already exists, generate a new one
                            continue

                    # Set the session_id cookie and redirect to the home page

                if user.is_staff or user.is_superuser:
                     response = redirect('dashboard')
                
                     #setup a gate to dashboard app
                else:    
                    response = redirect('base:home')
                response.set_cookie('session_id', session.session_id)
                return response
                

        except Customers.DoesNotExist:
            print("nonono")
            
            
            
        print("yes")
        
    context={
        'form':form,
    }

    return render(request,'base_templates/loginform.html',context)
 

def logo(request):
    
    session_id=request.COOKIES.get('session_id')
    print(session_id)
    if session_id:
         
        response = redirect('base:home')
        response.delete_cookie('session_id')
        print("yes")
        return response

    context={
        
    }
    return render(request,'base_templates/home.html',context)


def reg(request):

    n="nothing"
    form=Customers_forms()
    if request.method=='POST':
        mail=request.POST.get('Email')
        print(mail)
        form=Customers_forms(request.POST)
        if form.is_valid():


            try:
                n=None
                n=Customers.objects.get(Email=mail)
                print("sorry we already have that name")
                
            except:
                user=Customers.objects.create(
                    Name=request.POST.get('Name'),
                    Username=request.POST.get('Username'),
                    Email=request.POST.get('Email'),
                    password=request.POST.get('password')
                )

                return redirect('home')
                
                
            
            
                
                

    context={
        'form':form,
    }
    return render(request,'base_templates/registerform.html',context)



def details(request,pk):
     session_id=request.COOKIES.get('session_id')

     orders=""
     u=""
     products=Product.objects.get(id=pk)
     authent=False
     
          
     try:
        sessioncust=Session_model.objects.get(session_id=session_id)
        print(sessioncust.user.Name)
        u=sessioncust.user
        authent=True
     except:
        print("not login")
        return redirect('base:log')
     if request.method=='POST' :
          count=request.POST.get('quantity')
          o=Order.objects.create(
               order_product=products,
               order_user=u,
               order_count=count
          )
          
          #delete
          fornav(request,authent)
          print(authent)
          return redirect('base:details', pk=pk)

        
     orders=Order.objects.filter(order_user=u.id)

     context={'product':products,'orders':orders,
              'authent':authent,}

     return render(request,'base_templates/details.html',context)


def orderdelete(request,order_id):
     
     
    order =Order.objects.get(id=order_id)
    order.delete()
    return redirect('base:details', pk=order.order_product.id)



