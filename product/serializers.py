from rest_framework import serializers
from .models import Product


class Productserializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'rate', 'discount', 'batch_no', 'manufacturing_date', 'expiry_date',
                  'tax', 'location', 'manufacturing_company','date','added_by')
