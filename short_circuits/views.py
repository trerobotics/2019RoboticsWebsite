from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def index (request):
	return render(request, 'short_circuits/index.html')

def about (request):
	return render(request, 'short_circuits/index.html')

def sponsors (request):
	return render(request, 'short_circuits/index.html')

@login_required
def team_info (request):
	return render(request, 'short_circuits/team_info.html')

def register(request):
	return render(request, 'registration/register.html')
