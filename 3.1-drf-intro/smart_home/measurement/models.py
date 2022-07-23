from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(verbose_name='Description')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.name)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    image = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return str(self.sensor)
