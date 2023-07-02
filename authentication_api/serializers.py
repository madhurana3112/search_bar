from rest_framework import serializers
from  authentication_app.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number']

    def create(self, validated_data):
        user = CustomUser(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )

        user.save()
        return user
