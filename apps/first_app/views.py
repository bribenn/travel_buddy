from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
	return render(request, 'first_app/landing.html')
