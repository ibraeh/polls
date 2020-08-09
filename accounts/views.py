from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required


# Profile view for log on users to display user settings
def profile(request):
	return  render(request,'accounts/profile.html')


# Sign up view to handle new users	
def signup(request):
	if request.method =='POST':
		form =UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('profile')

	else:
		form =UserCreationForm()
	return render(request, 'accounts/signup.html', {'form':form})


# Dashboard to display all activities
@login_required
def dashboard(request):
	return render(request,'accounts/dashboard.html', {'section': 'dashboard'})




# Edit view for registered users to make changes to user settings
@login_required
def edit(request):
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
