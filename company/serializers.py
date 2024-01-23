from rest_framework import serializers

from company.models import Company, Product, Contacts


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    contacts = ContactSerializer()
    products = ProductSerializer(many=True, read_only=True)
    hierarchy_level = serializers.SerializerMethodField(read_only=True)

    def get_hierarchy_level(self, instance):
        if instance.provider:
            if instance.subjects_electronic_network == '0':
                return 0
            return int(instance.provider.subjects_electronic_network) + 1
        else:
            return 0

    class Meta:
        model = Company
        fields = '__all__'
        extra_kwargs = {
            'debt': {'read_only': True}
        }


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
