from rest_framework import serializers

from trialbalance.models import TrialBalance


class TrialBalanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = TrialBalance
        fields = ('particular', 'debitAmount', 'creditAmount', 'ledger','company')
