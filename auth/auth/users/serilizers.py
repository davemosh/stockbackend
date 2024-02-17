from rest_framework import serializers
from .model import User
class UserSerilizers(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'name', 'password' ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    