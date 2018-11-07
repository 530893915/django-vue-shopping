#coding:utf8
import json

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        """
        商品列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)