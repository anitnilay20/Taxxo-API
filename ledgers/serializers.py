from rest_framework import serializers
from ledgers.models import Ledgers


class Ledgersserializers(serializers.ModelSerializer):
    class Meta:
        model = Ledgers
        fields = ('id','company','name','groups','opening_balance','type','inventory','date','credit_account','debit_account')
