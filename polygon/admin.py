from django.contrib import admin
# Register your models here.
from .models import Polygon

@admin.register(Polygon)
class PolygonAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_first_coordinate')
	search_fields = ('name',)
	
	def get_first_coordinate(self, obj):
		if obj.polygon:
			first_point = obj.polygon.coords[0][0]
			return f"{first_point[1]}, {first_point[0]}"
		return "Нет данных"
	
	get_first_coordinate.short_description = "Первая координата"