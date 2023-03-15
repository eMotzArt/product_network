from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from goods.models import Product
from goods.permissions import IsFactory, IsAgent
from goods.serializers import ProductListCreateSerializer, ProductOrderSerializer


class GoodsCreateView(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsFactory]
    serializer_class = ProductListCreateSerializer

class GoodsOrderView(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAgent]
    serializer_class = ProductOrderSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StorageView(ListAPIView):
    serializer_class = ProductListCreateSerializer

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SupplierStorageView(ListAPIView):
    serializer_class = ProductListCreateSerializer

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user.supplier)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

