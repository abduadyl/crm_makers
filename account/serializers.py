from django.contrib.auth import get_user_model
from rest_framework import serializers


MyUser = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    password_confirm = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'password_confirm', )

    def validate_username(self, username):
        if MyUser.objects.filter(username=username).exists():
            raise serializers.ValidationError('Пользователь с данным именем уже существует')
        return username

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm', None)
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user