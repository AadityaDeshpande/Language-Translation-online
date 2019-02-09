def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier 
from textblob.classifiers import DecisionTreeClassifier 
import csv
def det(sent):
 try:
  sent=TextBlob(sent)
  z=sent.detect_language()
  print("Entered language is key code =",z)
  return z
 except:
  print("Exception caught in det ")
  return sent+" (returned as it is.please Enter a valid string)" 

def trans(sent,key):
 try:
  sent=TextBlob(sent)
  key=TextBlob(key)
  #temp = sent.detect_language()     #remove this comments if want to check current lang == expected lang
  #temp = TextBlob(temp)
  #print("this is a temp::: ",temp)
  #if temp==key:
  # raise ValueError
  #print(sent.translate(to=f'{key}'))
  return sent.translate(to=f'{key}')
 #except ValueError:
 # print("Same language exception")
 # return sent+" (You have typed a same converting language key, so no change..!)" 
 except:
  print("Exception caught in trans ")
  return sent+" (NOTE: string returned as it is.)" 
 
def r_csv():
 with open("codes.csv") as f:
  reader = csv.reader(f)
  for row in reader:
   print(''.join(row))
   
   
def main():
 sent=TextBlob(input("Enter a Sentence to translate: "))
 key =TextBlob(input("Enter a KEY: ")) 
 det(sent)
 trans(sent,key)
  
if __name__=='__main__':
 main()   
