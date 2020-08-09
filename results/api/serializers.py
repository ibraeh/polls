from rest_framework import serializers
from results.models import PollingStation,PresidentialPollResult


class PresidentialPollResultSerializer(serializers.ModelSerializer):

	class Meta:
		model=PresidentialPollResult
		fields='__all__'
		# fields=['pscode','NDC', 'NPP', 'CPP', 'rejected', 'pink_sheet', 'available', 'verified']



class PollingStationSerializer(serializers.ModelSerializer):

	class Meta:
		model=PollingStation
		fields='__all__'



# class VoteSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Vote
# 		fields='__all__'



















# class PollResultSerializer(serializers.ModelSerializer):
	
# 	class Meta:
# 		model=PollResult
# 		fields='__all__'
# 		# fields=['ps_code', 'NDC', 'NPP', 'CPP' ]


# class PollingStationSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model=PollingStation
# 		##fields=['id', 'name', 'pscode']
# 		fields='__all__'


# # Hyperlinked model serializers

# class PollResultHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):

# 	class Meta:
# 		model=PollResult
# 		fields=['url','ps_code', 'NDC', 'NPP', 'CPP']

# class PollingStationHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model=PollingStation
# 		fields=['url','name', 'pscode', 'vote_pop']