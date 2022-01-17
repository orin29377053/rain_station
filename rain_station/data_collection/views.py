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
import psycopg2
import psycopg2.extras
import requests
import json
# Create your views here.
pgdb_config={
    'host':'35.221.171.148',
    'port':5432,
    'user':'admin',
    'password':'admin',
    'database':'postgres',
}



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
# @api_view(['Post'])
# def data_creat(request):
#     serializer=iot_data_Serializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response('nice!')

@api_view(['Post'])
def data_creat(request):
    data=(request.headers['data'])#.split(',')
    data=json.loads(data)
    device=data['device']
    count=data['count']
    x=data['x']
    y=data['y']
    creat_date=data['creat_date']
    sqls=(
        """  
            INSERT INTO raindata 
            (device, count, x, y, creat_date)
            VALUES 
            ('{device}', '{count}', '{x}', '{y}', '{creat_date}')
        """.format(
        device=device,
        count=count ,
        x=x,
        y=y,
        creat_date=creat_date,
        )
    )
    print(sqls)
    conn = psycopg2.connect(**pgdb_config)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(sqls)
    conn.commit()
    conn.close()
    return Response('nice!')
