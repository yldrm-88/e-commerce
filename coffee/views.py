from django.shortcuts import render
from .models import*
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import JsonResponse
import json
import datetime
# Create your views here.

#Ana sayfam
def homepage(request):
    return render(request,'homepage.html')

#Ürünleri listelediğim sayfam
def coffee(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    #search kısmım
    search=""
    if request.GET.get("search"):
        search=request.GET.get("search")
        products=products.filter(
            Q(name__icontains=search) |
            Q(category__name__icontains=search)
        )
    #sayfalama yaptığım kısmım
    paginator=Paginator(products,8)
    page=request.GET.get('page')

    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'categories': categories,
        'search':search,
    }
    return render(request, 'coffee.html', context)

#Sepet kısmım
def detail(request):
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'detail.html', context)



def checkout(request):
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)


#ürün hakkında bilgilendiğim ve sepete eklediğim kısmım
def coffeeAbout(request,id):
    product=Product.objects.get(id=id)
    context={
        'product':product,
    }
    return render(request,'coffeeAbout.html',context)

def category(request,category_id):
    products=Product.objects.filter(category_id=category_id)
    context={
        'products':products,
    }
    return render(request,'category.html',context)



def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print('Action',action)
    print('Product ID',productId)

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)

    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)

    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action =='remove':
        orderItem.quantity=(orderItem.quantity-1)
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)



def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    print(data)
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        total = float(data['form']['total'])
        order.transaction_id=transaction_id

        if total == order.get_cart_total:
            order.complete=True
        order.save()

        if order.shipping == True:
            ShippingOrder.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                street=data['shipping']['street'],
            )

    else:
        print('Kullanıcı giriş yapmadı...')
    return JsonResponse('Ödeme Tamamlandı',safe=False)