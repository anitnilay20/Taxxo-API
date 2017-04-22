from rest_framework import serializers
from .models import Purchase


class Purchaseserializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = (
            'id','Invoice','party_name','reference','journals','payment_method','added_by')
