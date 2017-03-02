from rest_framework import serializers
from balance.models import Balance


class Balanceserializers(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('company', 'type', 'amount')
