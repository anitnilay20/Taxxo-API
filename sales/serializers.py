from rest_framework import serializers
from sales.models import Sales


class Salesserializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = (
            'id','date','party_name','journals','payment_method','total_amount','narration','company','added_by')
