from rest_framework import serializers
from .models import Profile


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'email', 'last_login', 'is_superuser', 'first_name', 'last_name', 'date_joined',
        'number',)
