from django.contrib.gis.db import models


class Polygon(models.Model):
	name = models.CharField(max_length=100, verbose_name="Название полигона")
	polygon = models.PolygonField(verbose_name="Геометрия полигона")
	crosses_antimeridian = models.BooleanField(default=False, verbose_name="Пересекает антимеридиан")
    
	def __str__(self):
		return self.name
	