from django.urls import path,include
from . import views
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
    path('addproducts',views.addproducts,name="addproducts"),
    path('addorders',views.addorders,name="addorders"),
    path('addcategories',views.addcategories,name="addcategories"),
    path('adddata<str:whichone>',views.adddata,name="adddata"),
    path('delete/customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('delete/product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete/order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('delete/category/<int:category_id>/', views.delete_category, name='delete_category'),
]