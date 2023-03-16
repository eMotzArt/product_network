from django.urls import path
from goods import views

urlpatterns = [
    path('make', views.GoodsCreateView.as_view(), name='create good'),
    path('order', views.GoodsOrderView.as_view(), name='request good'),
    path('storage', views.StorageView.as_view(), name='my storage list'),
    path('supplier', views.SupplierStorageView.as_view(), name='supplier storage list')
]
