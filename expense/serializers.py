from rest_framework import serializers
from expense.models import Expense


class Expenseserializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id','company', 'firstAccount', 'secondAccount', 'amount', 'addedBy', 'date', 'narration')
