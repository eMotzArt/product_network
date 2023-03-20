from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from goods.models import Supplier
from goods.permissions import IsActive
from goods.serializers import SupplierSerializer, SupplierFactoryCreateSerializer, \
    SupplierAgentCreateSerializer


class SuppliersListView(ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

class SupplierRetrieveDestroyView(RetrieveDestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class SupplierCreateView(CreateAPIView):
    serializer_classes = {
        'factory': SupplierFactoryCreateSerializer,
        'agent': SupplierAgentCreateSerializer
    }
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


    def get_serializer_class(self, *args, **kwargs):
        if self.request.data['role'] == Supplier.Role.factory:
            return self.serializer_classes['factory']
        return self.serializer_classes['agent']
