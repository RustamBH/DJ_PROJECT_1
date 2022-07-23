# from django.contrib import admin
from django.urls import path
from .views import SensorAPIRetrieveUpdate, SensorAPIList, MeasurementAPICreate

import measurement.views

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorAPIList.as_view()),
    path('sensors/<int:pk>/', SensorAPIRetrieveUpdate.as_view()),
    path('measurements/', MeasurementAPICreate.as_view()),
]
