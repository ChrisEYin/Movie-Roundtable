from django.contrib import admin
from qanda.models import Movie, Question, Answer

class QuestionInline(admin.StackedInline):
	model = Question
	extra = 3
	
class AnswerInline(admin.StackedInline):
	model = Answer

class MovieAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()
		
	fieldsets = [
		('Title', {'fields': ['title']}),
		('Poster', {'fields': ['poster']}),
	]
	
	#inlines = [QuestionInline]
	list_display = ('title', 'pub_date', 'poster', 'author')
	search_fields = ['question']
	
	
class QuestionAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.q_author = request.user
		obj.save()
	
	fieldsets = [
		('Movie', {'fields': ['movie']}),
		('Question', {'fields': ['question_text']}),
		('Detail', {'fields': ['question_detail']}),
	]
	
	list_display = ('movie', 'question_text', 'q_pub_date', 'q_author')
	#inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.a_author = request.user
		obj.save()
		
	fieldsets = [
		('Question', {'fields': ['question']}),
		('Answer', {'fields': ['answer_text']}),
	]
		
	list_display = ('answer_text', 'question', 'a_pub_date', 'a_author')

	
admin.site.register(Movie, MovieAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)