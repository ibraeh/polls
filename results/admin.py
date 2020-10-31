from django.contrib import admin

from results.models import Region, District,Constituency, ElectoralArea, PollingStation,  Agent, PresidentialPollResult, Vote

admin.site.register([Vote,  Agent, District])

# Polling station 
class PollinStationAdmin(admin.ModelAdmin):
	list_display = ['name', 'pscode','voter_pop','electoral_area','constituency']
	list_filter = ['created_on', 'name', 'electoral_area', 'constituency']
	#list_editable=['voter_pop','pscode']
	#date_hierarchy ='updated_on'
	#ordering = ['updated_on']
	search_fields = ['name', 'pscode']
	#autocomplete_fields = ['name']
admin.site.register(PollingStation, PollinStationAdmin)




#Poll results
@admin.register(PresidentialPollResult)
class PollResultAdmin(admin.ModelAdmin):
	list_display = ['pscode','NPP','NDC','GUM', 'CPP','GFP','GCPP','APC','LPG','PNC','PPP','NDP','IND', 'rejected', 'valid_votes', 'vote_cast','available']
	list_filter = ['created_on','pscode']
	#list_editable=['voter_pop','pscode']
	#autocomplete_fields = ['pscode']
	search_fields = ['pscode']


# Constituency
@admin.register(Constituency)
class ConstituencyAdmin(admin.ModelAdmin):
	list_display = ['name','district']
	list_filter = ['created_on']
	#list_editable=['voter_pop','pscode']
	# list_display_links = ('name')




# Electoral Area
@admin.register(ElectoralArea)
class ElectoralAreaAdmin(admin.ModelAdmin):
	list_display = ['name','constituency']
	list_filter = ['created_on']
	#list_editable=['voter_pop','pscode']




# Region
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
	list_display = ['name']
	list_filter = ['created_on']
	#list_editable=['voter_pop','pscode']
