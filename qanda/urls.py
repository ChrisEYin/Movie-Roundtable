from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *
from qanda.models import Question
from voting.views import vote_on_object
from qanda.models import Movie

urlpatterns = patterns('qanda.views',
	url(r'^$', 'index'),
	url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
	url(r'^register/$', 'register'),
	url(r'^profile/$', 'index'),
	url(r'^search/$', 'search'),
	url(r'^add_movie/$', 'add_movie'),
	url(r'^(?P<movie_id>\d+)/$', 'questions'),
	url(r'^(?P<movie_id>\d+)/add_question/$', 'add_question'),
	url(r'^(?P<movie_id>\d+)/(?P<question_id>\d+)/$', 'answers'),
	url(r'^(?P<movie_id>\d+)/(?P<question_id>\d+)/add_answer/$', 'add_answer'),
	url(r'^(?P<object_id>\d+)/(?P<direction>up|down|clear)/vote/$', 
			vote_on_object, dict(model = Question, template_object_name = 'question',
			template_name = 'qanda/confirm_vote.html', post_vote_redirect = '/home/', allow_xmlhttprequest=True)),
	url(r'^forgot/$', 'forgot'),
)