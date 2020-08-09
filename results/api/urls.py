from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from results.api import views


route=DefaultRouter()
via=DefaultRouter()
route.register('rs', views.PresidentialPollResultViewSet)
route.register('ps', views.PollingStationViewSet)
# via.register('', views.VoteViewSet)

urlpatterns=[
	path('', include(route.urls)),
	# path('via/', include(via.urls)),
]








# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register('', views.PollResultViewset)
# router.register('poll', views.PollingStationViewset)

# app_name='results'
# urlpatterns=[
# 	# path('',include(router.urls)),
# 	path('polls/', views.PollResultListView.as_view(), name='pollresultlist'),
# 	path('polls/<int:pk>/', views.PollResultDetailView.as_view(), name='pollresultdetails'),
	
# 	]

# #format_suffix_patterns(urlpatterns)