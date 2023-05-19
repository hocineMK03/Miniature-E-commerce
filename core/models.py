from django.db import models
import re
# Create your models here.


#users
class Customers(models.Model):
    Name=models.TextField(null=False)
    Username=models.TextField(null=True) #optionel
    Email=models.TextField(null=False ,max_length=30)
    password=models.TextField()
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    
    def Email_valid(Email):
        pattern = r'^[a-zA-Z0-9]+([_.+%-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        match = re.search(pattern,Email)
        return bool(match)
    
class Session_model(models.Model):
    session_id = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)





#product

class Category(models.Model):
    category_name=models.TextField(max_length=15)
    class Meta:
        verbose_name_plural = 'categories'
        
class CategoryofCategories(models.Model):

    category_name=models.TextField(max_length=15)
    categoryfrom=models.ForeignKey(Category,on_delete=models.CASCADE)
    
class Product(models.Model):

    product_name=models.TextField(max_length=15)
    product_info=models.TextField(null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    Date_created=models.DateTimeField(auto_now_add=True)
    product_price=models.DecimalField(max_digits=6, decimal_places=2,null=False)
    product_image=models.ImageField(upload_to='static/images/')
    product_stock=models.IntegerField(default=0)
    product_categoryofcategories=models.ForeignKey(CategoryofCategories,on_delete=models.CASCADE)
    


class Order(models.Model):
    order_product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_user=models.ForeignKey(Customers,on_delete=models.CASCADE)
    Date_created=models.DateTimeField(auto_now_add=True)
    order_count=models.IntegerField(default=0)
    
