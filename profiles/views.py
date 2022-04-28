''' Required imports '''
from django.core.exceptions import MultipleObjectsReturned
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Order
from products.models import Product, Category
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    '''This displays the users profile'''
    profile = get_object_or_404(UserProfile, user=request.user)
    usertype = request.user.is_superuser
    products = Product.objects.all()


    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile was sucessfully updated!')
        else:
            messages.add_message(request, messages.ERROR,
            'Update failure, please check your form is valid!')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    # the error is point to this line
    template = 'profiles/profile.html'
    context = {
        'profile':profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'usertype': usertype,
        'products': products,
    }
    return render(request, template, context)


@login_required
def order_history(request, order_number):
    ''' List out users previous orders '''
    order = get_object_or_404(Order, order_number=order_number)

    messages.add_message(request, messages.INFO,
    f'This is a previous confirmation order num: {order_number}. A confirmation was alreadly sent.')

    template = 'checkout/my_checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
