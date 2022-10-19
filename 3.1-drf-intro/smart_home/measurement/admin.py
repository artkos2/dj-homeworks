from django.contrib import admin
from .models import Sensor,Measurement
# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
    list_display = ['sensor','temperature', 'date']