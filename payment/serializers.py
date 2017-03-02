from rest_framework import serializers
from payment.models import Payment


class Paymentserializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('company', 'firstAccount', 'secondAccount', 'amount', 'addedBy', 'date', 'narration')
