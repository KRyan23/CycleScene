''' Required imports '''
import json
import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from products.models import Product
from shoppingbag.contexts import shoppingbag_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from .forms import OrderForm
from .models import Order, OrderLineItem

# Mostly from BA project



@login_required
@require_POST
def cache_checkout_data(request):
    ''' cache user data in order to save info in the event of a unexpected event'''
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'shoppingbag': json.dumps(request.session.get('shoppingbag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Were sorry your payment was not successful \
            Please try again later.')
        return HttpResponse(content=e, status=400)

@login_required
def checkout(request):
    ''' handle checkout requests and save to order '''
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('shopping_bag', {})
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'mobile_number': request.POST['mobile_number'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'county': request.POST['county'],
            'city': request.POST['city'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_shoppingbag = json.dumps(bag)
            order.user_profile = UserProfile.objects.get(user=request.user)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "A products in your bag wasn't found in our \
                        database. Please call us on (01) 8551522")
                    )
                    order.delete()
                    return redirect(reverse('view_shoppingbag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('my_checkout_success', args=[order.order_number]))
        else:
            messages.error(request,
            'There was an error with your form. Please double check your info.')
    else:
        shoppingbag = request.session.get('shopping_bag', {})
        if not shoppingbag:
            messages.error(request, "your shopping bag is currently empty!")
            return redirect(reverse('home'))

        current_bag = shoppingbag_contents(request)
        total = current_bag['bagtotal']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': profile.user.first_name,
                    'last_name': profile.user.last_name,
                    'email': profile.user.email,
                    'mobile_number': profile.default_mobile_phone,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'city': profile.default_city,
                    'address1': profile.default_address1,
                    'address2': profile.default_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'stripe Public key missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required()
def my_checkout_success(request, order_number):
    ''' used to handle checkout success '''
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        #This will attach the order to the users profile
        order.user_profile = profile
        order.save()
        #Save the users information
        if save_info:
            profile_data = {
                'default_mobile_phone': order.mobile_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_city': order.city,
                'default_address1': order.address1,
                'default_address2': order.address2,
                'default_county': order.county,
            }
            
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.add_message(request, messages.SUCCESS,
        f'Great your order has been successfully processed!\
        Reference: {order} \
        Confirmation email will be sent to {order.email}. ')

    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    template = 'checkout/my_checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
