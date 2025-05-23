
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from apirest.models import Sensores
from apirest.serializers import SensoresSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([AllowAny, IsAuthenticated])
def sensor_data_list(request):
    if request.method == 'GET':
        sensor_data = Sensores.objects.all()
        sensor_data_serializer = SensoresSerializer(sensor_data, many=True)
        return JsonResponse(sensor_data_serializer.data, safe=False)
    elif request.method == 'POST':
        sensor_data_data = JSONParser().parse(request)
        sensor_data_serializer = SensoresSerializer(data=sensor_data_data)
        if sensor_data_serializer.is_valid():
            sensor_data_serializer.save()
            return JsonResponse(sensor_data_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(sensor_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny, IsAuthenticated])
def sensor_data_detail(request, pk):
    try: 
        sensor_data = Sensores.objects.get(pk=pk) 
        if request.method == 'GET': 
            sensor_data_serializer = SensoresSerializer(sensor_data) 
            return JsonResponse(sensor_data_serializer.data) 
        elif request.method == 'PUT': 
            sensor_data_data = JSONParser().parse(request) 
            sensor_data_serializer = SensoresSerializer(sensor_data, data=sensor_data_data) 
            if sensor_data_serializer.is_valid(): 
                sensor_data_serializer.save() 
                return JsonResponse(sensor_data_serializer.data) 
            return JsonResponse(sensor_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            sensor_data.delete() 
            return JsonResponse({'message': 'sensor data was deleted successfully!'}, status=status.HTTP_200_OK)
    except Sensores.DoesNotExist: 
        return JsonResponse({'message': 'The sensor data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
