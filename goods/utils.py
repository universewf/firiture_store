from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from goods.models import Products


# SearchRank- Упорядочение по релевантности
# SearchVector -поиск по обоим полям
# rank - рассчитывается совпадание описание товара с введенным запросом


def q_search(query):
    if (
        query.isdigit() and len(query) <= 5
    ):  # queryisdigit- если query состоит из цифр и длина <=5(т.к id = 0000 и id товара)
        return Products.objects.filter(id=int(query))
    vector = SearchVector(
        "name", "description"
    )  # поиск по обоим полям,названию и описанию
    query = SearchQuery(query)
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    # -rank от наиболее подходящего к менее
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    return result
