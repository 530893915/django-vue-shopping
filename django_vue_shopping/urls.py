"""django_vue_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django_vue_shopping.settings import MEDIA_ROOT
from django.views.static import serve
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.documentation import include_docs_urls
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from goods.views import GoodsListViewset
# import xadmin

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewset, base_name="goods")

urlpatterns = [
    # path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='dudu'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
