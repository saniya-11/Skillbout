from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_form.html', {'products': products})

@csrf_exempt
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('ProductName')
        price = request.POST.get('productPrice')
        desc = request.POST.get('productDescription')
        Product.objects.create(ProductName=name, productPrice=price, productDescription=desc)
        return JsonResponse({'success': True})

@csrf_exempt
def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.ProductName = request.POST.get('ProductName')
        product.productPrice = request.POST.get('productPrice')
        product.productDescription = request.POST.get('productDescription')
        product.save()
        return JsonResponse({'success': True})
    return render(request, 'product_form.html', {'product': product, 'edit': True})

@csrf_exempt
def product_delete(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        product.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'})