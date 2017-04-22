from rest_framework import serializers
from sales.models import Sales


class Salesserializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = (
            'id','Invoice','party_name','reference','journals','payment_method','added_by')
