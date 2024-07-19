from django.shortcuts import get_list_or_404,get_object_or_404, render

from goods.utils import q_search
from .models import Products
from django.core.paginator import Paginator



def catalog(request,category_slug=None):
    page = request.GET.get('page', 1) #проверка с помощью метод get,если есть ключ "page",то выводится,если нет,то по умолчанию 1
    on_sale = request.GET.get("on_sale",None) #если не выбирает пользователь товар по акции,то передается None
    order_by = request.GET.get("order_by",None) #если не выбирает пользователь сортировку,то передается None
    query = request.GET.get("q",None)

    if category_slug == 'vse-tovary':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug)) #сортировка по классу Category,атрибуту класса slug

    if on_sale:
        goods = goods.filter(discount__gt=0)#фильтруем queryset,если скидка больше чем 0

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3) #колво товаров на стр
    current_page = paginator.page(int(page)) #какую страницу открывать при открытии каталога

    context = {
        "title": "ArtWood- Каталог",
        "goods": current_page,
        "slug_url":category_slug,
    }
    return render(request, "goods/catalog.html", context)




def product(request,product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product':product
    }

    return render(request, "goods/product.html",context)

