from django.db import models

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=2000)
	def __str__(self):
		return self.question_text

class Answer(models.Model):
	answer_text = models.CharField(max_length=2000)		
	def __str__(self):
		return self.answer_text

class Choices(models.Model):
	choice_text = models.CharField(max_length=2000)		
	def __str__(self):
		return self.choice_text
		
