from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm
# Create your views here.

def showProducts(request):
    products = Product.objects.all()
    user_count = User.objects.count()
    product_count = Product.objects.count()
    context = {
        'products' : products,
        'u_c' : user_count,
        'p_c' : product_count
    }
    return render(request, 'ProductManagement/products.html', context)


def showDetails(request, product_id):
    searched_product = get_object_or_404(Product, id=product_id)
    context = {
        'search': searched_product
    }

    return render(request, 'ProductManagement/detail_product_view.html', context)

def uploadProducts(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid:
            form.save()
            return redirect('products_list')

    context = {
        'form' : form
    }

    return render(request, 'ProductManagement/upload.html', context)
