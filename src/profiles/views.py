from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
	template = 'home.html'
	context = locals()
	return render(request,template,context)


def about(request):
        context = locals()
        template = 'about.html'
        return render(request, template, context)

@login_required
def user_profile(request):
	if request.user.is_authenticated():
		user=request.user
	else:
		user = None
	context = {'user':user }
	template = 'profile.html'
	return render(request,template,context)
