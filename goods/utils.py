from django.db.models import Q
from goods.models import Products

def q_search(query):
    if query.isdigit() and len(query) <=5:   #queryisdigit- если query состоит из цифр и длина <=5(т.к id = 0000 и id товара)
        return Products.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 2 ]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token) #поиск по описанию
        q_objects |= Q(name__icontains=token) #поиск по названию

    return Products.objects.filter(q_objects)
