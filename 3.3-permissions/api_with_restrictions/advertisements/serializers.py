# from django.contrib.auth.models import User
# from rest_framework import serializers
# from advertisements.models import Advertisement
# from rest_framework.exceptions import ValidationError


# class UserSerializer(serializers.ModelSerializer):
#     """Serializer для пользователя."""

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name',
#                   'last_name',)


# class AdvertisementSerializer(serializers.ModelSerializer):
#     """Serializer для объявления."""

#     creator = UserSerializer(
#         read_only=True,
#     )

#     class Meta:
#         model = Advertisement
#         fields = ('id', 'title', 'description', 'creator',
#                   'status', 'created_at',)
#         read_only_fields = ['creator']

#     def create(self, validated_data):
#         if len(Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN')) > 9:
#             raise ValidationError('Разрешено не более 10 объявлений')

#         validated_data["creator"] = self.context["request"].user
#         return super().create(validated_data)

#     def update(self, data, validated_data):
#         if len(Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN')) > 9:
#             raise ValidationError('Разрешено не более 10 объявлений')

#         validated_data["creator"] = self.context["request"].user
#         return super().update(validated_data)

#     def validate(self, data):
#         return data

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        if len(Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN')) > 9:
            raise ValidationError('Разрешено не более 10 объявлений')
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)
        

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        return data