from .models import Category
from .models import Order
def categories_processor(request):
    categories = Category.objects.all()
    context={
        'categories':categories
    }
    return context

def cart_quantity(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    return {'cartItems': cartItems}

