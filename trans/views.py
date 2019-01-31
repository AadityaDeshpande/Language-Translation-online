from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question,Answer,Choices
from django.urls import reverse
#def index(request):
	
def index(request):
	#my_question = 
    context = {}
    return render(request, 'trans/index.html', context)

def ans(request):
	question = {}
	#question = dict(question.question_text.get(request.POST['question']))
	#print(question)
	return render(request, 'trans/ans.html', question)
	    
	

