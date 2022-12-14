from django.db import models
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,primary_key=True)
	phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
	
	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)


