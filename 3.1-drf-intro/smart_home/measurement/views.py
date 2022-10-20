# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):

        Sensor.objects.create(name = request.data['name'], description = request.data['description'])
        return Response({'Response': 'OK'})


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        Sensor.objects.filter(id = pk).update(description = request.data['description'])
        return Response({'Response': 'OK'})

class MeasurementAdd(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request): 
        Measurement.objects.create(sensor_id = request.data['sensor'], temperature = request.data['temperature'])
        return Response({'Response': 'OK'})