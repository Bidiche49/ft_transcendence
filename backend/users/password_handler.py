from django.contrib.auth.hashers import make_password, check_password

def set_password(self, raw_password):
	self.password_hash = make_password(raw_password)

def check_password(self, raw_password):
	return check_password(raw_password, self.password_hash)
