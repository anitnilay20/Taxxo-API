from rest_framework import serializers
from contra.models import Contra


class Contraserializers(serializers.ModelSerializer):
    class Meta:
        model = Contra
        fields = ('company','firstAccount','secondAccount','amount','addedBy','date','narration')
