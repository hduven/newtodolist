from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

class Category(models.Model):
	category_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


	def __str__(self):
		return self.category_name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Description(models.Model):
    description_text = models.TextField() 
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)


    def __str__(self):
        return self.description_text



    