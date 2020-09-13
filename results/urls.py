from . import views
from django.urls import path, reverse, include


app_name='results'

urlpatterns=[
	
	path('barchart/',views.BarChartView, name='barchart'),
	path('constituency/',views.Constituent, name='constituency'),
	path('stations/',views.Station, name='stations'),
	path('presidential/',views.PresidentialResult, name='presidential'),
	path('heatmap/',views.HeatMap, name='heatmap'),
	path('tilemap/',views.TileMap, name='tilemap'),
	path('pie/',views.Pie, name='pie'),
	path('presidentialview/',views.PresidentialChartView.as_view(), name='presidentialview'),
	path('barchartview/', views.BarView.as_view(), name='barview'),
	path('heatmapview/',views.PresidentialHeatView.as_view(), name='heatmapview'),
	path('tilemapview/',views.TilemapView.as_view(),name='tilemapview'),
	path('piechartview/',views.Piechartview.as_view(),name='piechartview'),
	path('columnchartview/',views.ColumnChartView.as_view(), name='columnchartview'),
]