from rest_framework import serializers

from .models import Sensor, Measurement


# class WeaponSerializer(serializers.Serializer):
#     power = serializers.IntegerField()
#     rarity = serializers.CharField()


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']