from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login

from .forms import *

def handle_methods(*methods):
	def decorator(f):
		def wrapper(request, *args, **kw):
			for method in methods:
				if request.method == method.upper():
			  		func = globals()[method.lower() + "_" + f.__name__]
			  		return func(request)
			return f(request)
		return wrapper
	return decorator


def index(request):
	return HttpResponse("Welcome")

@handle_methods("POST")
def login(request):
	form = LoginForm(request.POST, label_suffix="")
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse("Login POSTED")
	return render(request, 'user_extension/login.html', {'form': form})
def post_login(request):
	return HttpResponse("Login POSTED")

@handle_methods("POST")
def register(request):
	return render(request, 'user_extension/register.html', {'form': RegisterForm(label_suffix="")})
def post_register(request):
	form = RegisterForm(request.POST, label_suffix="")
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = User.objects.create_user(username=username, password=password)
		login(request, user)
		return HttpResponse("Registration POSTED")
	else:
		return render(request, 'user_extension/register.html', {'form': form})

@handle_methods("POST")
def logout(request):
	raise Http404()

def post_logout(request):
	logout(request)