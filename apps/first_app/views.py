from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.serializers import serialize
import datetime, bcrypt
from .models import *

# Create your views here.
def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def index(request):
	return render(request, 'first_app/landing.html')

def register(request):
	check = User.objects.validateUser(request.POST)
	if request.method != 'POST':
		return redirect('/')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="registration")
			return redirect('/')
	if check[0] == True:
		#has password
		hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
		#create user
		user = User.objects.create(
			first_name = request.POST.get('first_name'),
			last_name = request.POST.get('last_name'),
			email = request.POST.get('email'),	
			password = hashed_pw,
		)

		#add user to session, logging them in
		request.session['user_id'] = user.id
		#route to user profile page
		return redirect('/user')

def user_profile(request):
	user = current_user(request)
	context = {
		'user': user,
		'trips': Trip.objects.filter(creator = user)
	}
	return render(request,'first_app/user_profile.html', context)

def create(request):
	user = current_user(request)
	print user.id
	return render(request, 'first_app/create_trip.html')

def add(request):
	user = current_user(request)
	print user

	trip = Trip.objects.create(
		title = request.POST.get('title'),
		destination = request.POST.get('destination'),
		description = request.POST.get('description'),
		start_date = request.POST.get('start_date'),
		end_date = request.POST.get('end_date'),
		creator = user
		)
	print trip
	return redirect('/user')





