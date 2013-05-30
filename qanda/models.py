import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Movie(models.Model):
	title           = models.CharField(max_length = 500)
	poster          = models.ImageField(upload_to = 'media')
	pub_date        = models.DateTimeField(auto_now_add = True)
	author          = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.title
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
class Question(models.Model):
	movie           = models.ForeignKey(Movie, blank=True, null=True)
	question_text   = models.CharField(verbose_name = "Question", max_length = 1000)
	question_detail = models.CharField(verbose_name = "Details (Optional)", max_length = 5000, blank = True, null = True)
	q_pub_date      = models.DateTimeField(auto_now_add = True)
	q_author        = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.question_text
		
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
class Answer(models.Model):
	question         = models.ForeignKey(Question, blank=True, null=True)
	answer_text      = models.CharField(verbose_name = "", max_length = 20000)
	a_pub_date       = models.DateTimeField(auto_now_add = True)
	a_author         = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.answer_text
		
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
class MovieForm(ModelForm):
	def save(self, user = None, force_insert = False, force_update = False, commit = True):
		q = super(MovieForm, self).save(commit = False)
		q.author = user
		if commit:
			q.save()
		return q
		
	class Meta:
		model = Movie
		exclude = ('author', 'pub_date')
		widgets = {
			'title': Textarea(attrs={'cols': 30, 'rows': 1}),
		}
			
class QuestionForm(ModelForm):
	def save(self, user = None, force_insert = False, force_update = False, commit = True):
		q = super(QuestionForm, self).save(commit = False)
		q.q_author = user
		if commit:
			q.save()
		return q
		
	class Meta:
		model = Question
		exclude = ('movie', 'q_author', 'q_pub_date')
		widgets = {
			'question_detail': Textarea(attrs={'cols':22, 'rows':8}),
			'question_text': Textarea(attrs={'cols':22, 'rows':1}),
		}
		
class AnswerForm(ModelForm):
	def save(self, user = None, force_insert = False, force_update = False, commit = True):
		q = super(AnswerForm, self).save(commit = False)
		q.a_author = user
		if commit:
			q.save()
		return q
	
	class Meta:
		model = Answer
		exclude = ('question', 'a_author', 'a_pub_date')
		widgets = {
			'answer_text': Textarea(attrs={'cols':78, 'rows':5}),
		}
 
class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True)
	
	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
	
	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
 
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	