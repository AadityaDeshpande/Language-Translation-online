from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question,Answer,Choices
from django.urls import reverse
from django.template.loader import get_template
#def index(request):
	
def index(request):
    context = {}
    return render(request, 'trans/index.html', context)

def ans(request):
	if request.method == "POST":
		quest = request.POST.get("question")
		key = request.POST.get("key")
		print("\nSENTENSE= ",quest)
		print("KEY= ",key)
		print("")
	context = {
			"ans":quest    #quotes
			}	
	return render(request, 'trans/ans.html', context)
	    
	

