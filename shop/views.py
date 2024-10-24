from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Product, Cart, Order, Facture, Category
User = get_user_model()
# Create your views here.

def index(request):
    products = Product.objects.all()
    categorie = Category.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != "" and item_name is not None:
        products = Product.objects.filter(title__icontains=item_name)
    return render(request, "index.html", context={"products": products, "categorie": categorie})

def categories(request, name):
    categorie = Category.objects.all()
    categoris = get_object_or_404(Category, name=name)
    products = Product.objects.filter(category=categoris)
    return render(request, "categorie.html", context={"categoris": categoris, "products": products, "categorie": categorie})
def product_detail(request, slug):
    categorie = Category.objects.all()
    product = get_object_or_404(Product, slug=slug)
    return render(request, "detail.html", context={"product": product, "categorie": categorie})

# def contact(request):
#     return render(request, "contact.html")
def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)
    if created:
        cart.ordered.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.total_price = order.product.price * order.quantity
        order.save()
    return redirect(reverse("product", kwargs={"slug": slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    orders = cart.ordered.all()
    return render(request, "cart.html", context={"orders": orders})

def add_product(request, myid):
    user = request.user
    product = get_object_or_404(Product, id=myid)
    cart, _ = Cart.objects.get_or_create(user=user)
    counter, _ = Order.objects.get_or_create(user=user, product=product)
    counter.quantity += 1
    counter.total_price = counter.product.price * counter.quantity
    counter.save()
    return redirect('cart')

def del_product(request, myid):
    user = request.user
    product = get_object_or_404(Product, id=myid)
    cart, _ = Cart.objects.get_or_create(user=user)
    orders, _ = Order.objects.get_or_create(user=user, product=product)
    orders.quantity -= 1
    orders.total_price = orders.product.price * orders.quantity
    orders.save()
    return redirect('cart')


def order(request):
    cart = get_object_or_404(Cart, user=request.user)
    orders = cart.ordered.all()
    return render(request, "order.html", context={"orders": orders})

def contact(request):
    if request.method == "POST":
        return redirect('contact_success')
    return render(request, 'contact.html')


def contact_success(request):
    return render(request, "contact_success.html")