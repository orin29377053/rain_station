from re import I
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from .models import iot_data
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import iot_data_Serializers
from .models import iot_data
# Create your views here.

def hello_world(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })
@api_view(['GET'])
def  apioverview(request):
    api_urls={
        'list':'/data_list/',
        'creat':'/data_creat/',
        'delete':'/data_delet/'
    }
    return JsonResponse(api_urls)
@api_view(['GET'])
def data_list(request):
    rain=iot_data.objects.all()
    serializer=iot_data_Serializers(rain,many=True)
    return Response(serializer.data)
@api_view(['Post'])
def data_creat(request):
    serializer=iot_data_Serializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
