from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

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
		#route to profile form page
		return redirect('/')