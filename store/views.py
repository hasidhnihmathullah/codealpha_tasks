from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product, Order, OrderItem

def index(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    total_qty = 0

    for pid, qty in cart.items():
        prod = Product.objects.filter(id=int(pid)).first()
        if prod:
            subtotal = prod.price * qty
            cart_total += subtotal
            total_qty += qty
            cart_items.append({
                'product': prod,
                'qty': qty,
                'subtotal': subtotal
            })

    user_orders = []
    if request.user.is_authenticated:
        user_orders = Order.objects.filter(user=request.user).order_by('-created_at')

    # Auth form modal submissions
    if request.method == 'POST':
        if 'login' in request.POST:
            u = request.POST.get('username')
            p = request.POST.get('password')
            user = authenticate(request, username=u, password=p)
            if user:
                login(request, user)
            return redirect('index')
        elif 'register' in request.POST:
            u = request.POST.get('username')
            p = request.POST.get('password')
            if not User.objects.filter(username=u).exists():
                user = User.objects.create_user(username=u, password=p)
                login(request, user)
            return redirect('index')

    return render(request, 'index.html', {
        'products': products,
        'cart_items': cart_items,
        'cart_total': f"{cart_total:.2f}",
        'cart_count': total_qty,
        'orders': user_orders,
    })

def add_to_cart(request, pk=None, product_id=None):
    # Accepts either 'pk' or 'product_id' from urls.py
    item_id = pk if pk is not None else product_id
    product = get_object_or_404(Product, id=item_id)
    
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    request.session.modified = True

    cart_items = []
    cart_total = 0
    total_qty = 0
    for pid, qty in cart.items():
        prod = Product.objects.filter(id=int(pid)).first()
        if prod:
            subtotal = prod.price * qty
            cart_total += subtotal
            total_qty += qty
            cart_items.append({
                'id': prod.id,
                'name': prod.name,
                'price': float(prod.price),
                'qty': qty,
                'subtotal': float(subtotal)
            })

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('ajax'):
        return JsonResponse({
            'status': 'success',
            'cart_count': total_qty,
            'cart_total': f"{cart_total:.2f}",
            'cart_items': cart_items
        })
    return redirect('index')

def remove_from_cart(request, pk=None, product_id=None):
    item_id = str(pk if pk is not None else product_id)
    cart = request.session.get('cart', {})
    if item_id in cart:
        del cart[item_id]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('index')

def clear_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('index')

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('index')

    cart = request.session.get('cart', {})
    if not cart:
        return redirect('index')

    total_price = 0
    items_to_create = []
    for pid, qty in cart.items():
        prod = Product.objects.filter(id=int(pid)).first()
        if prod:
            total_price += prod.price * qty
            items_to_create.append((prod, qty, prod.price))

    if items_to_create:
        order = Order.objects.create(user=request.user, total_price=total_price)
        for prod, qty, price in items_to_create:
            OrderItem.objects.create(
                order=order,
                product=prod,
                quantity=qty,
                price=price
            )

        request.session['cart'] = {}
        request.session.modified = True
        return redirect(f'/?order_success={order.id}')

    return redirect('index')

def user_logout(request):
    logout(request)
    return redirect('index')