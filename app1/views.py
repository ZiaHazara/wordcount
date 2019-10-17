from django.shortcuts import render

from django.http import HttpResponse
import operator
# Create your views here.
def home(request):
    return render(request,'home.html')


def count(request):
    fullText = request.GET["fullText"]
    wordcount = fullText.split()
    worddict = {}
    for w in wordcount:
        if w in worddict:
            worddict[w] += 1
        else:
            worddict[w] = 1
    worddict = sorted(worddict.items(),key = operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{"fullText":fullText,"count":len(wordcount),"worddict":worddict})