# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import CreateAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


# Used for read-write endpoints to represent a collection of model instances.
# Provides get and post method handlers
class SensorAPIList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# a single model instance
# Provides get and post method handlers
class SensorAPIRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Used for create-only endpoints.
# Provides a post method handler.
class MeasurementAPICreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
