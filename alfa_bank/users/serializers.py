from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField
from rest_framework.serializers import ModelSerializer

from users.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username',
                  'password']


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(
#         style={'placeholder': 'Имя пользователя', 'autofocus': True}
#     )
#     password = serializers.CharField(
#         max_length=100,
#         style={'input_type': 'password', 'placeholder': 'Пароль'}
#
#     )
#
#     def validate(self, data):
#         username = data.get('username', None)
#         password = data.get('password', None)
#         if username == 'test007':
#             raise serializers.ValidationError('Нельзя такое имя')
#         if username is None:
#             raise serializers.ValidationError('Заполните имя пользователя')
#         if password is None:
#             raise serializers.ValidationError('Заполните пароль')
#         return data
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']



    def validate(self, data):
        errors = []
        print("МЕТОД VALIDATE СРАБОТАЛ")
        username = data.get('username', None)
        password = data.get('password', None)

        if username == "test007":
            print("Попало в проверку")
            errors.append('Проблемы с логином')

        if password is None:
            errors.append('Проблемы с паролем')
            # raise serializers.ValidationError({'name': 'Please enter a valid name.'})

        if errors:
            print(errors)
            raise ValidationError(errors)
        return data

    def create(self, validated_data):
        print("МЕТОД CREATE СРАБОТАЛ")
        return User.objects.create_user(**validated_data)
