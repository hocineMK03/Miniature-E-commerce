from django.urls import path,include
from . import views


app_name = 'base'
urlpatterns = [
    path('home',views.home,name="home"),
    path('login',views.log,name="log"),
    path('reg',views.reg,name="reg"),
    path('logo',views.logo,name="logo"),
    path('details<int:pk>',views.details,name="details"),
     path('delete_order/<int:order_id>/', views.orderdelete, name='delete_order'),
]