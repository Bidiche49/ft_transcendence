from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from .models import User



def set_password(self, raw_password):
	self.password_hash = make_password(raw_password)

def check_password(self, raw_password):
	return check_password(raw_password, self.password_hash)

def register(request):
	if request.method == "POST":
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User(username=username, email=email)
		user.set_password(password)
		user.save()
		return JsonResponse({"message": "User registered successfully"}, status=201)
	return JsonResponse({"error": "Invalid request"}, status=400)


def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = User.objects.filter(username=username).first()
		if user and user.check_password(password):
			request.session['user_id'] = user.id
			return JsonResponse({"message": "Login successful"}, status=200)
		return JsonResponse({"error": "Invalid credentials"}, status=401)
	return JsonResponse({"error": "Invalid request"}, status=400)


def logout(request):
	if 'user_id' in request.session:
		del request.session['user_id']
	return JsonResponse({"message": "Logged out"}, status=200)


class AuthenticationMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not request.path.startswith('/login') and not request.path.startswith('/register'):
			user_id = request.session.get('user_id')
			if not user_id:
				return JsonResponse({"error": "Unauthorized"}, status=401)
		response = self.get_response(request)
		return response
