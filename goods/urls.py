from django.urls import path
from goods import views

urlpatterns = [
    path('suppliers', views.SuppliersListView.as_view(), name='Suppliers view'),
    path('suppliers/<int:pk>', views.SupplierRetrieveDestroyView.as_view(), name='Supplier view'),
    path('suppliers/create', views.SupplierCreateView.as_view(), name='Supplier create')
]
