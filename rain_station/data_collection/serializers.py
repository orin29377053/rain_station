from dataclasses import fields
from rest_framework import serializers
from .models import iot_data


class iot_data_Serializers(serializers.ModelSerializer):
    class Meta:
        model = iot_data
        fields='__all__'
        