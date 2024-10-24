from django.urls import path
from .views import index, product_detail, add_to_cart, cart, add_product, del_product, order, categories, contact, contact_success

urlpatterns = [
    path('', index, name="index"),
    path('product/<str:slug>/', product_detail, name="product"),
    path('category/<str:name>/', categories, name="categories"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('cart/', cart, name="cart"),
    path('cart/add/<int:myid>/', add_product, name="add-product"),
    path('cart/delete/<int:myid>/', del_product, name="del-product"),
    path('cart/order/', order, name="order"),
    path('contact/', contact, name="contact"),
    path('contact/contact_success', contact_success, name="contact_success")
]



















# path('contact/success/', contact_success, name='contact_success'),