from django.db import models


class AreasTecnologicas(models.Model):
    id_area_tecnologica = models.IntegerField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.area_tecnologica