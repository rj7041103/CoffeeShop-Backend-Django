from rest_framework import serializers
from .models import Products, Reviews, Users, Subscriptions, Returns, Payments, Inventory


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields = ['created_at',]

class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'
        read_only_fields = ['created_at',]

class SubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = '__all__'

class ReturnsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Returns
        fields = '__all__'
        read_only_fields = ['created_at',]

class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
        read_only_fields = ['created_at',]

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['created_at',]

class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = ['created_at',]