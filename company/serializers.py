from rest_framework import serializers
from .models import Company


class Companyserializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id', 'alias_name', 'name', 'address', 'country', 'city', 'pin_code', 'telephone_number', 'email',
            'currency_symbols',
            'accounts_with_inventory', 'financial_year_from', 'books_beginning_from',
            'show_amounts_in_millions', 'admin','password')
