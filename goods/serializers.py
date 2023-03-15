from django.db import transaction
from dotmap import DotMap
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from goods.models import Product


class ProductListCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = '__all__'

class ProductOrderSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    count = serializers.IntegerField(required=True)

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, attrs):
        data = DotMap(attrs)
        if not Product.objects.filter(name=data.name, model=data.model, owner=data.owner.supplier).exists():
            raise ValidationError("Searched product not found in supplier store")
        requested_product = Product.objects.get(name=data.name, model=data.model, owner=data.owner.supplier)
        if requested_product.count < data.count:
            raise ValidationError(f"Not enough goods in supplier store. Available only: {requested_product.count}")
        return attrs

    def create(self, validated_data):
        data = DotMap(validated_data)
        requested_product = Product.objects.get(name=data.name, model=data.model, owner=data.owner.supplier)
        requested_product.count -= data.count
        data.owner.debts += requested_product.price * data.count
        with transaction.atomic():
            requested_product.save()
            data.owner.save()
            instance = Product.objects.create(name=data.name, model=data.model, count=data.count, owner=data.owner)
            instance.price = requested_product.price
            instance.save()
        return instance


    class Meta:
        model = Product
        fields = '__all__'
