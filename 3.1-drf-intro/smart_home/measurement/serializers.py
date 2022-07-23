from rest_framework import serializers
from .models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы
class MeasurementSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=255, allow_empty_file=True, use_url=True)

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
