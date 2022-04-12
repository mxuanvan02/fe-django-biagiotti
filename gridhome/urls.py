from django.urls import path
from gridhome import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about-us', views.aboutus, name='aboutus'),
  path('blog-standard', views.blogStandard, name='blog-standard'),
  path('portfolio', views.portfolio, name='portfolio'),
  path('contact', views.contact, name='contact'),
  path('product-list', views.productsList, name='product-list'),
  path('product-detail', views.productDetail, name='product-detail'),
  path('shop-account', views.account, name='shop-account'),
  path('shop-lost-password', views.lostPassword, name='lost-password'),
  path('shop-cart', views.cart, name='shop-cart'),
  path('shop-order-tracking', views.orderTracking, name='shop-order-tracking'),
  path('shop-wishlist', views.wishlist, name='shop-wishlist'),
]