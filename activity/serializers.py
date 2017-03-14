from rest_framework import serializers
from activity.models import Activity


class Activityserializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('name','date','added_by','amount','company')
