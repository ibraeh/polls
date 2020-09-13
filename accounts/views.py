from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from results.models import *
from django.db.models import Sum

def Home(request):
	return render(request, 'accounts/home.html')



# Profile view for log on users to display user settings
@login_required
def Profile(request):
	return  render(request,'accounts/profile.html')


# Sign up view to handle new users

def Signup(request):
	if request.method =='POST':
		form =UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('login')

	else:
		form =UserCreationForm()
	return render(request, 'accounts/signup.html', {'form':form})


# Dashboard to display all activities
@login_required
def Dashboard(request):

	return render(request,'accounts/dashboard.html', {'section': 'dashboard'})




# Edit view for registered users to make changes to user settings
@login_required
def Edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,data=request.POST)
		profile_form = ProfileEditForm(	instance=request.user.profile,	data=request.POST,	files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request,'accounts/edit.html',	{'user_form': user_form,'profile_form': profile_form})


# Presidential 
@login_required
def Presidential(request):
	context_variable=Constituency.objects.values('region__name', 'name').annotate(ndc=Sum('pollingstation__presidentialpollresult__NDC'),npp=Sum('pollingstation__presidentialpollresult__NPP'),cpp=Sum('pollingstation__presidentialpollresult__CPP'))
	polls=PresidentialPollResult.objects.aggregate(p_ndc=Sum('NDC'),p_npp=Sum('NPP'),p_cpp=Sum('CPP'))
	return render(request,'accounts/presidential.html', {'context_variable':context_variable, 'polls':polls})


def Region(request):
	return render(request, 'accounts/region.html')

def PollingStation(request):
	context_variable=Constituency.objects.values('region__name','name','pollingstation__name', 'pollingstation__pscode','pollingstation__voter_pop','pollingstation__presidentialpollresult__NDC','pollingstation__presidentialpollresult__NPP','pollingstation__presidentialpollresult__CPP','pollingstation__presidentialpollresult__rejected','pollingstation__presidentialpollresult__valid_votes','pollingstation__presidentialpollresult__vote_cast','pollingstation__presidentialpollresult__available','pollingstation__presidentialpollresult__verified','pollingstation__presidentialpollresult__voting_status','pollingstation__presidentialpollresult__created_on')
	return render(request,'accounts/polling_station.html',{'context_variable':context_variable})