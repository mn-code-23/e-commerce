from shopper.settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=180)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=180)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    desc = models.TextField()
    image = models.ImageField(upload_to="static/products/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=1.0)
    ordered_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.title} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.ManyToManyField(Order)
    ordered_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Facture(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=180)

    # def __str__(self):
    #     return self.user.username


