from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from company.models import Company, Product
from company.serializers import (CompanySerializer, ProductSerializer,
                                 ContactSerializer, CompanyCreateSerializer)


class CompanyViewSet(viewsets.ModelViewSet):
    """Создание, просмотр, редактирование и удаление компании"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']

    def create(self, request, *args, **kwargs):
        serializer = CompanyCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_company = serializer.save()
        return Response(CompanyCreateSerializer(new_company).data,
                        status=status.HTTP_201_CREATED)


class ProductViewSet(viewsets.ModelViewSet):
    """Создание, просмотр, редактирование и удаление продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ContactViewSet(viewsets.ModelViewSet):
    """Создание, просмотр, редактирование и удаление контакта"""
    serializer_class = ContactSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
