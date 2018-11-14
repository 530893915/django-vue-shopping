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
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewset, UserViewset
import xadmin

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")

# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

router.register(r'users', UserViewset, base_name="users")

goods_list = GoodsListViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的认证接口
    path('login/', obtain_jwt_token),

    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='dudu'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
