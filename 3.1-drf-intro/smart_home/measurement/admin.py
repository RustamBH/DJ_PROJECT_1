from django.contrib import admin
from .models import Sensor, Measurement


# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    model = Sensor
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    model = Measurement
    list_display = ['id', 'temperature', 'created_at', 'image']
