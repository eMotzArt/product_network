from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from dotmap import DotMap
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import Contact, Country, City


USER_MODEL = get_user_model()


class ContactSerializer(serializers.ModelSerializer):
    country = serializers.CharField(required=True)
    city = serializers.CharField(required=True)

    class Meta:
        model = Contact
        exclude = ('id', )


class AgentCreateSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = USER_MODEL
        fields = ('name', 'password', 'email', 'contact', 'supplier', 'role')
        read_only_fields = ('is_active', 'is_staff', 'debts', 'id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, password):
        validate_password(password=password, user=USER_MODEL)
        return password

    def validate(self, attrs):
        #exclude supplier if user is factory, request if not
        supplier = attrs.get('supplier', None)
        if attrs['role'] == USER_MODEL.Role.factory:
            attrs['supplier'] = None
        elif supplier == None:
            raise ValidationError({'supplier': 'Supplier must be set'})
        return attrs

    def create(self, validated_data):
        #contact get or creation
        contact_data = DotMap(validated_data['contact'])
        country, _ = Country.objects.get_or_create(country_name=contact_data.country)
        city, _ = City.objects.get_or_create(city_name=contact_data.city)
        contact, created = Contact.objects.get_or_create(country=country, city=city, street=contact_data.street, house=contact_data.house)
        validated_data['contact'] = contact

        #instance creation, password cypher
        instance = USER_MODEL.objects.create(**validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            raise serializers.ValidationError('Username or password is incorrect')
        return attrs


class EnterprisesListSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    class Meta:
        model = USER_MODEL
        fields = ['name', 'email', 'debts', 'supplier', 'role', 'contact']
