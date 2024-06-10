from django.http import HttpResponse
from .models import User, Comment

def index(request):
	user_list = User.objects.all()
	response = ''
	for user in user_list:
		response += f'<h2>{user.name} ({user.age})</h2>'
		comment_list = Comment.objects.all()
		for comment in comment_list:
			response += f'<p>{comment.text} (on {comment.created_at})</p>'

	return HttpResponse(response)