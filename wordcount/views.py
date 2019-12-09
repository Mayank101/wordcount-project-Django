from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.strip().split()
    wordDict = {}
    for word in wordlist:
        if word in wordDict:
            #increase the count value
            wordDict[word] += 1
        else:
            #add new value 
            wordDict[word] = 1

    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1),reverse=True)         
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedWords':sortedWords})

def about(request):
    return render(request,'about.html')    