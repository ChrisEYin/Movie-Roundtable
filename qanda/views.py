from django.http import HttpResponse
from qanda.models import Movie, Question, Answer, MovieForm, QuestionForm, AnswerForm, UserCreateForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import auth
from django import forms
import datetime
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from voting.models import Vote
from django.db.models import Sum

def index(request):
	r     = Movie.objects.all().order_by('-pub_date')
	form  = UserCreateForm()
	return render_to_response('qanda/index.html', 
								{'latest_movie_list': r, 'form':form}, 
								context_instance = RequestContext(request))
	
def register(request):
	if request.method == 'POST':
		form           = UserCreateForm(request.POST)
		if form.is_valid():
			new_user   = form.save()
			new_user   = auth.authenticate(username = request.POST['username'],
									       password = request.POST['password1'])
			auth.login(request, 
					   new_user)
			return HttpResponseRedirect("/home/")
	else:
		form = UserCreateForm()
	return render_to_response("registration/register.html", 
								{'form': form}, 
								context_instance = RequestContext(request))

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q      = request.GET['q']
		movies = Movie.objects.filter(title__icontains=q)
		return render_to_response('qanda/search_results.html', 
									{'movies':movies, 'query':q},
									context_instance = RequestContext(request))
									
def forgot(request):
	return render_to_response('registration/forgot_password.html',
								context_instance = RequestContext(request))
	
def add_movie(request):
	if request.method     == "POST":
		form               = MovieForm(request.POST, request.FILES)   
		if form.is_valid():
			form.save(user = request.user)
			return HttpResponseRedirect("/home/")
	else:
		form               = MovieForm()
	return render_to_response("qanda/add_movie.html", 
								{'form': form}, 
								context_instance = RequestContext(request))
	
def questions(request, movie_id):
	p     = Movie.objects.get(pk=movie_id)
	k     = Question.objects.filter(movie = p).order_by('-q_pub_date')
	#top   = generic_annotate(k, Vote.object, Sum('vote'))
	form1 = UserCreateForm()
	form2 = QuestionForm()
	return render_to_response('qanda/questions.html', 
								{'movie':p, 'the_question':k, 'form1':form1, 'form2': form2}, 
								context_instance = RequestContext(request))
	
def add_question(request, movie_id):
	if request.method       == "POST":
		form                 = QuestionForm(request.POST, request.FILES)
		if form.is_valid():
			question         = form.save(user = request.user)
			question.movie   = Movie.objects.get(pk = movie_id)
			question.save()
			return HttpResponseRedirect("/home/%s/" % movie_id)
	else:
		form                 = QuestionForm()
		form.q_author        = request.user
		form.movie           = Movie.objects.get(pk = movie_id)
	return render_to_response("qanda/add_question.html", 
								{'form': form}, 
								context_instance = RequestContext(request))
								
def back_url(request, object_id):
	movie_id = object_id
	return HttpResponseRedirect(default_back_url)

def answers(request, movie_id, question_id):
	p = Movie.objects.get(pk=movie_id)
	k = Question.objects.filter(movie=p)
	r = Question.objects.get(id = question_id)
	a = Answer.objects.filter(question_id = question_id).order_by('a_pub_date')
	form = AnswerForm()
	return render_to_response('qanda/answers.html',
								{'movie': p, 'the_question':k, 'the_answers':a, 'question':r, 'form': form}, 
								context_instance = RequestContext(request))

def add_answer(request, movie_id, question_id):
	if request.method       == "POST":
		form                 = AnswerForm(request.POST, request.FILES)
		if form.is_valid():
			answer           = form.save(user = request.user)
			answer.question  = Question.objects.get(id = question_id)
			answer.save()
			return HttpResponseRedirect("/home/%s/" % (movie_id))
	else:
		form                 = AnswerForm()
	return render_to_response("qanda/add_answer.html", 
								{'form': form}, 
								context_instance = RequestContext(request))