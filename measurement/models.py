from django.db import models


class Sensor(models.Model):
    name = models.CharField()
    description = models.CharField(blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, related_name="measurements", on_delete=models.CASCADE
    )
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
