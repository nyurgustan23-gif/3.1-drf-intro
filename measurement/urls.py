from django.urls import path

from measurement.views import SensorDetailView, SensorsListView

urlpatterns = [
    path("sensors/", SensorsListView.as_view()),
    path("sensors/<pk>/", SensorDetailView.as_view()),
]
