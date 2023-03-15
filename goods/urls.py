"""product_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from goods import views

urlpatterns = [
    path('make', views.GoodsCreateView.as_view(), name='create good'),
    path('order', views.GoodsOrderView.as_view(), name='request good'),
    path('storage', views.StorageView.as_view(), name='my storage list'),
    path('supplier', views.SupplierStorageView.as_view(), name='supplier storage list')
]