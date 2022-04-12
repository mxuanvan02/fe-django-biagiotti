from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'pages/home.html', {})

def aboutus(request):
  return render(request, 'pages/about-us.html', {})

def blogStandard(request):
  return render(request, 'pages/blog-standard.html')

def portfolio(request):
  return render(request, 'pages/portfolio.html')

def contact(request):
  return render(request, 'pages/contact.html')

# Products

def productsList(request):
  return render(request, 'pages/products/list.html')

def productDetail(request):
  return render(request, 'pages/products/detail.html')

# Shops

def account(request):
  return render(request, 'pages/shops/account.html')

def lostPassword(request):
  return render(request, 'pages/shops/lost-password.html')

def cart(request):
  return render(request, 'pages/shops/cart.html')

def orderTracking(request):
  return render(request, 'pages/shops/order-tracking.html')

def wishlist(request):
  return render(request, 'pages/shops/wishlist.html')