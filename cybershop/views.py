from django.shortcuts import render, get_object_or_404
from shop.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .utils import *


def index(request):
    # Produits récemment ajoutés
    nouveaux = Product.objects.all().order_by('-create_at')[:15]

    # Produits les plus vus ces derniers jours
    tendances = Product.objects.annotate(
        nb_view=Count("productview")
    ).order_by("-nb_view", "-productview__viewed_at").distinct()[:15]

    context = {
        'nouveaux': nouveaux,
        'tendances': tendances,
    }

    if request.user.is_authenticated:
        recommendations = global_recommendations(request.user)
        if not recommendations:
        	context['recommendations'] = Product.objects.all().order_by('?')[:10]
        else:
        	context['recommendations'] = recommendations
    print(context)
    return render(request, 'index.html', context=context)



def itemview(request, id):
    product = get_object_or_404(Product, id=id)

    if request.user.is_authenticated:
        ProductView.objects.create(user=request.user, product=product)

    similar = mini_recommendation(product.id)

    context = {
        'product': product,
        'similar': similar,
    }

    return render(request, 'itemview.html', context=context)


@login_required
def register_product_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product = Product.objects.filter(id=product_id).first()
            if product:
                ProductView.objects.create(user=request.user, product=product)
                return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)