from django.db.models.signals import pre_save
from django.dispatch import receiver
from results.models import PresidentialPollResult

@receiver(pre_save, sender=results.PresidentialPollResult)
def valid_votes_sum(sender, instance, **kwargs):
	# instance.valid_votes = instance.
	# instance.save()
	pass
