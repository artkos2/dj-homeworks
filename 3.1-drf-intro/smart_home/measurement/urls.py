from django.urls import path
from .views import SensorsView, SensorDetailView, MeasurementAdd
 

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementAdd.as_view())
    ]
