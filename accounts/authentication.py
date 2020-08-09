from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.hashers import check_password



class EmailAuthBackend(object):
	""" Authenticate using e-mail account. """
	def authenticate(self,request, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			#print(user)
			if user.check_password(password):
				return user
			return None
		except User.DoesNotExist:
			return None
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None


class PhoneNumberAuthBackend(object):
	""" Authenticate using user phone number or mobile number"""
	
	def authenticate(self, request,username=None, password=None):
		try:

			profile_user = User.objects.select_related().get(profile__phone=username)
			#print(profile_user)
			if profile_user.check_password(password):
				return profile_user
			return None
		except Profile.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None