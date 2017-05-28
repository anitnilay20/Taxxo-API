from rest_framework import serializers
from ledgerhistory.models import LedgerHistory


class Ledgerhistoryserializers(serializers.ModelSerializer):
    class Meta:
        model = LedgerHistory
        fields = ('id', 'name', 'type', 'to_account', 'date', 'closing_balance', 'total_amount')
