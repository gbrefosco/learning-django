# from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
	user_list = User.objects.all()
	user_list_string = [str(user) for user in user_list]
	response = '<br>'.join(user_list_string)

	return HttpResponse(response)