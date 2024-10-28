from django.db import models

# Create your models here.


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  
    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    image_profile = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  
    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

class Subscriptions(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    discount_percentage = models.DecimalField(max_digits=3, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2) 
    class Meta:
        db_table = "subscriptions"
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "reviews"
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "payments"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

class Returns(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "returns"
        verbose_name = "Return"
        verbose_name_plural = "Returns"