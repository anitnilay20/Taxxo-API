from rest_framework import serializers
from income.models import Income


class Incomeserializers(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id','company', 'firstAccount', 'secondAccount', 'amount', 'addedBy', 'date', 'narration')
