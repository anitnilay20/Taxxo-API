from rest_framework import serializers
from .models import Purchase


class Purchaseserializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = (
            'id', 'date', 'party_name', 'journals', 'payment_method', 'total_amount', 'narration', 'company',
            'added_by')