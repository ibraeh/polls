from django.urls import path
from .import views
urlpatterns=[
	path('', views.Home, name='home'),
	path('profile/', views.Profile, name='profile'),
	path('signup/', views.Signup, name='signup'),
	path('dashboard/', views.Dashboard, name='dashboard'),
	path('edit/', views.Edit, name='edit'),
	path('presidential/', views.Presidential, name='presidential'),
	path('region/',views.Region, name='region'),
	path('stations/',views.PollingStation, name='pollingstation'),
]