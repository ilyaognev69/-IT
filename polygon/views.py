from django.shortcuts import render, redirect
from .forms import PolygonForm
from .models import Polygon
from rest_framework import viewsets
from .serializers import PolygonSerializer


class PolygonViewSet(viewsets.ModelViewSet):
	queryset = Polygon.objects.all()
	serializer_class = PolygonSerializer

def polygon_view(request):
	if request.method == 'POST':
		form = PolygonForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('polygon_view')
		else:
			print(form.errors)
	else:
		form = PolygonForm()

	polygons = Polygon.objects.all()
	
	last_polygon = Polygon.objects.order_by('-id').first()
	if last_polygon:
		coords = [[lat, lon] for lon, lat in last_polygon.polygon.coords[0]]
	else:
		coords = []
	
	return render(request, 'polygon_form.html', {
		'form': form,
		'polygons': polygons,
		'coords':coords,
	})
