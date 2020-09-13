from django.db import models
from django.utils.text import slugify
from django.db.models import Sum

# Class for the 16 regions in Ghana
class Region(models.Model):
	name=models.CharField(max_length=20, null=False, unique=True, db_index=True)
	created_on = models.DateTimeField(auto_now_add=True, db_index=True)
	updated_on = models.DateTimeField(auto_now=True)


	class Meta:
		ordering=['name']

	def __str__(self):
		return self.name


# Class for districts
class District(models.Model):
	name=models.CharField(max_length=40, null=False, unique=True, db_index=True)
	region=models.ForeignKey('Region',on_delete=models.SET_NULL,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True, db_index=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['region', 'name']

	def __str__(self):
		return self.name



# Class for the constituencies
class Constituency(models.Model):
	name=models.CharField(max_length=50, null=False, unique=True, db_index=True)
	district=models.ForeignKey('District',on_delete=models.SET_NULL,blank=True,null=True)
	region=models.ForeignKey('Region',on_delete=models.SET_NULL,blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True, db_index=True)
	updated_on = models.DateTimeField(auto_now=True)


	class Meta:
		verbose_name='Constituency'
		verbose_name_plural='Constituencies'
		ordering=['region','district', 'name']


	def __str__(self):
		return self.name

# Class for the electoral areas
class ElectoralArea(models.Model):
	name=models.CharField(max_length=50, null=False, db_index=True)
	constituency=models.ForeignKey('Constituency',on_delete=models.SET_NULL,blank=True,null=True, db_index=True)
	created_on = models.DateTimeField(auto_now_add=True, db_index=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['constituency', 'name']

	def __str__(self):
		return self.name

# Class for the polling stations
class PollingStation(models.Model):
	name=models.CharField(max_length=50, null=False,verbose_name='Polling Station Name', db_index=True)
	pscode=models.CharField(primary_key=True, max_length=8, null=False, blank=False,unique=True,verbose_name='Polling Station Code', db_index=True)
	voter_pop=models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Voter Population')
	address=models.CharField(max_length=255, null=True, blank=True)
	electoral_area=models.ForeignKey('ElectoralArea',on_delete=models.SET_NULL,blank=True,null=True, db_index=True)
	constituency=models.ForeignKey('Constituency',on_delete=models.SET_NULL,blank=True,null=True, db_index=True)
	district=models.ForeignKey('District',on_delete=models.SET_NULL,blank=True,null=True, db_index=True)
	region=models.ForeignKey('Region',on_delete=models.SET_NULL,blank=True,null=True, db_index=True)
	created_on = models.DateTimeField(auto_now_add=True, db_index=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['pscode']

	def __str__(self):
		return self.pscode      #f"{self.pscode}, {self.name} "

		
# Class for agents at the polling stations
class Agent(models.Model):
	name=models.CharField(max_length=255, blank=False)








# Class for the voting results
class PresidentialPollResult(models.Model):
	pscode=models.OneToOneField('PollingStation', on_delete=models.CASCADE,  verbose_name='Polling Station', primary_key=True, db_index=True)
	NDC=models.PositiveSmallIntegerField(blank=True, default=0)
	NPP=models.PositiveSmallIntegerField(blank=True, default=0)
	CPP=models.PositiveSmallIntegerField(blank=True, default=0)
	rejected=models.PositiveSmallIntegerField( blank=True, default=0)
	pink_sheet=models.FileField(upload_to='uploads/%Y/%m/%d/', help_text='Snap and upload image of the sheet')
	sheet=models.ImageField(upload_to='uploads/%Y/%m/%d/', help_text='Take picture of the sheet', blank=True)
	available = models.BooleanField(default=True)
	verified = models.BooleanField(default=False)
	valid_votes=models.PositiveSmallIntegerField(default=0)
	vote_cast=models.PositiveSmallIntegerField(default=0)
	voting_status=models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True, db_index=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['pscode']

	def save(self, *args, **kwargs):
		self.valid_votes = ((self.NDC)+(self.NPP) +(self.CPP))
		self.vote_cast = ((self.NDC)+(self.NPP) +(self.CPP) + (self.rejected))
		obj=PollingStation.objects.values('pscode','voter_pop').get(pscode=self.pscode)
		ob=obj['voter_pop']
		# print("The intented value")
		# print(ob)
		if self.vote_cast < ob:
			self.voting_status=True
		else:
			self.voting_status=False

		super(PresidentialPollResult, self).save(*args, **kwargs)

		
	def __str__(self):
		return f"{self.pscode} Polls"




class ParliamentaryPollResult(models.Model):
	pass

	class Meta:
		pass

	# def __str__(self):



class Vote(models.Model):
	name=models.CharField(max_length=20)
	slug = models.SlugField(max_length=200,blank=True)
	vote=models.CharField(max_length=10)
	photo=models.FileField(upload_to='vote', help_text='upload photos here')
	

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
			super(Vote, self).save(*args, **kwargs)

	def __str__(self):
		return self.name



