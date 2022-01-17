from django.db import models

# Create your models here.
class iot_data(models.Model):
    area = models.CharField(max_length=100)
    device_name = models.TextField(blank=True)
    value = models.FloatField(blank=True)
    value2 = models.FloatField(blank=True)
    upload_time = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.area
