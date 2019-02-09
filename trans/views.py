from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question,Answer,Choices
from django.urls import reverse
from django.template.loader import get_template

from .lang import det,trans
from .data import ser,display,rev
from .net import is_connected
from .new import pol,sub,asse,speech
#def index(request):
	
def index(request):
    context = {}
    #to do something first
    return render(request, 'trans/index.html', context)

def ans(request):
	context={}
	
	if request.method == "POST" and is_connected()==True:
		quest = request.POST.get("question")
		key = (request.POST.get("key"))
		print("\nSENTENSE= ",quest)
		print("KEY= ",key)
		print("")
		if quest != "" and key !="":
			key=rev(key)
			detectl=det(quest)
			answer=trans(quest,key)
			print("return by det is ",detectl)
			detectl=ser(detectl)
			context = {
					"query":quest,
					"key":ser(key),
					"ans":answer,
					"detect":detectl    #quotes
					}
		else:
			err="NO INPUT DETECTED PLZ ENTER DATA (reply from server)"
			context = {
					"ans":err,
					"detect":err
			}
	else:
		noint="PLEASE CONNECT TO INTERNET..!!!"
		context = {
				"query":request.POST.get("question"),
				"key":ser((request.POST.get("key")).lower()),
				"ans":noint,
				"detect":noint    #quotes
				}
		print(noint)				
	return render(request, 'trans/ans.html', context)

def analysis(request):
	context = {}
	if request.method == "POST":
		quest = request.POST.get("question")
		print("\nSENTENSE= ",quest)
		polarity1=pol(quest)
		subjectivity1=sub(quest)
		assement1=asse(quest)
		speech1=speech(quest)
		context = {
				"string":quest,
				"polar":polarity1,
				"subject":subjectivity1,
				"asse":assement1,
				"arr":speech1
				}
				
	return render(request, 'trans/analysis.html', context)
		    
	

