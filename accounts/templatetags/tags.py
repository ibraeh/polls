from django import template
register = template.Library()
from results.models import *

@register.simple_tag
def total_posts():
	return PresidentialPollResult.objects.filter(voting_status=False).count()


@register.filter
def maximum(value):
	return max(value)

