from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from goods.models import Product
from goods.permissions import IsFactory, IsAgent, IsActive
from goods.serializers import ProductListCreateSerializer, ProductOrderSerializer


class GoodsCreateView(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsFactory, IsActive]
    serializer_class = ProductListCreateSerializer

class GoodsOrderView(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsAgent, IsActive]
    serializer_class = ProductOrderSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StorageView(ListAPIView):
    serializer_class = ProductListCreateSerializer
    permission_classes = [IsAuthenticated, IsActive]
    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

class SupplierStorageView(ListAPIView):
    serializer_class = ProductListCreateSerializer
    permission_classes = [IsAuthenticated, IsActive, IsAgent]

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user.supplier)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

