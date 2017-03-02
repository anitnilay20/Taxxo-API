from rest_framework import serializers
from receipt.models import Receipt


class Receiptserializers(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('company', 'firstAccount', 'secondAccount', 'amount', 'addedBy', 'date', 'narration')
