from django.urls import path,include
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('addproducts',views.addproducts,name="addproducts"),
    path('addorders',views.addorders,name="addorders"),
    path('addcategories',views.addcategories,name="addcategories"),
]