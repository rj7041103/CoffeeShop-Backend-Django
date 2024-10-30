from .models import Products,Users,Subscriptions,Reviews,Returns,Payments, Inventory
from rest_framework import serializers
from rest_framework import viewsets, permissions
from .serializer import ProductsSerializer,UsersSerializer,SubscriptionsSerializer,ReviewsSerializer,ReturnsSerializer,PaymentsSerializer, InventorySerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsersSerializer

class SubscriptionsViewSet(viewsets.ModelViewSet):
    queryset = Subscriptions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubscriptionsSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReviewsSerializer

class ReturnsViewSet(viewsets.ModelViewSet):
    queryset = Returns.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReturnsSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PaymentsSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InventorySerializer