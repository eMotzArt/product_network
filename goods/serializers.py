from django.db import transaction
from dotmap import DotMap
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from goods.models import Product, Contact, Supplier


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SubSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class SupplierSerializer(serializers.ModelSerializer):
    provider = SubSupplierSerializer()
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Supplier
        fields = '__all__'
        depth = 1

class SupplierFactoryCreateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    products = ProductSerializer(many=True)


    def create(self, validated_data):
        products_data = validated_data.pop('products')
        contact_data = DotMap(validated_data.pop('contact'))
        with transaction.atomic():
            contact = Contact.objects.create(country=contact_data.country, city=contact_data.city,
                                             street=contact_data.street, house=contact_data.house,
                                             email=contact_data.email)

            products_instances = []
            for product in products_data:
                product_instance = Product.objects.create(**product)
                products_instances.append(product_instance)

            supplier = Supplier.objects.create(contact=contact, **validated_data)

            for product in products_instances:
                supplier.products.add(product)

        return supplier

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierAgentCreateSerializer(serializers.ModelSerializer):
    provider = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    contact = ContactSerializer()
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)


    def validate(self, attrs):
        products = attrs['products']
        provider = attrs['provider']
        provider_products = provider.products.all()
        non_provider_products = []

        for product in products:
            if product not in provider_products:
                non_provider_products.append(product.pk)

        if non_provider_products:
            raise ValidationError({'products': f'Данные продукты не относится к вашему поставщику. {non_provider_products}'})

        return attrs

    def create(self, validated_data):
        products = validated_data.pop('products')

        contact_data = DotMap(validated_data.pop('contact'))
        with transaction.atomic():
            contact = Contact.objects.create(country=contact_data.country, city=contact_data.city,
                                             street=contact_data.street, house=contact_data.house,
                                             email=contact_data.email)
            supplier = Supplier.objects.create(contact=contact, **validated_data)
            for product in products:
                supplier.products.add(product)

        return supplier


    class Meta:
        model = Supplier
        fields = '__all__'
