from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import auth
from .forms import *
# from one_shot.utils import handle_methods

def handle_methods(*methods):
	"""A decorator to delegate various request types to their corresponding methods."""
	def decorator(f):
		def wrapper(request, *args, **kw):
			for method in methods:
				if request.method == method.upper():
					print globals()
			  		func = globals()[method.lower() + "_" + f.__name__]
			  		return func(request)
			return f(request)
		return wrapper
	return decorator


def index(request):
	return render(request, 'user_extension/index.html', {'user': request.user, 'logged_in': request.user.is_authenticated()})

@handle_methods("POST")
def login(request):
	if request.user.is_authenticated():
		print("YOU TRIED TO LOG IN BUT YOU'RE ALREADY LOGGED IN")
		return redirect('user:home')
	else:
		return render(request, 'user_extension/login.html',
								{'form': LoginForm(label_suffix="")})
def post_login(request):
	form = LoginForm(request.POST, label_suffix="")
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = auth.authenticate(username=username, password=password)
		print "USER: " + str(user)
		if user is not None:
			print request
			auth.login(request, user)
			return redirect('user:home')
	return render(request, 'user_extension/login.html', {'form': form})

@handle_methods("POST")
def register(request):
	return render(request, 'user_extension/register.html', {'form': RegisterForm(label_suffix="")})
def post_register(request):
	form = RegisterForm(request.POST, label_suffix="")
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		User.objects.create_user(username=username, password=password)
		user = auth.authenticate(username=username, password=password)
		auth.login(request, user)
		return HttpResponse("Registration POSTED")
	else:
		return render(request, 'user_extension/register.html', {'form': form})

@handle_methods("POST")
def logout(request):
	raise Http404()

def post_logout(request):
	auth.logout(request)
	return redirect('user:home')