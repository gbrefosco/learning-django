from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()

	def __str__(self):
		return f'{self.name} ({self.age})'
	
class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
	created_at = models.DateTimeField(auto_now_add=True)
	text = models.CharField(max_length=140)

	def __str__(self):
		return f'Comment by {self.user.name}, on {self.created_at}'