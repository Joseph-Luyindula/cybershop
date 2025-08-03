from shop.models import Product, ProductView, UserProfile
from django.shortcuts import get_object_or_404


def mini_recommendation(product_id, limit=10):
    try:
        product = Product.objects.get(id=product_id)
        categories = product.category.all()

        similar_products = Product.objects.filter(
            category__in=categories
        ).exclude(id=product.id).distinct()[:limit]
        if similar_products:
        	return Product.objects.all().order_by('?')[:limit]

        return similar_products

    except Product.DoesNotExist:
        print('test')
        return Product.objects.none()


def global_recommendations(user, limit=10):
    profile, _ = UserProfile.objects.get_or_create(user=user)

    recent_views = ProductView.objects.filter(user=user).order_by('-viewed_at')[:10]
    if not recent_views.exists():
        return Product.objects.all().order_by('?')[:limit]

    recent_products = [view.product for view in recent_views]

    # Récupération des ID de catégories
    category_ids = set()
    for product in recent_products:
        category_ids.update(product.category.values_list('id', flat=True))

    # Calcul du prix moyen
    prices = [product.price for product in recent_products]
    mean_price = sum(prices) / len(prices) if prices else (profile.mean_price or 0)
    low, high = (mean_price * 100 )/60, (mean_price * 100)/140

    recommendations = Product.objects.filter(
        category__in=category_ids,
        price__gte=low,
        price__lte=high
    ).exclude(id__in=[p.id for p in recent_products]).distinct()[:limit]

    return recommendations