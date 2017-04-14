from rest_framework import serializers
from .models import Journal


class Journalserializers(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('credit_amount','debit_amount','narration','for_account','to_Account'
            )
