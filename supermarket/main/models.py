from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    description = models.TextField(blank=True)
    image=models.ImageField(upload_to='cat_images',null=True,blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class AllItems(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    oldprice=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/',blank=True)
    stock_quantity = models.PositiveIntegerField(default=50)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    allitems = models.ForeignKey(AllItems, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0,null=True)
    # payment = models.CharField(max_length=100,null=True)
    # status = models.CharField(max_length=100,null=True)
    # delivery = models.CharField(max_length=100,null=True)
    total = models.CharField(max_length=100,null=True)
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(AllItems, on_delete=models.CASCADE)
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    address=models.TextField(null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    pin_code=models.CharField(max_length=200,null=True)
    total_price=models.FloatField(null=True)
    payment_mode=models.CharField(max_length=200,null=True)
    # payment_id=models.CharField(max_length=200,null=True)
    orderstatuses=(
            ('pending','pending'),
            ('out for shippig','out for shippig'),
            ('completed','completed'),
        )
    status=models.CharField(max_length=200,choices=orderstatuses,default='pending',null=True)
    message=models.TextField(null=True,blank=True)
    # tracking_no=models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)
    
    def __str__(self):
        return self.name
    
class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(AllItems,on_delete=models.CASCADE)  
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)  
    
