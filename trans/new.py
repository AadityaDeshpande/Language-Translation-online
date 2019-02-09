def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from textblob import TextBlob
#import textblob

def pol(inp):
	inp=TextBlob(inp)
	return inp.polarity


def sub(inp):
	inp=TextBlob(inp)
	return inp.subjectivity

def asse(inp):
	arr=[]
	inp=TextBlob(inp)
	var=inp.sentiment_assessments
	print ("this :: ",var)   #this returns a list of elements
	for i in var[2]:
		#print(i[0][0])
		ans=i[0]		#ERROR
		arr.append(ans)
	return arr	#PROJECT.HTML


def speech(inp):
	inp=TextBlob(inp)	#this returns a list of elements
	arr=inp.tags		#text = word_tokenize("And now for something completely different")
	return arr			#nltk.pos_tag(text)


def main():
	#inp=input("Enter the string")
	inp="this movie was good but requires an improvement. we will work on in and will move foward.this is worst movie"
	polarity=pol(inp)
	print(polarity)
	var=sub(inp)
	print(var)
	ass=asse(inp)
	for i in ass:
		print(i)
	ass=speech(inp)  #nltk.help.upenn_tagset()
	for i in ass:
		print(i)	#DIRECCT MAPPING WITH A DATA SET
#inp : string  output list of token 

# and used in slicing
if __name__=="__main__":
	main()
