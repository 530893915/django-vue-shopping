#coding:utf8

from django_filters import rest_framework as filters
from .models import Goods

class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    price_min = filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='shop_price', lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']