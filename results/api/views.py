from results.api.serializers import *
from rest_framework import generics
from results.models import PollingStation, PresidentialPollResult
from rest_framework import viewsets



class PresidentialPollResultViewSet(viewsets.ModelViewSet):
	queryset=PresidentialPollResult.objects.all()
	serializer_class=PresidentialPollResultSerializer



class PollingStationViewSet(viewsets.ModelViewSet):
	queryset=PollingStation.objects.all()
	serializer_class=PollingStationSerializer



# class VoteViewSet(viewsets.ModelViewSet):
# 	queryset=Vote.objects.all()
# 	serializer_class=VoteSerializer





# class PollResultListView(generics.ListCreateAPIView):
# 	queryset=PollResult.objects.all()
# 	serializer_class=PollResultSerializer


# class PollResultDetailView(generics.RetrieveUpdateDestroyAPIView):
# 	queryset=PollResult.objects.all()
# 	serializer_class=PollResultSerializer


# # Viewset class

# class PollResultViewset(viewsets.ModelViewSet):
# 	queryset=PollResult.objects.all()
# 	serializer_class=PollResultHyperlinkedSerializer


# class PollingStationViewset(viewsets.ModelViewSet):
# 	queryset=PollingStation.objects.all()
# 	serializer_class=PollingStationHyperlinkedSerializer