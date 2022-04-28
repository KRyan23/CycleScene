from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                messages.add_message(request, messages.WARNING,
                'Were Sorry But Your Search Criteria Was Blank, \
                so we have listed all of our products for you!')
                return redirect(reverse('products'))

            queries = ( Q(name__icontains=query) |
            Q(description__icontains=query) | Q(highlights__icontains=query) )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }
    if query:
        messages.add_message(request, messages.INFO,
        f'Here Are Your Search Requests For "{query.upper()}"')

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    ''' Let a superuser add product to store '''
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR, 'Only Superusers Can Add Products!')
        return redirect(reverse('account_login'))

    if request.method == 'POST':

        profile = get_object_or_404(UserProfile, user=request.user)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.add_message(request, messages.SUCCESS, 'Product Added Successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.add_message(request, messages.ERROR,
            'Failure to add the product. Please check form is valid!')
    else:
        form =ProductForm()
        profile = get_object_or_404(UserProfile, user=request.user)
    template = 'products/add_products.html'
    context = {
            'form': form,
            'profile': profile,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    ''' Let a superuser edit a product in the store '''
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR, 'Only Superusers Can Add Products!')
        return redirect(reverse('account_login'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
            f'Sucessfully updated product { product.name.lower().title() }')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.add_message(request, messages.ERROR,
            'Failure to update product. Please check form is valid!')
    else:
        form = ProductForm(instance=product)
        profile = get_object_or_404(UserProfile, user=request.user)
        messages.add_message(request, messages.INFO,
        f'You are currently editing "{ product.name.lower().title() }"')

    template = 'products/edit_products.html'
    context = {
            'form': form,
            'profile': profile,
            'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    ''' Let a superuser remove a product in the store '''
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR, 'Only Superusers Can Add Products!')
        return redirect(reverse('account_login'))

    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    product.delete()
    messages.add_message(request, messages.SUCCESS, f'Sucessfully Deleted Product { product.name }')
    return redirect(reverse('profile'))
