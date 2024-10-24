from django import forms
from .models import Polygon as PolygonModel
from django.contrib.gis.geos import Polygon, LinearRing

class PolygonForm(forms.ModelForm):
	coordinates = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label="Введите координаты через запятую (каждая пара широта долгота через пробел)")
	
	class Meta:
		model = PolygonModel
		fields = ['name']
		
	def clean_coordinates(self):
		coordinates = self.cleaned_data['coordinates']
		crosses_antimeridian = False
		try:
			points = coordinates.split(",")
			parsed_points = []
			
			for point in points:
				lat, lon = map(float, point.strip().split())
				
				if lon > 180:
					lon -= 360
					crosses_antimeridian = True
				elif lon < -180:
					lon += 360
					crosses_antimeridian = True
				
				if not (-90 <= lat <= 90):
					raise forms.ValidationError('Широта должна быть в диапазоне от -90 до 90.')
				parsed_points.append((lat, lon))
				
			if len(parsed_points)<4:
				raise forms.ValidationError('Для создания полигона необходимо минимум 4 точки.')
			
			if parsed_points[0] != parsed_points[-1]:
				parsed_points.append(parsed_points[0])
			
			return parsed_points, crosses_antimeridian
		except ValueError:
			raise forms.ValidationError('Некорректный формат координат. Введите координаты в виде: "широта долгота, широта долгота, ..."')
	
	def save(self, commit=True):
		instance = super().save(commit=False)
		parsed_points, crosses_antimeridian = self.cleaned_data['coordinates']
		
		ring = LinearRing(parsed_points)
		polygon = Polygon(ring)
		instance.polygon = polygon
		instance.crosses_antimeridian = crosses_antimeridian
		
		if commit:
			instance.save()
		return instance