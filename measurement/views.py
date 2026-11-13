from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from measurement.models import Sensor
from measurement.serializers import SensorSerializer, SensorDetailSerializer


class SensorsListView(ListAPIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
